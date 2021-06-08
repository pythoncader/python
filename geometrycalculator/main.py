try:
  import myfunctions
  import subprocess
  import sys
  myfunctions.clear()
    
  print("What would you like to calculate? \n '1' = volume \n '2' = area \n '3' = perimeter \n '4' = finding values \n ...")
  try:
    calculate = int(input())
  except Exception:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python3', 'menuvolume.py'])
  elif calculate == 2:
      subprocess.call(['python3', 'menuarea.py'])
  elif calculate == 3:
      subprocess.call(['python3', 'menuperimeter.py'])
  elif calculate == 4:
      subprocess.call(['python3', 'menufindingvalues.py'])
  else:
      myfunctions.invalidinput()
except Exception:
  print("Something went wrong!")
except KeyboardInterrupt:
  sys.exit("Quitting Geometry Calculator...")
#start calculator again on keypress Enter
myfunctions.runmainagain()