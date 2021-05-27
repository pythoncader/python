try:
  import time
  import myfunctions
  import subprocess
  import myfunctions

  myfunctions.clear()
  print('Find the area of a rectangular prism!')
  print('Write the length here (in feet, decimals if not integer):')
  lfeet = float(input())
  lyards = lfeet/3
  print('Write the width here (in feet, decimals if not integer):')
  wfeet = float(input())
  wyards = wfeet/3
  print('Write the height here (in feet, decimals if not integer):')
  hfeet = float(input()) 
  hyards = hfeet/3
  print('Here is the volume of your rectangular prism!')
  volume=lyards*wyards*hyards
  print(str(volume)+' cubic yard(s)')
  print(str(lfeet*wfeet*hfeet)+' cubic feet')
  #start calculator again on keypress Enter	
  myfunctions.runmainagain()
except:
  print("Something went wrong!")
#start calculator again on keypress Enter
myfunctions.runmainagain()