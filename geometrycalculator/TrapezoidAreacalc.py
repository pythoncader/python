from myfunctions import clear
import subprocess
import time

print('Find the Area of a Trapezoid \nPlease Type the First Base Length Below:')
base1 = float(input())
print('Please Type the Second Base Length Below:')
base2 = float(input())
print('Please Type the Height Below:')
height = float(input())
bases = base1+base2
Area = 0.5 * height * bases
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