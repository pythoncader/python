try:
  print('running finding values...')
  import subprocess
  import sys
  import myfunctions

  myfunctions.clear()
  print("What would you like to calculate? \n '1' = distance formula \n '2' = pythagorean theorem\n ...")
  try:
    calculate = int(input())
  except Exception:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python3', 'distancebetweenpointsformula.py'])
  elif calculate == 2:
      subprocess.call(['python3', 'PythagoreanTheorem.py'])
except Exception:
  print("Something went wrong!")
except KeyboardInterrupt:
  myfunctions.clear()
  sys.exit("Quitting Geometry Calculator...")
#start calculator again on keypress Enter
myfunctions.runmainagain()