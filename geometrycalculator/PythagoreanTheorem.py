import math
import subprocess
from myfunctions import clear

clear()
print('Find missing side lengths of triangles using the Pythagorean Theorem')
print("What would you like to calculate? \n '1' = missing side length\n '2' = verification of whether a triangle is a right triangle or not\n ...")
calculate = input()
if calculate == "1":
	clear()
	print('Find the missing side length of a triangle: c = hypotenuse, b = leg, a = other leg. \nSimply put the missing side length in as 0 (zero)')
elif calculate == "2":
	clear()
	print('Find out if a triangle is a right triangle or not based on the side lengths:\nc = hypotenuse or longest side, b = leg or any other side, a = other leg\n\nPlease type the length of side c below: (as an integer or decimal)')
	sidec = float(input())
	print('\nPlease type the length of side b below:')
	sideb = float(input())
	print('\nPlease type the length of side a below:')
	sidea = float(input())
	asqrd = sidea * sidea
	bsqrd = sideb * sideb
	csqrd = sidec * sidec
	aplsbsqrd = asqrd + bsqrd
	roundedaplsbsqrd = math.ceil(aplsbsqrd)
	if aplsbsqrd == csqrd:
		print('\nYour triangle, with side lengths a = '+str(sidea)+" b = "+str(sideb)+" and c = "+str(sidec)+" is a right triangle")
	elif roundedaplsbsqrd == csqrd:
		print('\nIt is a right triangle, but it is close:\n\nc squared is equal to: '+str(csqrd)+ ", and b squared plus a squared is equal to: "+str(aplsbsqrd))
	else:
		print('\nNope, this triangle is not a right triangle: \n\n c squared is equal to: '+str(csqrd)+ ', and b squared plus a squared is equal to: '+str(aplsbsqrd))
else:
		print('Input not valid')
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