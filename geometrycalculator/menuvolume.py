from myfunctions import clear
print('running volume...')
clear()
print("What would you like to calculate? \n '1' = rectangular prism volume\n '2' = triangle area (with base and height)\n '3' = triangle area (with side lengths)\n '4' = polygon perimeter (up to 15 sides)\n '5' = circle circumference or area\n ...")
calculate = int(input())

import subprocess
if calculate == 1:
		subprocess.call(['python', 'RectangularPrismVolume.py'])
elif calculate == 2:
		subprocess.call(['python', 'TriangleAreabaseheight.py'])
elif calculate == 3:
		subprocess.call(['python', 'TriangleAreasidelengths.py'])
elif calculate == 4:
		subprocess.call(['python', 'Perimetercalc.py'])
elif calculate == 5:
		subprocess.call(['python', 'CircumferenceAreaCirclecalc.py'])