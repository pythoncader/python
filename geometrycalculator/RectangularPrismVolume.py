print('Find the area of a rectangular prism!')
print('Write the length here (in feet, decimals if not integer):')
lfeet = float(input())
lyards = lfeet/3
print('Write the width here (in feet, decimals if not integer):')
wfeet = float(input())
wyards = wfeet/3
print('Write the height here (in feet, decimals if not integer):')
hfeet = float(input()) 
hyards = hfeet/3
print('Here is the volume of your rectangular prism!')
volume=lyards*wyards*hyards
print(str(volume)+' cubic yard(s)')
print(str(lfeet*wfeet*hfeet)+' cubic feet')
#start calculator again on keypress Enter	
print("\n \nPress Enter to Clear and Calculate Again")
input("")
import replit
import time
replit.clear()

a = 1

while a < 1:
    a += 1
    time.sleep(1)
    replit.clear()
import subprocess
subprocess.call(['python', 'main.py'])