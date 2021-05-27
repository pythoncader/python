try:
  print('running finding values...')
  import subprocess
  import myfunctions

  myfunctions.clear()
  print("What would you like to calculate? \n '1' = distance formula \n '2' = pythagorean theorem\n ...")
  try:
    calculate = int(input())
  except:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python', 'distancebetweenpointsformula.py'])
  elif calculate == 2:
      subprocess.call(['python', 'PythagoreanTheorem.py'])
except:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()