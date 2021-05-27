import subprocess
from myfunctions import clear

clear()
pi = 3.1415926535897932384626433832795
print('Find the Circumference or Area of a Circle:')
print(" '1' = Circumference \n '2' = Area")
CircorArea = int(input())
if CircorArea == 1:
	clear()
	#CircumferenceCalculation
	print("Find the circumference of a circle\n")
	print("Write the radius here: ")
	radiuscirc = float(input())
	Circumference = radiuscirc * 2 * pi
	print("\nHere is Your Circle's Circumference: \n" +str(Circumference))
elif CircorArea == 2:
	clear()
	print("Find the area of a circle\n")
	print("Write the radius here: ")
	radiusarea = float(input())
	print("\nHere is Your Circle's Area:")
	print(radiusarea * radiusarea * pi)
else:
	print("Entry is not valid")
#start calculator again on keypress Enter	
print("\n \nPress Enter to Clear and Calculate Again")
input("")

subprocess.call(['python', 'main.py'])