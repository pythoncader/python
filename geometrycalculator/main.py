import os
try: 
	os.system("cls")
except:
	os.system("clear")
print("What would you like to calculate? \nType your choice in the box below: \n\nvolume \n\narea \n\nperimeter \n\nfinding values \n\nother\n")
calculate = str(input(""))
import subprocess
if calculate == "volume":
    subprocess.call(['python', 'menuvolume.py'])
elif calculate == "area":
    subprocess.call(['python', 'menuarea.py'])
elif calculate == "perimeter":
		subprocess.call(['python', 'menuperimeter.py'])
elif calculate == "finding values":
		subprocess.call(['python', 'menufindingvalues.py'])
elif calculate == "other":
		subprocess.call(['python', 'menuother.py'])
else:
	print('Input not valid\nPress enter to calculate again')
	input("")
	subprocess.call(['python', 'main.py'])