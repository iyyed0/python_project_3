import pyautogui,datetime,time
iteration_count=0
time.sleep(2)
while iteration_count<10: ### the loop will run for 10 iterations (changeable)
    print(datetime.datetime.now())
    pyautogui.typewrite("WAKE UP")
    pyautogui.press("enter")
    time.sleep(2)
    iteration_count+=1
