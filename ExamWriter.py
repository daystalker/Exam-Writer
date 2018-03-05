import pyautogui
import random
import time
a="a.png"
b="b.png"
c="c.png"
d="d.png"
for i in range(20):
    n=random.randint(1,4)
    print(n)
    if(n==1):
        x,y=pyautogui.locateCenterOnScreen(a)
        pyautogui.moveTo(x-20,y)
        pyautogui.click()
    elif(n==2):
        x,y=pyautogui.locateCenterOnScreen(b)
        pyautogui.moveTo(x-20,y)
        pyautogui.click()
    elif(n==3):
        x,y=pyautogui.locateCenterOnScreen(c)
        pyautogui.moveTo(x-20,y)
        pyautogui.click()
    else:
        x,y=pyautogui.locateCenterOnScreen(d)
        pyautogui.moveTo(x-20,y)
        pyautogui.click()
    x,y=pyautogui.locateCenterOnScreen("N.png")
    pyautogui.moveTo(x,y)
    pyautogui.click()
    time.sleep(10)

