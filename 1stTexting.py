
count = 0

def Introduction():
    print("txt")

def Firstscene():
    userInput1 = input("What do you do?")
    #graphics*
    if userInput1 == "Walk out of room":
        WalkoutRoom(1stPath)
    elif userInput1 == "Stay in room":
        StayinRoom(2ndPath)
def WalkoutRoom(1stPath):
    userInput2 = input("txt")
    if userInput2 =="fight":
        FightZombie()
    elif userInput2 == "run":
        RunAway()
    elif userInput == "lock the door"
        LockDoor()
def FightZombie():
    #graphics with objects
    userInput3 = input(#selectobjects/window)
    if userInput3 == "Crutches": #put to inventory
        print("Hit with crutches does not have an effect")
        return WalkoutRoom() #return to be able to run away
    #survival count += 1
    elif userInput3 == "Wheelchair": #put to inventory
        print("Wheelchair is not effective + heavy inventory")
        return WalkoutRoom() #return to be able to run away
    #survival count
    elif userInput3 == "Gun": #put to inventory
        print("Tricky ToyGun is no thelping")
        return WalkoutRoom()
    #survival count
def RunAwayZombie():
    userInput4 = input("wkhbv")
    if userInput4 == "Right":
        if Inventory with Crutches:
            print("you can defend yourself ")#here no count
            return WalkoutRoom()
        if Inventory without Crutches:
            print("infected") #here count +1
            return WalkoutRoom()
    elif userInput4 == "Left": # 2 chances continue running or hide in room
        userInput5 = input("Show corridor")
        if userInput5 == "Continue running":

        elif userInput5 =="Hide in Room":

def LockDoorZombie():
    print("txt")
    probably return to WalkoutRoom()


def StayinRoom(2ndPath):


def main():
main()