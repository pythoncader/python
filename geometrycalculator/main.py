from myfunctions import clear
import subprocess
clear()
	
print("What would you like to calculate? \nType your choice in the box below: \n\n'1' = volume \n\n'2' = area \n\n'3' = perimeter \n\n'4' = finding values \n")
try:
	calculate = int(input())
except:
	print('Input not valid\nPress enter to calculate again')
	input("")
	subprocess.call(['python', 'main.py'])

if calculate == 1:
    subprocess.call(['python', 'menuvolume.py'])
elif calculate == 2:
    subprocess.call(['python', 'menuarea.py'])
elif calculate == 3:
		subprocess.call(['python', 'menuperimeter.py'])
elif calculate == 4:
		subprocess.call(['python', 'menufindingvalues.py'])
else:
	print('Input not valid\nPress enter to calculate again')
	input("")
	subprocess.call(['python', 'main.py'])