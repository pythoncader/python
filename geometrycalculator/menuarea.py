try:
  print("running area...")
  import subprocess
  import myfunctions

  myfunctions.clear()
  print("What would you like to calculate? \n '1' = triangle area (with base and height)\n '2' = triangle area (with side lengths)\n '3' = circle circumference or area\n '4' = trapezoid area\n ...")
  try:
    calculate = int(input())
  except Exception:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python3', 'TriangleAreabaseheight.py'])
  elif calculate == 2:
      subprocess.call(['python3', 'TriangleAreasidelengths.py'])
  elif calculate == 3:
      subprocess.call(['python3', 'CircumferenceAreaCirclecalc.py'])
  elif calculate == 4:
      subprocess.call(['python3', 'TrapezoidAreacalc.py'])
except Exception:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()