import pyautogui,datetime,time
n1=int(input('Enter the number of minutes:'))
n2=int(input("Enter the number of seconds: "))
n=n1*60 + n2
time.sleep(n)
x=str(datetime.datetime.now())
x1=x[14:19]
pyautogui.alert(f'its {x1},time is up')