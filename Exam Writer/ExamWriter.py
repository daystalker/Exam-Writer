import pyautogui
import random
import time
m=input("Enter No. of Questions:")
a="src"
a+=r"\\"
for i in range(int(m)):
    b=random.choice("abcd")
    print(b)
    b+=r".png"
    c=a+b
    x,y=pyautogui.locateCenterOnScreen(c)
    pyautogui.moveTo(x-20,y)
    pyautogui.click()
    x,y=pyautogui.locateCenterOnScreen(r"src\N.png")
    pyautogui.moveTo(x,y)
    pyautogui.click()
    time.sleep(6)
    
