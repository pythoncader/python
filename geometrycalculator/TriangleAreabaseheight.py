import subprocess
import time
from myfunctions import clear

print("Find The Area Of A Triangle! (with base and height)")
print("Make sure to type the base length first, then the height\n")
print("type the base length here")
b = float(input())
print("type the height here")
h = float(input())
Area = (1 / 2 * b * h)
print("And there is your answer!")
print(Area)
#start calculator again on keypress Enter	
print("\n \nPress Enter to Clear and Calculate Again")
input("")

clear()

a = 1

while a < 1:
    a += 1
    time.sleep(1)
    clear()

subprocess.call(['python', 'main.py'])