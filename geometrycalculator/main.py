try:
  import myfunctions
  import subprocess
  myfunctions.clear()
    
  print("What would you like to calculate? \n '1' = volume \n '2' = area \n '3' = perimeter \n '4' = finding values \n ...")
  try:
    calculate = int(input())
  except:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python', 'menuvolume.py'])
  elif calculate == 2:
      subprocess.call(['python', 'menuarea.py'])
  elif calculate == 3:
      subprocess.call(['python', 'menuperimeter.py'])
  elif calculate == 4:
      subprocess.call(['python', 'menufindingvalues.py'])
  else:
      myfunctions.invalidinput()
except:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()