import time
import pyautogui

pyautogui.FAILSAFE = True

target_rgb = (75, 219, 106)



print("the trigger bot is on")
print("live tracker is on")

try:
    while True:
        x, y = pyautogui.position()
        print(f"x: {x:4d} | y: {y:4d}", end="\r")
        time.sleep(0.1)
        if pyautogui.pixelMatchesColor(x, y, target_rgb, tolerance=25):
            pyautogui.click()
            print(f"triggered at (x: {x}, y: {y})")

            time.sleep(0.5)

    time.sleep(0.05)
except KeyboardInterrupt:
    print("Program terminated by user.")