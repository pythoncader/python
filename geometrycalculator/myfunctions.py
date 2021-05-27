def clear():
    try:
        import replit
        replit.clear()
    except:
        import os
        returnvalue = os.system("cls")
        if returnvalue != 0:
            os.system("clear")