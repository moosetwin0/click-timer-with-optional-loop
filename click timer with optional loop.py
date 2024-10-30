from time import sleep
from mouse import click
from win32api import GetKeyState

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

# -127 = button actively being pressed, 1 = numlock on
# 0x90 is the code for numlock
# todo: "starting timer in 5 seconds" so it's not immediate
print("The timer will activate in a moment. To pause the timer, press NumLock.")
print()
sleep(3)
if GetKeyState(0x90) in (-127, 1):
    print("Warning! Numlock is activated, timer will not start until numlock is disengaged.")
while GetKeyState(0x90) in (-127, 1):
    sleep(0.5)

# I deserve to be publicly shamed for writing this code:
# I thought I was being clever with the while loops until I wanted to add more stuff
# which broke everything
# and after bugfixes the code eventually turned into this
# I shoulda just started over man
breakvarB = False
# I am 80% sure this timecounter stuff is unneeded overengineering but that's hindsight for ya
# (It's unneeded because I probably coulda just slept the timer before checking, 
# I initially made this due to a bug that ended up being fixed anyways)
timecounter = 0
while time >= 0.5:
    time -= 0.5
    timecounter += 1
while breakvarB != True:
    if GetKeyState(0x90) not in (-127, 1):
        fivetimer = 5
        while fivetimer:
            print("Starting timer in " + str(fivetimer) + " seconds.")
            sleep(1)
            fivetimer -= 1
        breakvarA = False
    while GetKeyState(0x90) not in (-127, 1):
        # see above timecounter comment
        timecounterB = timecounter
        while timecounterB:
            sleep(0.5)
            if GetKeyState(0x90) in (-127, 1):
                breakvarA = True
                break
            timecounterB -= 1
        sleep(time)
        if breakvarA == True: 
            print("Pausing timer.")
            break
        click(clickbutton)
        if not loopchoice: 
            breakvarB = True
            break
