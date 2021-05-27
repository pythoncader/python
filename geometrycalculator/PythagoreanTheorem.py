print('Find missing side lengths of triangles using the Pythagorean Theorem')
print("What would you like to calculate? \n '1' = missing side length\n '2' = verification of whether a triangle is a right triangle or not\n ...")
calculate = input()
if calculate == "1":
		print('Find the missing side length of a triangle: c = hypotenuse, b = leg, a = other leg. \nSimply put the missing side length in as 0 (zero)')
elif calculate == "2":
		print('Find out if a triangle is a right triangle or not based on the side lengths:\nc = hypotenuse or longest side, b = leg or any other side, a = other leg\nPlease type the length of side c below: (as an integer or decimal)')
		sidec = float(input())
		print('Please type the length of side b below:')
		sideb = float(input())
		print('Please type the length of side a below:')
		sidea = float(input())
		asqrd = sidea * sidea
		bsqrd = sideb * sideb
		csqrd = sidec * sidec
		aplsbsqrd = asqrd + bsqrd
		import math
		roundedaplsbsqrd = math.ceil(aplsbsqrd)
		if aplsbsqrd == csqrd:
			print('Your triangle, with side lengths a = '+str(sidea)+" b = "+str(sideb)+" and c = "+str(sidec)+" is a right triangle")
			input("")
		elif roundedaplsbsqrd == csqrd:
			print('It is a right triangle, but it is close:\n\nc squared is equal to: '+str(csqrd)+ " b squared plus a squared is equal to: "+str(aplsbsqrd))
			input("")
		else:
			print('Nope, this triangle is not a right triangle')
			input("")
else:
		print('Input not valid')
		input("")
#start calculator again on keypress Enter	
print("\n \nPress 1 and Enter to Clear and Restart the Calculator\nPress 2 and Enter to Calculate Finding Values again,")
clearorcalculate = input("")
if clearorcalculate == "1":
	import subprocess
	subprocess.call(['python', 'main.py'])
elif clearorcalculate == "2":
		import subprocess
		subprocess.call(['python', 'menufindingvalues.py'])