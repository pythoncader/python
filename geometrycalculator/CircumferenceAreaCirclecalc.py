pi = 3.1415926535897932384626433832795
print('Find the Circumference or Area of a Circle:')
print(" '1' = Circumference \n '2' = Area")
CircorArea = int(input())
if CircorArea == 1:
	#CircumferenceCalculation
	print("Write the radius here: ")
	radiuscirc = float(input())
	Circumference = radiuscirc * 2 * pi
	print("Here is Your Circle's Circumference: \n" +str(Circumference))
elif CircorArea == 2:
	print("Write the radius here: ")
	radiusarea = float(input())
	print("Here is Your Circle's Area:")
	print(radiusarea * radiusarea * pi)
else:
	print("Entry is not valid")
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