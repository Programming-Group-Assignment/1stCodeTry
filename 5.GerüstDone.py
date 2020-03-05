count = 0      # Survival count needs to be implemented in all definitions
inventory = []
# All Story related texts have to be in seperate def function()
# This in order to not repeat unwanted text and only repeat 'count and questions + if-solutions'
# 'count and questions + if-solutions' have to be able to get called seperately ('in def function()')
# Calling needs to be more precise depending on importance of function
#Parameter/arguments = within () to call in seperate function
#There will be survival count, based on the amount of steps you take to complete
#Inventory has impact on users possible decisions
def YourDeath():
    print("""Coronavirus has gone crazy:
            But it hasn’t affected you yet and you decide you’re still young and life is fun 
            so you go with 2 friends skydiving.You fly up to 50,000m and your two friends jump first, followed by you.
            You are all falling really fast but you are all having the time of your life…30,000m…
            You start filming each other in the air while you fall…10,000m…You look at your height watch…5,000m….
            Now is the time to deploy your parachute…Your two friends go first…
            Perfect… no problem…You pull on your parachute…Nothing…3,000m 
            You pull on your reserve parachute… 2,000m It only half deploys slowing you slightly down… 
            but it's not slow enough… 1,000m….That's the last thing you remember. 
""")
def Introduction():
    print("""...2 years later...
You wake up from a deep deep coma.
Your eyes open... 
You're expecting to be greeted by your family… No one is there:
Your head is feeling funny and your rib cage hurts slightly along with your legs. Your eyes begin to focus…
You realise you are in a hospital room and your memory comes back. You remember everything up to 1000m…. 
You realise why you are here... You wonder where everyone is, especially your family, and why it is so quiet… 
You have to find out… *Click here to see your room*""")
def Firstscene(count, Inventory):
    userInput1 = input("What do you do? a) Walk out of room b) Stay in room ( <enter> a or b )\n:")
    count = count + 1
    if userInput1 == "a":  # Solution Path1
        TextBox1()
        WalkoutRoom(count, Inventory)
    elif userInput1 == "b":  # Will return to Walkoutroom()
        StayinRoom(count,Inventory)
def StayinRoom(count, Inventory):   # Go back to the Firstscene()
    print(""" You wait for 2 hours but nothing happens… you think to yourself “ah I’ll watch some tv to pass the time”
              you click on the on button but nothing happens… you try again… nothing.
              You decide no I can't stay here… I'll get bored… you look around your room once more... 
              only one option really remains....""")
    Firstscene(count, Inventory)
def TextBox1():
    print("""...Horror...The corridor is dark but there is a shadow standing in front of you… 
                    coughing silently… you call out “Hello”...
                    the shadow turns around violently and without hesitation begins to run in your direction... :
                    What do you do?""")

def WalkoutRoom(count,Inventory):#solution path
    count = count + 1
    userInput2 = input("The corona Zombie is coming for u, What do you do(<enter>A = fight, B = Run, C = Lock door)\n:")
    if userInput2 == "A":
        TextBox2()
        FightZombie(count,Inventory)
    elif userInput2 == "B": #solution path2
        TextBoxRun2()
        RunAwayZombie(count,Inventory)
    elif userInput2 == "C":
        print("""You lock the door and start feeling safer for a while, but the corona zombie is hammering on your door.
                 After a while he gave up and you are now safe. 
                 However after some time you decide to go out on the corridor and find a way out of the hospital.""")
        WalkoutRoom(count,Inventory)  # has to include text so maybe make seperate TextPart function = 1 more step
def TextBox2():
    print("""The Zombie is coming closer to you and you don’t know how to defend yourself.
                    There are some objects lying around you…. Which one could fit your situation the best?""")
def FightZombie(count,Inventory):  # graphics with objects #INVENTORY
    userInput3 = input("Which of the objects could help you? (Put to inventory: A Crutches, B Wheelchair, C Gun )\n:")
    if userInput3 == "A":  # put to inventory
        Inventory.append("Crutches")
        count = count + 1
        print("You pick up crutches and want to use them but how?")
        userInput5 = input("How u wanna use crutch?(A = Hit, B = Use)\n:")
        if userInput5 == "A":
            print("""You hit it well on the head… but it lets out a loud shriek… you hit it again... 
                     and this time it collapses on to the floor with a loud thud… You think to yourself... 
                     What was that thing… but before you can figure it out...
                     you see another dark figure running towards you from the shadows…
                     This time you choose to run…""")
            TextBoxRun2()
            RunAwayZombie(count,Inventory)
        elif userInput5 == "B":
            print("""You support yourself with the crutches and do a Bruce Lee sideways Karate kick… 
            you hit it well on the head… but it lets out a loud shriek… you kick it again... 
            and this time it collapses on to the floor with a loud thud… You think to yourself...'What was that thing
            ...but before you can figure it out you see another dark figure running towards you from the shadows…""")
            TextBoxRun2()
            RunAwayZombie(count,Inventory)  # going back to
    elif userInput3 == "B":  # put to inventory
        Inventory.append("Wheelchair")
        count = count + 1
        print("""You look hesitantly at it not 100% sure on how to use it… 
        unsure and panicked you push it towards the mysterious figure hoping it knocks it over… 
        NOPE…it merely made it stumble slightly… you look to your other options:""")
        WalkoutRoom(count, Inventory)
    elif userInput3 == "C":  # put to inventory
        Inventory.append("Gun")
        count = count + 1
        print("You pick up the gun, but is is light and is made out of plastic....you are running out of time!")
        WalkoutRoom(count)

def TextBoxRun2():
    print("""You are a good runner, but your leg still slightly hurts so you can’t run as fast as you once were able to.
             You turn right and run along the dark corridor being chased by a weird figure. 
             You need to find a way out of the hospital. There are two options(right or left)""")

def RunAwayZombie(count, Inventory):
    userInput4 = input("You want to find out of the hospital ( a = Right, b = Left)\n:")
    if userInput4 == "a": #going to count more
        if Inventory == "Crutches":
            print("You run against a locked door, knocking you to the ground… you are now cornered by Wuhan Zombie")  # here no count
            print("you can defend yourself with your crutches.You escaped without a survival point")
            RunAwayZombie(count, Inventory)
        elif Inventory != "Crutches":  # if inventory does not contain 'crutches' return to runawayzombie() to pick left
            count = count + 1
            print("You can not defend yourself, Pick another option")
            RunAwayZombie(count,Inventory)
        else:
            RunAwayZombie(count, Inventory)
    elif userInput4 == "b":  #solution path3
        count = count + 1
        ShowCorridor(count,Inventory)
def ShowCorridor(count, Inventory):
    userInput7 = input("A = Continue running; B = Hide in Room\n:")  # choose graphical corridor or room
    count = count + 1
    if userInput7 == "A":  # solutions path4
        TextBoxRun1()
        ContinueRunning(count, Inventory)
    elif userInput7 == "B":  # you are locked in with zombies and need to return to Left- Show_Corridor graphics
        print("""You run in and the door closes behind you with a big bang… 
            maybe the Corona Zombie heard you but this door has locked itself now and so you feel slightly relieved… Until...
            from the dark shadows of the room… 4 more figures emerge… 
            you realise you just ran into a room full of corona zombies… your screams are echoed in the hospital corridors 
            along with their infections chorus of coughs.""") #goback to graphical window
        ShowCorridor(count, Inventory)
    else:
        ShowCorridor(count, Inventory)
def TextBoxRun1():
    print("""You are a good runner, but your leg still slightly hurts so you can’t run as fast as you once were able to.
     You turn right and run along the dark corridor being chased by a weird figure. 
     You need to find a way out of the hospital. There are two options""")
def ContinueRunning(count, Inventory):  # solutions path
    userInput8 = input("A = Look; B = Hide")  # graphical reception or text with items to pick up
    count = count + 1
    if userInput8 == "A":   #solution path5 # look for items
        print("There is some stuff lying around...Which of these items could fit your situation best")
        PickupMap(count, Inventory)
    elif userInput8 == "B":
        print("""You sit there… your heart is racing… your breathing... loud…
        you try to breathe quietly but it's difficult and hurting your lungs… the air wants to escape your body.
        Suddenly a faint groan fills the large reception area… followed by a weak cough. It’s here…""")
        ContinueRunning(count,Inventory)
def PickupMap(count,Inventory):
    UserInput9 = input("Pick up: Map, Pencils ,Paper ,Staple ,Paperclip, Chair\n:")  # look for items in reception desk#Maybe str() need
    while UserInput9 != "Map":
        count = count + 1
        print("This item will not help you")
        PickupMap(count, Inventory)
    if UserInput9 == "Map": #solution path6
        Inventory.append("Map")
        print("This is your Inventory now:", Inventory)
        count = count + 1
        RuntoQuiz(count, Inventory)
    return "Map"

def RuntoQuiz(count, Inventory):
    userInput10 = input("<enter> 'Hide' or 'Run'\n:")
    count = count + 1
    if userInput10 == "Hide":
        RuntoQuiz(count, Inventory)
    elif userInput10 == "Run": #solutions path 7 #Graphical window quiz# select a)b)c) of pictures Final door
        FinalDoor(count, Inventory) #Input in graphic

def TextforQuiz():
    print("""You stand up and give it one last push!
             The map you picked up is a top secret map that has a riddle on it.
             Only the correct answer will allow you to find the exit of this hospital.
             Maybe you will live to see one more day… you run for your life... almost exhausted… 
             only the correct answer from the riddle will save you now:""")
def RiddleQuiz():
    userInput15 = input("Which of shape A, B or C is it?")
    if userInput15 == "A":
        print("Unfortunately not!")
        RiddleQuiz()
    elif userInput15 == "B":
        print("Not right, try again")
        RiddleQuiz()
    elif userInput15 =="C":
        print("Good Choice, you are close to freedom")
        FinalDoor()
def FinalDoor(count,Inventory):
    userInput22 = input("<enter>'Left' or 'Right' to ur freedom. Choose wisely...\n:")
    count = count + 1
    if userInput22 == "Left":
        print("HAHA Almost")
        FinalDoor(count, Inventory)
    elif userInput22 == "Right":
        print("!!!YOU WIN!!!")  # insert graphics picture win a nice finish
        print("your survival count is:", count, "Points. Optimal score is: 8")
        print("Your Inventory contains:", Inventory)

def main():
    count = 0
    Inventory = []
    YourDeath()#txt
    Introduction() #txt
    Firstscene(count, Inventory)
main()
#optimal step count = 8
