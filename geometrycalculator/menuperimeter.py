try:
  print('running perimeter...')
  import subprocess
  import myfunctions

  myfunctions.clear()
  print("What would you like to calculate? \n '1' = polygon perimeter (3 to 15 sides)\n '2' = circle circumference or area\n ...")
  try:
    calculate = int(input())
  except:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python', 'Perimetercalc.py'])
  elif calculate == 2:
      subprocess.call(['python', 'CircumferenceAreaCirclecalc.py'])
except:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()