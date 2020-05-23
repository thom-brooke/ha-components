'''IR Codes for Samsung BluRay.

These are derived from code set #26 from the Global Cache IR code database ("Control Tower"),
which is not entirely correct.  In fact, as given, none of the codes worked at all for me; 
hence the discussion below about the proper protocol format.  The "MENU_HOME" code comes from
set #5400, for Samsung UBD-K 4K player.

According to http://www.hifi-remote.com/johnsfine/DecodeIR.html
the "Samsung36" IR protocol goes like this:
* Carrier frequency = 38 kHz
* Base Time = 500 usec
* 0-bit = on/1, off/1  (i.e., on 500 usec then off 500 usec)
* 1-bit = on/1, off/3
* the protocol format is:
  * lead-in: on/9, off/9
  * device: 8-bits
  * subdevice: 8-bits
  * padding: on/1, off/9
  * data: 12-bits
  * off 68 usec
  * data: 8-bits
  * stop: on/1, off/118+

This translates to 1 period (@ 38kHz) = 26.3 usec.
So, GC durations are:
* lead in: 171,171
* 0-bit: 19, 19
* 1-bit: 19, 57
* stop: 19, 2185

The only hitch is the extra 68 usec space after the 28th bit.
To account for this, we extend the "off" time by 3 (periods).
So you'll see either 22 or 60 for "off" times in bit 28.
'''

CARRIER_FREQUENCY = 38000
REPEAT_OFFSET = 3

IR_CODES = {
"3D":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,57,19,57,19,57,19,19,19,22,19,57,19,57,19,19,19,19,19,19,19,19,19,57,19,57,19,2185",

"AUDIO":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,57,19,19,19,19,19,57,19,19,19,22,19,19,19,57,19,19,19,57,19,57,19,19,19,57,19,57,19,2185",

"BONUS_VIEW":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,19,19,19,19,57,19,57,19,19,19,22,19,19,19,19,19,57,19,57,19,19,19,19,19,57,19,57,19,2185",

"CANCEL":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,57,19,57,19,57,19,19,19,19,19,22,19,19,19,19,19,19,19,19,19,19,19,57,19,57,19,57,19,2185",

"CURSOR_DOWN":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,57,19,57,19,19,19,19,19,22,19,19,19,57,19,57,19,19,19,19,19,57,19,57,19,57,19,2185",

"CURSOR_ENTER":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,57,19,57,19,19,19,19,19,22,19,57,19,57,19,19,19,19,19,19,19,57,19,57,19,57,19,2185",

"CURSOR_LEFT":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,169,19,57,19,57,19,57,19,19,19,57,19,57,19,19,19,57,19,57,19,19,19,19,19,22,19,19,19,19,19,57,19,19,19,19,19,57,19,57,19,57,19,2185",

"CURSOR_RIGHT":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,57,19,57,19,19,19,19,19,22,19,57,19,19,19,57,19,19,19,19,19,57,19,57,19,57,19,2185",

"CURSOR_UP":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,57,19,57,19,19,19,19,19,22,19,57,19,57,19,57,19,19,19,19,19,57,19,57,19,57,19,2185",

"DIGIT_0":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,19,19,57,19,19,19,19,19,19,19,22,19,19,19,19,19,57,19,19,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_1":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,22,19,57,19,19,19,57,19,57,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_2":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,19,19,19,19,19,19,19,19,19,19,22,19,19,19,19,19,57,19,57,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_3":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,22,19,57,19,57,19,19,19,57,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_4":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,57,19,19,19,19,19,19,19,19,19,22,19,19,19,57,19,19,19,57,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_5":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,57,19,19,19,19,19,19,19,19,19,22,19,57,19,19,19,19,19,57,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_6":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,22,19,19,19,19,19,19,19,57,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_7":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,22,19,57,19,57,19,57,19,19,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_8":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,57,19,19,19,19,19,19,19,22,19,19,19,57,19,57,19,19,19,57,19,57,19,57,19,57,19,2185",

"DIGIT_9":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,57,19,19,19,19,19,19,19,22,19,57,19,19,19,57,19,19,19,57,19,57,19,57,19,57,19,2185",

"DISC_2_DIGITAL":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,57,19,22,19,57,19,57,19,57,19,57,19,57,19,57,19,19,19,57,19,2185",

"FORWARD":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,57,19,19,19,57,19,19,19,19,19,22,19,19,19,57,19,19,19,57,19,19,19,57,19,57,19,57,19,2185",

"FULL_SCREEN":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,57,19,57,19,57,19,19,19,22,19,19,19,57,19,57,19,19,19,19,19,19,19,57,19,57,19,2185",

"FUNCTION_BLUE":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,19,19,19,19,57,19,19,19,22,19,57,19,57,19,19,19,57,19,57,19,19,19,57,19,57,19,2185",

"FUNCTION_GREEN":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,19,19,19,19,57,19,19,19,22,19,57,19,19,19,57,19,57,19,57,19,19,19,57,19,57,19,2185",

"FUNCTION_RED":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,19,19,19,19,57,19,19,19,22,19,19,19,57,19,57,19,57,19,57,19,19,19,57,19,57,19,2185",

"FUNCTION_YELLOW":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,19,19,19,19,19,19,57,19,19,19,22,19,19,19,19,19,57,19,57,19,57,19,19,19,57,19,57,19,2185",

"INFO":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,57,19,57,19,57,19,19,19,19,19,22,19,57,19,19,19,19,19,19,19,19,19,57,19,57,19,57,19,2185",

"INPUT_HDMI":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,57,19,22,19,19,19,57,19,57,19,57,19,57,19,57,19,19,19,57,19,2185",

"INTERNET":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,57,19,57,19,57,19,19,19,22,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,57,19,2185",

"MARKER":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,57,19,19,19,57,19,19,19,22,19,19,19,57,19,57,19,19,19,57,19,19,19,57,19,57,19,2185",

"MENU_DISC":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,57,19,57,19,57,19,19,19,19,19,22,19,19,19,57,19,19,19,19,19,19,19,57,19,57,19,57,19,2185",

"MENU_HOME":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,57,19,19,19,57,19,19,19,19,19,22,19,57,19,19,19,19,19,57,19,19,19,57,19,57,19,57,19,2185",
    
"MENU_MAIN":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,57,19,57,19,57,19,19,19,19,19,22,19,19,19,57,19,19,19,19,19,19,19,57,19,57,19,57,19,2185",

"MENU_POPUP":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,22,19,57,19,57,19,57,19,57,19,57,19,19,19,57,19,57,19,2185",

"NETFLIX":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,57,19,57,19,57,19,57,19,19,19,22,19,57,19,19,19,19,19,19,19,19,19,19,19,57,19,57,19,2185",

"NEXT":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,19,19,57,19,19,19,19,19,22,19,19,19,57,19,57,19,57,19,19,19,57,19,57,19,57,19,2185",

"OPEN":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,22,19,19,19,57,19,57,19,57,19,57,19,57,19,57,19,57,19,2185",

"PANDORA":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,57,19,57,19,57,19,57,19,19,19,22,19,19,19,19,19,19,19,19,19,19,19,19,19,57,19,57,19,2185",

"PAUSE":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,169,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,19,19,57,19,57,19,19,19,22,19,57,19,19,19,57,19,57,19,19,19,19,19,57,19,57,19,2185",

"PLAY":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,19,19,57,19,19,19,19,19,22,19,57,19,57,19,19,19,57,19,19,19,57,19,57,19,57,19,2185",

"POWER_TOGGLE":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,22,19,57,19,57,19,57,19,57,19,57,19,57,19,57,19,57,19,2185",

"PREVIOUS":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,19,19,57,19,57,19,19,19,19,19,19,19,22,19,19,19,57,19,19,19,19,19,57,19,57,19,57,19,57,19,2185",

"REPEAT":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,22,19,19,19,19,19,19,19,57,19,57,19,19,19,57,19,57,19,2185",

"RETURN":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,57,19,19,19,57,19,19,19,19,19,22,19,19,19,19,19,19,19,57,19,19,19,57,19,57,19,57,19,2185",

"REVERSE":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,19,19,57,19,19,19,19,19,22,19,57,19,19,19,57,19,57,19,19,19,57,19,57,19,57,19,2185",

"SEARCH":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,57,19,19,19,19,19,19,19,22,19,57,19,57,19,19,19,19,19,57,19,57,19,57,19,57,19,2185",

"SMART_HUB":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,19,19,19,19,57,19,57,19,57,19,19,19,22,19,57,19,57,19,57,19,19,19,19,19,19,19,57,19,57,19,2185",

"STOP":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,57,19,57,19,19,19,19,19,57,19,19,19,19,19,22,19,19,19,19,19,57,19,57,19,19,19,57,19,57,19,57,19,2185",

"SUBTITLE":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,57,19,19,19,19,19,57,19,19,19,22,19,57,19,19,19,19,19,57,19,57,19,19,19,57,19,57,19,2185",

"TOOLS":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,57,19,57,19,57,19,19,19,22,19,57,19,19,19,57,19,19,19,19,19,19,19,57,19,57,19,2185",

"ZOOM":"171,171,19,19,19,19,19,19,19,19,19,19,19,57,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,171,19,57,19,57,19,57,19,19,19,19,19,57,19,19,19,57,19,19,19,57,19,19,19,22,19,57,19,19,19,57,19,19,19,57,19,19,19,57,19,57,19,2185"
}
	
	
	
