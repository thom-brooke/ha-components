'''IR Codes for Sony BluRay (remote RMT-VB310U)

These are derived from code set #6528 from the Global Cache IR code database ("Control Tower").
They seem to have been compiled from multiple sources, hence the slight variations in timing
from one code to another.
'''


CARRIER_FREQUENCY = 40000
REPEAT_OFFSET = 1
REPEAT_COUNT = 3

IR_CODES = {
    "AUDIO":"96,24,24,24,24,24,48,24,24,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "BLUETOOTH":"96,24,48,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,456",

    "CLEAR":"96,24,48,24,48,24,48,24,48,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "CURSOR_DOWN":"96,24,24,24,48,24,24,24,48,24,48,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "CURSOR_ENTER":"96,24,48,24,24,24,48,24,48,24,48,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,456",

    "CURSOR_LEFT":"96,24,48,24,48,24,24,24,48,24,48,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,456",

    "CURSOR_RIGHT":"96,24,24,24,24,24,48,24,48,24,48,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "CURSOR_UP":"96,24,48,24,24,24,24,24,48,24,48,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "DIGIT_0":"96,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,576",

    "DIGIT_1":"96,24,48,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,552",

    "DIGIT_2":"96,24,24,24,48,24,24,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,552",

    "DIGIT_3":"96,24,48,24,48,24,24,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,528",

    "DIGIT_4":"96,24,24,24,24,24,48,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,552",

    "DIGIT_5":"96,24,48,24,24,24,48,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,528",

    "DIGIT_6":"96,24,24,24,48,24,48,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,528",

    "DIGIT_7":"96,24,48,24,48,24,48,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "DIGIT_8":"96,24,24,24,24,24,24,24,48,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,552",

    "DIGIT_9":"96,24,48,24,24,24,24,24,48,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,528",

    "DISPLAY":"96,24,48,24,24,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,528",

    "FAVORITE":"96,24,24,24,48,24,48,24,48,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,456",

    "FORWARD":"96,24,24,24,24,24,48,24,48,24,48,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "FUNCTION_BLUE":"96,24,48,24,24,24,48,24,24,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "FUNCTION_GREEN":"96,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "FUNCTION_RED":"96,24,48,24,48,24,48,24,24,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,456",

    "FUNCTION_YELLOW":"96,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "MENU_HOME":"96,24,24,24,48,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,528",

    "MENU_POPUP":"96,24,48,24,24,24,24,24,48,24,24,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "MENU_TOP":"96,24,24,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "NET_SERVICES":"96,24,48,24,24,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "NETFLIX":"96,24,48,24,48,24,24,24,48,24,24,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "NEXT":"96,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "OPEN_CLOSE":"96,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "OPTIONS":"96,24,48,24,48,24,48,24,48,24,48,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,432",

    "PAUSE":"96,24,48,24,24,24,24,24,48,24,48,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "PLAY":"96,24,24,24,48,24,24,24,48,24,48,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "POWER_OFF":"96,24,48,24,48,24,48,24,48,24,24,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,456",

    "POWER_ON":"96,24,24,24,48,24,48,24,48,24,24,24,48,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "POWER_TOGGLE":"96,24,48,24,24,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "PREVIOUS":"96,24,48,24,48,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,456",

    "RETURN":"96,24,48,24,48,24,24,24,24,24,24,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "REVERSE":"96,24,48,24,48,24,24,24,48,24,48,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "SLOW_FORWARD":"96,24,24,24,24,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,504",

    "SLOW_REVERSE":"96,24,48,24,48,24,24,24,24,24,48,24,24,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480",

    "STOP":"96,24,24,24,24,24,24,24,48,24,48,24,24,24,24,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,528",

    "SUBTITLE":"96,24,48,24,48,24,24,24,24,24,24,24,48,24,48,24,24,24,48,24,24,24,48,24,48,24,24,24,48,24,24,24,24,24,24,24,48,24,48,24,48,480"
}
