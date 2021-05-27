from myfunctions import clear
print('running perimeter...')
clear()
print("What would you like to calculate? \n '1' = polygon perimeter (3 to 15 sides)\n '2' = circle circumference or area\n ...")
calculate = int(input())

import subprocess
if calculate == 1:
		subprocess.call(['python', 'Perimetercalc.py'])
elif calculate == 2:
		subprocess.call(['python', 'CircumferenceAreaCirclecalc.py'])