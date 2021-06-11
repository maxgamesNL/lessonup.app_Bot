import time

#This is the main file of the project.
#On editing write documentation for easy editing.
Running = True


#Explains what the program is to the user.
def Intro():
    print("Welcome to LessonUp Bot!!!")
    time.sleep(1.5)
    print("This bot is able to perform")
    time.sleep(1.5)
    print("A lot of actions realy fast")
    time.sleep(1.5)
    print("It is able to answer randomly.")
    time.sleep(1.5)
    print("And give custom answers")
    time.sleep(2.5)
    print("Start-Up Complete")
    time.sleep(1)   
    print("This is a list of all the commands.") 
    time.sleep(1)
    print("Type the number of your command.")
    time.sleep(1)
    print("And you will go to the menu of your command!")
    print("")



def CommandList():
    print("1. Flooder(Fills the Lesson-Up with bots that give random answers.)")
    print("")
    print("")
    print("")
    print("")

    print("To stop type stop.")
#This is where the user is shown all the options of the program.
def MainMenu():
    CommandList()
    UserInput = input("Enter the number of your command: ")
    if(UserInput == "stop" or "Stop"):
        Running = False
    else:
        UserInputNum = int(UserInput)
    







Intro()
time.sleep(3)
while(Running):
    MainMenu()