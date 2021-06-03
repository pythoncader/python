try:
  import time
  import subprocess
  import myfunctions

  myfunctions.clear()
  print("Find The Area Of A Triangle! (with side lengths)")
  print("\nType the first side length here:")
  a = float(input())
  print("\nType the second side length here:")
  b = float(input())
  print("\nType the third side length here:")
  c = float(input())
  sa = 0.5 * a
  sb = 0.5 * b
  sc = 0.5 * c
  s = sa + sb + sc
  xroot = s * (s-a)*(s-b)*(s-c)
  import math
  Area = math.sqrt(xroot)
  print("\nAnd there is your answer!")
  print(Area)
  #start calculator again on keypress Enter	
  myfunctions.runmainagain()
except Exception:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()