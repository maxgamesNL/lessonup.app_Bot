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
    print("Lots of actions realy fast")
    time.sleep(1.5)
    print("It is able to answer random.")
    time.sleep(1.5)
    print("And custom answers")
    time.sleep(2.5)
    print("Start-Up Complete")

#This is where the user is shown all the options of the program.
def MainMenu():
    print("")




Intro()
time.sleep(3)
MainMenu()
while(Running):
    
    Running = False