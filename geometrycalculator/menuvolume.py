try:
  print('running volume...')
  import subprocess
  import myfunctions

  myfunctions.clear()
  print("What would you like to calculate? \n '1' = rectangular prism volume\n ...")
  try:
    calculate = int(input())
  except Exception:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python3', 'RectangularPrismVolume.py'])
except Exception:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()