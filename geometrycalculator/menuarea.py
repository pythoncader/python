try:
  print("running area...")
  import subprocess
  import myfunctions

  myfunctions.clear()
  print("What would you like to calculate? \n '1' = triangle area (with base and height)\n '2' = triangle area (with side lengths)\n '3' = circle circumference or area\n '4' = trapezoid area\n ...")
  try:
    calculate = int(input())
  except:
    myfunctions.invalidinput()

  if calculate == 1:
      subprocess.call(['python', 'TriangleAreabaseheight.py'])
  elif calculate == 2:
      subprocess.call(['python', 'TriangleAreasidelengths.py'])
  elif calculate == 3:
      subprocess.call(['python', 'CircumferenceAreaCirclecalc.py'])
  elif calculate == 4:
      subprocess.call(['python', 'TrapezoidAreacalc.py'])
except:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()