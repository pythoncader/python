print('running other...')
import replit
replit.clear()
print("What would you like to calculate? \n '1' = Sample \n...")
calculate = int(input())

import subprocess
if calculate == 1:
		subprocess.call(['python', 'Samplefilename.py'])