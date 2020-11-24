import sys
import pyautogui
import time
import traceback


def console_main(sleep_time=30):
    try:
        print("I will keep your PC and monitor alive. :)\nPress Ctrl+C to exit.")
        while True:
            pyautogui.press('left')
            time.sleep(sleep_time)
            pyautogui.press('right')
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("Bye!")
    except Exception:
        traceback.print_exc(file=sys.stdout)


console_main(15)
