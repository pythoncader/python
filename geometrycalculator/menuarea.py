print('running area...')
import replit
replit.clear()
print("What would you like to calculate? \n '1' = triangle area (with base and height)\n '2' = triangle area (with side lengths)\n '3' = circle circumference or area\n '4' = trapezoid area\n ...")
calculate = int(input())

import subprocess
if calculate == 1:
		subprocess.call(['python', 'TriangleAreabaseheight.py'])
elif calculate == 2:
		subprocess.call(['python', 'TriangleAreasidelengths.py'])
elif calculate == 3:
		subprocess.call(['python', 'CircumferenceAreaCirclecalc.py'])
elif calculate == 5:
		subprocess.call(['python', 'TrapezoidAreacalc.py'])
