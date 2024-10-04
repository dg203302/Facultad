import pyautogui
import time
time.sleep(5)
i=0
while True:
    pyautogui.write('.')
    pyautogui.press('enter')
    if i==10000:
        break
    i+=1