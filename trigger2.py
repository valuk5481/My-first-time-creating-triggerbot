import time
import pyautogui


pyautogui.FAILSAFE = True

target_rgb = (75, 219, 106)

print("the trigger bot is active")
print("Press Ctrl+C to stop the trigger bot")

try:
    while True:
        x, y = pyautogui.position()
     
    

        if pyautogui.pixelMatchesColor(x, y, target_rgb, tolerance=25):
          print("aim activated")
          pyautogui.click()
         
          time.sleep(0.5)
          

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Program terminated by user.")      