try:
  import myfunctions
  import subprocess
  import sys
  import time
  import myfunctions

  myfunctions.clear()
  print('Find the Area of a Trapezoid \n\nPlease Type the First Base Length Below:')
  base1 = float(input())
  print('\nPlease Type the Second Base Length Below:')
  base2 = float(input())
  print('\nPlease Type the Height Below:')
  height = float(input())
  bases = base1+base2
  Area = 0.5 * height * bases
  print(f"\nHere is the area of your trapezoid: {Area}")
  #start calculator again on keypress Enter	
  myfunctions.runmainagain()
except Exception:
  print("Something went wrong!")
except KeyboardInterrupt:
  sys.exit("Quitting Geometry Calculator...")
#start calculator again on keypress Enter
myfunctions.runmainagain()