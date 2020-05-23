'''IR Codes for Samsung BluRay.

These are derived from code set #1235 from the Global Cache IR code database ("Control Tower").
They seem to have been compiled from multiple sources, hence the slight variations in timing
from one code to another.
'''


CARRIER_FREQUENCY = 37000
REPEAT_OFFSET = 3

IR_CODES = {
    "AUDIO":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,16,16,47,16,47,16,16,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,16,16,47,16,2741",

    "BD/SD":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,47,16,47,16,47,16,16,16,16,16,47,16,2741",

    "CANCEL":"127,63,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,49,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,49,16,16,16,16,16,16,16,16,16,16,16,49,16,49,16,49,16,16,16,16,16,49,16,49,16,16,16,16,16,2741",

    "CURSOR_DOWN":"127,64,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,49,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,49,16,16,16,16,16,16,16,16,16,49,16,16,16,49,16,49,16,16,16,49,16,49,16,16,16,16,16,2741",

    "CURSOR_ENTER":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,47,16,47,16,16,16,16,16,2741",

    "CURSOR_LEFT":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,47,16,16,16,16,16,16,16,16,16,47,16,47,16,47,16,47,16,16,16,47,16,47,16,16,16,16,16,2741",

    "CURSOR_RIGHT":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,47,16,47,16,47,16,16,16,16,16,2741",

    "CURSOR_UP":"127,63,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,49,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,16,16,49,16,16,16,16,16,16,16,16,16,49,16,49,16,16,16,49,16,16,16,49,16,49,16,16,16,16,16,2741",

    "DIGIT_0":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,47,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_1":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_2":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_3":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_4":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,16,16,47,16,16,16,16,16,16,16,47,16,47,16,16,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_5":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_6":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,47,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_7":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_8":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,47,16,47,16,47,16,16,16,16,16,47,16,16,16,47,16,2741",

    "DIGIT_9":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,47,16,2741",

    "DISPLAY":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,16,16,47,16,16,16,16,16,2741",

    "ENTER":"127,63,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,47,15,15,15,47,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,47,15,47,15,15,15,47,15,15,15,47,15,47,15,15,15,47,15,15,15,47,15,47,15,47,15,2741", # TBR

    "EXIT":"127,63,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,47,15,15,15,47,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,15,15,15,15,47,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,47,15,47,15,2748", # TBR

    "FORWARD":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,47,16,47,16,16,16,47,16,2741",

    "FUNCTION_BLUE":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,47,16,47,16,47,16,47,16,2741",

    "FUNCTION_GREEN":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,47,16,16,16,16,16,47,16,47,16,47,16,47,16,2741",

    "FUNCTION_RED":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,47,16,47,16,2741",

    "FUNCTION_YELLOW":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,16,16,47,16,47,16,47,16,47,16,2741",

    "MENU_HOME":"127,63,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,48,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,48,16,48,16,16,16,48,16,16,16,48,16,16,16,48,16,48,16,48,16,16,16,16,16,48,16,48,16,48,16,2741",

    "MENU_MAIN":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,47,16,16,16,16,16,47,16,47,16,47,16,16,16,47,16,16,16,47,16,16,16,16,16,2741",

    "MENU_POPUP":"127,63,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,48,16,16,16,48,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,16,16,48,16,16,16,48,16,16,16,16,16,16,16,16,16,48,16,48,16,48,16,2741",

    "MENU_SETUP":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,2741",

    "MENU_SUB":"127,63,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,47,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,15,15,15,15,15,15,47,15,47,15,15,15,15,15,2741",

    "NEXT":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,47,16,47,16,47,16,47,16,47,16,2741",

    "OPEN":"127,65,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,49,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,16,16,16,16,16,16,49,16,49,16,17,16,49,16,2731",

    "PAUSE":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,47,16,16,16,47,16,2741",

    "PIP":"127,63,15,15,15,48,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,48,15,15,15,15,15,15,15,15,15,15,15,15,15,48,15,48,15,15,15,48,15,48,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,48,15,48,15,15,15,48,15,15,15,48,15,15,15,48,15,48,15,48,15,15,15,15,15,48,15,48,15,48,15,2741",

    "PLAY":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,47,16,47,16,16,16,47,16,2741",

    "POWER_OFF":"127,65,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,49,16,48,16,16,16,48,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,48,16,48,16,48,16,48,16,48,16,48,16,16,16,16,16,48,16,48,16,48,16,48,16,16,16,16,16,16,16,48,16,2731",

    "POWER_ON":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,47,16,47,16,47,16,16,16,16,16,16,16,47,16,47,16,47,16,16,16,16,16,16,16,47,16,2741",

    "PREVIOUS":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,47,16,16,16,16,16,47,16,47,16,47,16,47,16,47,16,2741",

    "RE_MASTER":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,47,16,16,16,47,16,47,16,47,16,47,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,2741",

    "RETURN":"127,63,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,47,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,15,15,15,15,15,15,15,15,15,15,15,15,47,15,47,15,15,15,15,15,15,15,47,15,47,15,15,15,15,15,2741",

    "REVERSE":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,47,16,47,16,16,16,47,16,2741",

    "STATUS":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,47,16,47,16,47,16,16,16,47,16,16,16,47,16,47,16,47,16,47,16,16,16,47,16,47,16,47,16,2741",

    "STOP":"127,63,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,47,16,47,16,16,16,47,16,2741",
}
