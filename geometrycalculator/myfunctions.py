def clear():
    try:
        import replit
        replit.clear()
        print("You are using replit")
    except:
        import os
        returnvalue = os.system("cls")
        print("You are using a Windows PC")
        if returnvalue != 0:
            os.system("clear")
            print("You are using OSX or Linux")

def runmainagain():
  import subprocess
  print('\n\nPress enter to calculate again')
  input("")
  subprocess.call(['python', 'main.py'])
  
def invalidinput():
  import subprocess
  clear()
  print('Input not valid.\n\nPress enter to calculate again')
  input("")
  subprocess.call(['python', 'main.py'])