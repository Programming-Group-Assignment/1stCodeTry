from graphics import*
count = 0 #Survival count needs to be implemented in all definitions
inventory = ""
#All Story related texts have to be in seperate def function() 
#This in order to not repeat unwanted text and only repeat 'count and questions + if-solutions'
#'count and questions + if-solutions' have to be able to get called seperately ('in def function()')
#Calling needs to be more precise depending on importance of function
def IntroductionText():
    print("txt")

def Firstscene():
    userInput1 = input("What do you do?"):
                       #graphics
    if userInput1 == "Walk out of room": #Solution Path!
        WalkoutRoom()
    elif userInput1 == "Stay in room": #Will return to Walkoutroom()
        StayinRoom()
def StayinRoom():
    userInput0 = input("What to do?") #Go back to the Firstscene()
        WalkoutRoom()
    return userInput1

def TextPart1(): #Here there will be the text of the story 
    print("txt")
    
def WalkoutRoom():
    userInput2 = input("txt")
    if userInput2 =="fight":
        FightZombie()
    elif userInput2 == "run":
        RunAwayZombie()
    elif userInput == "lock the door"
        WalkoutRoom() #has to include text so maybe make seperate TextPart function = 1 more step
    return userInput2

def FightZombie(): #graphics with objects
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
                RunAwayZombie() #going back to 
            return userInput5
    elif userInput3 == "Wheelchair": #put to inventory
        print("txt")
        WalkoutRoom()
        return userInput3 
    elif userInput3 == "Gun": #put to inventory
        print("Tricky ToyGun is no thelping")
        WalkoutRoom()
    return userInput3
   

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
         elif Inventory != "Crutches": #if inventory does not contain 'crutches' return to runawayzombie() to pick left
            print("txt") 
            RunAwayZombie()
    elif userInput4 == "Left":# 2 chances continue running or hide in room
         print("txt")
         ShowCorridor()
          
                
def ShowCorridor():               
         userInput7 = input("Show corridor") #choose graphical corridor or room
         if userInput7 == "Continue running": #solutions path
                print("txt") #graphics for reception area
                ContinueRunning()
                
        elif userInput7 =="Hide in Room": #you are locked in with zombies and need to return to Left- Show_Corridor graphics
                print("txt")
                ShowCorridor()
                
                
def ContinueRunning(): #solutions path
      userInput8 = input(#receptionchoice)#graphical reception or text with items to pick up
          if userInput8 == "Look"
                print("txt")
                userInput9 = input(#yesorno) #look for items in reception desk
                    if userInput9 == "Yes"
                        print("txt")
                        if Inventory == "Crutches":
                            userInput10 = input(#HideorRunorCrutches)
                            if userInput10 == "Crutches"
                                print("txt")
                                #map riddle
                                userinput11 = input(#leftdoororrightdoor)
                                    if userinput11 == "Left"
                                        print("txt")
                                    elif useinput11 == "Right"
                                        print("txt")
                                        return to userinput11                            
                            elif userInput10 == "Hide"
                                print("txt")
                                HideBehindDesk()
                            elif userInput10 == "Run"
                                print("txt")
                                #map riddle 
                                userinput12 = input(#leftdoororrightdoor)
                                    if userinput12 == "Left"
                                        print("txt")
                                    elif useinput12 == "Right"
                                        print("txt")
                                        return to userinput12
                        elif Inventory != "Ctrutches":
                            userInput10 = input(#HideorRun)
                            if userInput10 == "Hide"
                                print("txt")
                                HideBehindDesk()
                            elif userInput10 == "Run"
                                print("txt")
                    elif userInput9 == "No"
          elif userInput8 == "Hide"                                 


def main():
main()
