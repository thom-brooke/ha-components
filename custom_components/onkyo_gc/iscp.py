"""Integra Serial Communications Protocol for AV Receiver (version 1.38)

Onkyo protocol for controlling A/V equipment.  This module implements
the SERIAL (RS232) version of the protocol.  If you are looking for
ethernet, you probably want "onkyo-eiscp".  Even if you aren't looking
for ethernet, yuo may want to consider using onkyo-eiscp anyway, as
it is more complete and addresses other receiver models.

If onkyo-eiscp is more complete, why does this module exist?
Because it is easier and simpler.  The only part of onkyo-eiscp that 
would be usable would be command formatting: one dict and one function out
of dozens.  And it would still require considerable processing to make it "easy".

Nothing wrong with that.  It's just a choice.  My choice is a close-to-the-ground
basic interface.  Ta da.

"""

# General protocol constants:

# Every command and response starts with the same PREFIX:
PREFIX = '!1'

# commands (sent TO the receiver) are terminated with a CR.
# responses/notifications FROM the receiver are terminated with a SUB (Ctrl-Z)
SUFFIX_CMD = '\r'
SUFFIX_MSG = '\x1a'

# @todo: Exception for invalid op/arg?

# Constants for operations and arguments.
# Tailored for my needs; main zone only.

POWER  = 'PWR'
MUTING = 'AMT'
INPUT  = 'SLI'
VOLUME = 'MVL'
OSD    = 'OSD'
MODE   = 'LMD'

# common args
OFF = '00'
ON  = '01'
UP = 'UP'
DOWN = 'DOWN'

ALL = 'ALL'

QUERY = 'QSTN'

# op-specific args:

# AMT
TOGGLE = 'TG'

# OSD
MENU = 'MENU'
RIGHT = 'RIGHT'
LEFT = 'LEFT'
ENTER = 'ENTER'
EXIT = 'EXIT'
AUDIO = 'AUDIO'
VIDEO = 'VIDEO'
HOME = 'HOME'
QUICK = 'QUICK' # TBR
PREVIEW = 'IPV' # TBR (Instaprevue)

# SLI
VIDEO1 = '00'
VCR_DVR = VIDEO1
STB_DVR = VIDEO1
VIDEO2 = '01'
CBL_SAT = VIDEO2
VIDEO3 = '02'
GAME_TV = VIDEO3
GAME = VIDEO3
GAME1 = VIDEO3
VIDEO4 = '03'
AUX = VIDEO4
AUX1 = VIDEO4
VIDEO5 = '04'
AUX2 = VIDEO5
GAME2 = VIDEO4
# '05' '06' '07', '08', '09'
DVD = '10'
BD_DVD = DVD
# '11' '12'
TAPE_1 = '20'
TV_TAPE = TAPE_1
# '21'
PHONO = '22'
CD = '23'
TV_CD = CD
FM = '24'
AM = '25'
TUNER = '26'
# '27' '28' '29' '2A' '2B' '2C' '2D' '2E' '2F'
# '30' '31' '32' '33'
# '40' '41' '42' '44' '45'
# '55' '56' '57'

INPUT_MAP = {
    VIDEO1: 'VCR/DVR',
    VIDEO2: 'CBL/SAT',
    VIDEO3: 'GAME/TV',
    VIDEO4: 'AUX',
    VIDEO5: 'AUX2',
    DVD: 'DVD',
    TAPE_1: 'TAPE',
    PHONO: 'PHONO',
    CD: 'CD',
    FM: 'FM',
    AM: 'AM',
    TUNER: 'TUNER'
    }

VIDEO_INPUTS = (VIDEO1, VIDEO2, VIDEO3, VIDEO4, VIDEO5, DVD)
AUDIO_INPUTS = (TAPE_1, PHONO, CD, FM, AM, TUNER)

# LMD
STEREO = '00'
DIRECT = '01'
SURROUND = '02'
# FILM = '03'
# GAME_RPG = FILM
THX = '04'
# '05' '06'
MONO_MOVIE = '07'
ORCHESTRA = '08'
UNPLUGGED = '09'
STUDIO_MIX = '0A'
TV_LOGIC = '0B'
ALL_CH_STEREO = '0C'
THEATER_DIMENSIONAL = '0D'
# '0E'
MONO = '0F'
PURE_AUDIO = '11'
# '12'
FULL_MONO = '13'
# '14' '15' '16' '1F'
STRAIGHT_DECODE = '40'
# '41'
THX_CINEMA = '42'
THX_SURROUND = '43'
# '44' '45' '50' '51'
THX_GAMES = '52'
PLIIX_MOVIE = '80'
DOLBY_SURROUND = PLIIX_MOVIE
PLIIX_MUSIC = '81'
NEO6_CINEMA = '82'
DTS_X = NEO6_CINEMA
NEO6_MUSIC = '83'
PLIIX_THX = '84'
DOLBY_SURROUND_THX = PLIIX_THX
NEO6_THX = '85'
DTS_NEURAL_X = NEO6_THX
PLIIX_GAME = '86'
# '87'
NEURAL_THX = '88'
PLIIX_THX_GAMES = '89'
DOLBY_SURROUND_THX_GAMES = PLIIX_THX_GAMES
NEO6_THX_GAMES = '8A'
DTS_NEURAL_X_THX_GAMES = NEO6_THX_GAMES
# '8B' '8C' '8D' '8E' '8F'
# '90' '91' '92' '93' '94' '95' '96' '97' '98' '9A'
# 'A0' 'A1' 'A2' 'A3' 'A4' 'A5' 'A6' 'A7'
# 'FF'

MODE_MAP = {
    STEREO: 'STEREO',
    DIRECT: 'DIRECT',
    SURROUND: 'SURROUND',
    THX: 'THX',
    MONO_MOVIE: 'MONO MOVIE',
    ORCHESTRA: 'ORCHESTRA',
    UNPLUGGED: 'UNPLUGGED',
    STUDIO_MIX: 'STUDIO MIX',
    TV_LOGIC: 'TV LOGIC',
    ALL_CH_STEREO: 'ALL CH STEREO',
    THEATER_DIMENSIONAL: 'THEATER-DIMENSIONAL',
    MONO: 'MONO',
    PURE_AUDIO: 'PURE AUDIO',
    FULL_MONO: 'FULL MONO',
    STRAIGHT_DECODE: 'STRAIGHT DECODE',
    THX_CINEMA: 'THX CINEMA',
    THX_SURROUND: 'THX SURROUND',
    THX_GAMES: 'THX GAMES',
    PLIIX_MOVIE: 'PLIIx MOVIE',
    PLIIX_MUSIC: 'PLIIx MUSIC',
    NEO6_CINEMA: 'Neo:6 CINEMA',
    NEO6_MUSIC: 'Neo:6 MUSIC',
    PLIIX_THX: 'PLIIx THX CINEMA',
    NEO6_THX: 'Neo:6 THX CINEMA',
    PLIIX_GAME: 'PLIIx GAME',
    NEURAL_THX: 'NEURAL THX',
    PLIIX_THX_GAMES: 'PLIIx THX GAMES',
    NEO6_THX_GAMES: 'Neo:6 THX GAMES'
    }

# basic/universal commands.
# this will get trimmed/tailored by receiver model in ISCP_device class
COMMANDS = {
    POWER: (OFF, ON, ALL, QUERY),
    MUTING: (OFF, ON, TOGGLE, QUERY),
    INPUT: (QUERY), # plus per-model codes
    MODE : (QUERY), # plus per-model codes
    OSD  : (MENU, UP, DOWN, LEFT, RIGHT, ENTER, EXIT, AUDIO, VIDEO, HOME, QUICK, PREVIEW),
    VOLUME: (UP, DOWN, QUERY) # plus discrete levels
    }

# Specific support by receiver model
SUPPORT_TXSR805 = {
    INPUT: (VIDEO1, VIDEO2, VIDEO3, VIDEO4, VIDEO5, DVD, TAPE_1, PHONO, CD, FM, AM, TUNER),
    MODE: (STEREO, DIRECT, SURROUND, THX, MONO_MOVIE, ORCHESTRA, UNPLUGGED, STUDIO_MIX, TV_LOGIC,
           ALL_CH_STEREO, THEATER_DIMENSIONAL, MONO, PURE_AUDIO, FULL_MONO, STRAIGHT_DECODE,
           THX_CINEMA, THX_SURROUND, THX_GAMES, PLIIX_MOVIE, PLIIX_MUSIC, NEO6_CINEMA,
           NEO6_MUSIC, PLIIX_THX, NEO6_THX, PLIIX_GAME, NEURAL_THX, PLIIX_THX_GAMES, NEO6_THX_GAMES),
    VOLUME: 80
    }

MODEL_SUPPORT = {
    'TX-SR805': SUPPORT_TXSR805,
    'TX-SR875': SUPPORT_TXSR805
    }

def get_models():
    return MODEL_SUPPORT.keys()

class ISCP_device:

    def __init__(self, model):
        support = MODEL_SUPPORT[model]
        self.max_vol = support[VOLUME]
        self.commands = dict(COMMANDS) # make a copy
        vol_levels = tuple(["{:02X}".format(i) for i in range(self.max_vol+1)])
        self.commands[VOLUME] = self.commands[VOLUME] + vol_levels
        self.inputs = {k: INPUT_MAP[k] for k in support[INPUT]}
        self.modes = {k: MODE_MAP[k] for k in support[MODE]}
        
    def mk_command(self, op, arg, to_send=True):
        # verify op is in self.commands
        # verify arg is in self.commands[op]
        return PREFIX + op + arg + (SUFFIX_CMD if to_send else '')

    def mk_query(self, op, to_send=True):
        return self.mk_command(op, QUERY, to_send)

    def mk_tuning(self, freq):
        # as it turns out, we can send the TUN command with the full frequency.
        # so we should, here.  Question about whether to also return input select
        # (e.g., to AM, or FM or TUNER).
        pass

    def arg_volume(self, level):
        """Return volume argument value for level in 0 .. 1

        Scale normalized 'level' according to "max_vol" for device..
        """
        norm = max(0, min(1, level))
        return "{:02X}".format(round(norm * self.max_vol))

    def normalize_volume(self, arg):
        """Normalize a receiver volume level to range 0 .. 1"""
        return int(arg, 16) / self.max_vol
    
    # @todo: other arg "formatters" to produce dynamic argument values
    
    def parse(self, cmd):
        """Parse (split) a complete ISCP message into <op> and <arg>.

        The 'cmd' should be a string (not bytes).
        Expect 'cmd' to include the leading PREFIX, but NOT include the trailing suffix.
        """
        if not cmd.startswith(PREFIX):
            raise ValueError(f"Missing PREFIX in ->{cmd}<-")

        command = cmd[len(PREFIX):]
        
        # For laziness, assume all operators are three characters long.
        # That's true so far, but may not always be.
        OP_LEN = len(POWER)
        op = command[0:OP_LEN]
        arg = command[OP_LEN:]

        return (op, arg)

    # @todo: individual argument (result) parsers that split up content (e.g., IFA and IFV fields).

    def valid_args(self, op):
        return self.commands[op]



