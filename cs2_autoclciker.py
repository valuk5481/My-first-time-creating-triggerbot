import mouse
import pyautogui
import pydirectinput
import time
import keyboard
from mss import mss

center_x = 540
center_y = 540

target_blue = (49, 43, 45)

print("the game trigger bot is ready at")

with mss() as sct:
    monitor = {"top": center_y, "left": center_x, "width": 1, "height": 1}

    while True:
        if keyboard.is_pressed("alt"):
            img = sct.grab(monitor)

            current_color = (img.pixel(0, 0)[1], img.pixel(0, 0)[0])

            if all(abs(a - b) <= 20 for a, b in zip(current_color, target_blue)):
                pydirectinput.click()
                time.sleep(0.12)

            time.sleep(0.001)
        else:
            time.sleep(0.02)        