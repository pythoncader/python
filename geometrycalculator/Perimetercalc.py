def calc():
  try:
    import time
    import myfunctions
    import sys
    import myfunctions

    myfunctions.clear()
    print('Find the perimeter of a polygon with 3 to 15 sides!')
    print('\nWrite the number of sides here: (3 - 15 sides)')
    try:
      ns = int(input())
    except Exception:
      myfunctions.invalidinput()
      return
      
    if ns == 3:
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3)
    elif ns == 4:
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4)
    elif ns == 5:	
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5)
    elif ns == 6:
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print(s1 + s2 + s3 + s4 + s5 + s6)
    elif ns == 7:	
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7)
    elif ns == 8:
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8)
    elif ns == 9:	
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nPlease write the next side length here:') 
      s9 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9)
    elif ns == 10:
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nPlease write the next side length here:') 
      s9 = float(input())
      print('\nPlease write the next side length here:') 
      s10 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10)
    elif ns == 11:	
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nPlease write the next side length here:') 
      s9 = float(input())
      print('\nPlease write the next side length here:') 
      s10 = float(input())
      print('\nPlease write the next side length here:') 
      s11 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11)
    elif ns == 12:
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nPlease write the next side length here:') 
      s9 = float(input())
      print('\nPlease write the next side length here:') 
      s10 = float(input())
      print('\nPlease write the next side length here:') 
      s11 = float(input())
      print('\nPlease write the next side length here:') 
      s12 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12)
    elif ns == 13:	
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nPlease write the next side length here:') 
      s9 = float(input())
      print('\nPlease write the next side length here:') 
      s10 = float(input())
      print('\nPlease write the next side length here:') 
      s11 = float(input())
      print('\nPlease write the next side length here:') 
      s12 = float(input())
      print('\nPlease write the next side length here:') 
      s13 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13)
    elif ns == 14:
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nPlease write the next side length here:') 
      s9 = float(input())
      print('\nPlease write the next side length here:') 
      s10 = float(input())
      print('\nPlease write the next side length here:') 
      s11 = float(input())
      print('\nPlease write the next side length here:') 
      s12 = float(input())
      print('\nPlease write the next side length here:') 
      s13 = float(input())
      print('\nPlease write the next side length here:') 
      s14 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14)
    elif ns == 15:	
      print('\nPlease write the first side length here:')
      s1 = float(input())
      print('\nPlease write the next side length here:') 
      s2 = float(input())
      print('\nPlease write the next side length here:') 
      s3 = float(input())
      print('\nPlease write the next side length here:') 
      s4 = float(input())
      print('\nPlease write the next side length here:') 
      s5 = float(input())
      print('\nPlease write the next side length here:') 
      s6 = float(input())
      print('\nPlease write the next side length here:') 
      s7 = float(input())
      print('\nPlease write the next side length here:') 
      s8 = float(input())
      print('\nPlease write the next side length here:') 
      s9 = float(input())
      print('\nPlease write the next side length here:') 
      s10 = float(input())
      print('\nPlease write the next side length here:') 
      s11 = float(input())
      print('\nPlease write the next side length here:') 
      s12 = float(input())
      print('\nPlease write the next side length here:') 
      s13 = float(input())
      print('\nPlease write the next side length here:') 
      s14 = float(input())
      print('\nPlease write the next side length here:') 
      s15 = float(input())
      print('\nHere is your answer:')
      print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15)
    else:
      print('\nEntry is not valid')
  except Exception:
    print("Something went wrong!")
  except KeyboardInterrupt:
    myfunctions.clear()
    sys.exit("Quitting Geometry Calculator...")
  #start calculator again on keypress Enter
  myfunctions.runmainagain()
  return
  
if __name__ == "__main__":
  calc()