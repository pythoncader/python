from myfunctions import clear
print('running finding values...')
clear()
print("What would you like to calculate? \n '1' = distance formula \n '2' = pythagorean theorem...")
calculate = int(input())

import subprocess
if calculate == 1:
		subprocess.call(['python', 'distancebetweenpointsformula.py'])
elif calculate == 2:
		subprocess.call(['python', 'PythagoreanTheorem.py'])