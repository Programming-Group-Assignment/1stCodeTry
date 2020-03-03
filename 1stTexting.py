
count = 0
inventory = ""

def Introduction():
    print("txt")

def Firstscene():
    userInput1 = input("What do you do?")
    #graphics*
    if userInput1 == "Walk out of room":
        WalkoutRoom(1stPath)
    elif userInput1 == "Stay in room":
        StayinRoom(2ndPath)
    return userInput1

def WalkoutRoom(1stPath):
    userInput2 = input("txt")
    if userInput2 =="fight":
        FightZombie()
    elif userInput2 == "run":
        RunAway()
    elif userInput == "lock the door"
        LockDoor()
    return userInput2

def FightZombie():
    #graphics with objects
    userInput3 = input(#selectobjects/window)
    if userInput3 == "Crutches": #put to inventory
        print("txt")
        userInput5 = input(#selecthowtousecrutches)
            if userInput5 == "Hit"
                print("txt")
                RunAwayZombie()
            return userInput5
            elif userInput5 == "Use"
                print("txt")
                RunAwayZombie()
            return userInput5
    elif userInput3 == "Wheelchair": #put to inventory
        print("txt")
        FightZombie()
        return userInput3 
    elif userInput3 == "Gun": #put to inventory
        print("Tricky ToyGun is no thelping")
        WalkoutRoom()
    #survival count

def RunAwayZombie():
    userInput4 = input("txt")
    if userInput4 == "Right":
        if Inventory == "Crutches":
            print("you can defend yourself with your crutches")#here no count
            print("txt")
            userInput6 = input(#selecthowtousecrutches)
            if userInput6 == "Hit"
                print("txt")
                return userInput6
            elif userInput6 == "Use"
                print("txt")
                return userInput6        
         elif Inventory != "Crutches":
            print("txt") 
            RunAwayZombie()
    elif userInput7 == "Left":# 2 chances continue running or hide in room
         print("txt")
         userInput7 = input("Show corridor")
         if userInput7 == "Continue running":
                print("txt")
                #graphics for reception area
                userInput8 = input(#receptionchoice)
                    if userInput8 == "Look"
                        print("txt")
                        userInput9 = input(#yesorno)
                            if userInput9 == "Yes"
                                print("txt")
                                if Inventory == "Crutches":
                                   userInput10 = input(#HideorRunorCrutches)
                                    if userInput10 = "Hide"
                                    elif userInput10 = "Run"
                            elif userInput9 == "No"
                    elif userInput8 == "Hide"

        elif userInput7 =="Hide in Room":
                print("txt")
                

def LockDoorZombie():
    print("txt")
    WalkoutRoom()


def StayinRoom(2ndPath):


def main():
main()
