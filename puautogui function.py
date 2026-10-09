import pyautogui

def name():
    k=input('enter ur name')
    m= input("enter age")
    l= input('place')
    pyautogui.click(350, 400,  duration=0.8)
    pyautogui.write(k)
    pyautogui.press('return')
    pyautogui.write(m)
    pyautogui.press('return')
    pyautogui.write(l)

    #coping name
def copy_name():
    pyautogui.click(330, 400,  duration=0.8)
    pyautogui.hotkey('command' , 'c')
    #using right click
    # pyautogui.rightClick(330, 400 , duration=0.01)
    # pyautogui.click(400, 630,  duration=0.8)
    pyautogui.click(330,500 , duration=0.8)
    pyautogui.hotkey('command' , 'v')

  

name()














#.