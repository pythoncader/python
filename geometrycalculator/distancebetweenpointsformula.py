import math
print('Find the distance between two points on the coordinate plane\n')
print("Please write your first point's x-value here: (as an integer or decimal)")
x1 = float(input())
print("Please write your first point's y-value here: (as an integer or decimal)")
y1 = float(input())
print("Please write your second point's x-value here: (as an integer or decimal)")
x2 = float(input())
print("Please write your second point's y-value here: (as an integer or decimal)")
y2= float(input())
x2minusx1	= x2 - x1
x2minusx1squared = x2minusx1 * x2minusx1
y2minusy1 = y2 - y1
y2minusy1squared = y2minusy1 * y2minusy1
inside = x2minusx1squared + y2minusy1squared
distance = math.sqrt(inside)
print('\nHere is the distance between the points:\n'+str(distance))
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