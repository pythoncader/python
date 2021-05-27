print("Find The Area Of A Triangle! (with side lengths)")
print("type the first side length here")
a = float(input())
print("type the second side length here")
b = float(input())
print("type the third side length here")
c = float(input())
sa = 0.5 * a
sb = 0.5 * b
sc = 0.5 * c
s = sa + sb + sc
xroot = s * (s-a)*(s-b)*(s-c)
import math
Area = math.sqrt(xroot)
print("And there is your answer!")
print(Area)
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