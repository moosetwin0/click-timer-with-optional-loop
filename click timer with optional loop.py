from time import sleep
from mouse import click

menu1 = ["left", "right", "middle"]
menu2 = ["y", "yes", "n", "no"]

def invalid(message):
    print()
    print(message)
    sleep(2)
    print()

while True: 
    while True:
        print("Which mouse button would you like to click?")
        print("For left click, enter '1'.")
        print("For right click, enter '2'.")
        print("For middle click, enter '3'.")
        clickbutton = input("1, 2, or 3: ")
        if clickbutton.isdigit() and 0 < int(clickbutton) < 4:
            clickbutton = menu1[int(clickbutton) - 1]
            print()
            break
        else: invalid("Your mouse button choice must be 1, 2, or 3.")

    while True:
        print("Would you like it to loop?")
        print("Enter 'Y' for yes, 'N' for no.")
        loopchoice = (input("Y/N: ")).lower()
        if loopchoice in menu2:
            if menu2.index(loopchoice) < 2:
                loopchoice = True
            else: loopchoice = False
            print()
            break
        else: invalid("Your loop choice must be either 'Y' or 'N'.")

    while True:
        print("How long would you like to wait before clicking? (in seconds)")
        time = input("Seconds before click: ")
        if time.replace('.','',1).isdigit():
            time = float(time)
            print()
            break
        else: invalid("Your click time choice must be a number.")

    while True:
        print("It will click the " + clickbutton + " mouse button.")
        if loopchoice: print("It will loop.")
        else: print("It will not loop.")
        print("It will wait " + str(time) + " seconds before clicking.")
        
        print("Would you like to re-enter this information before starting?")
        print("Enter 'Y' for yes, 'N' for no.")
        reenter = (input("Y/N: ")).lower()
        if reenter not in menu2:
            invalid("Your choice must be either 'Y' or 'N'.")
        else: break
    if menu2.index(reenter) > 1: 
        print()
        break

print("Starting timer.")
while True:
    sleep(time)
    click(clickbutton)
    if not loopchoice: break