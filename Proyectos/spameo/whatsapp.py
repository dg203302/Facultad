import pyautogui
import time
time.sleep(5)
start_time=time.time()
duration=(5*60)
for i in range(0, 10000000):
    pyautogui.write('paga cagon')
    pyautogui.press('enter')
    time.sleep(1)
    if (time.time()-start_time)>duration:
        break