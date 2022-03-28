# Mwila Kangombe
# CSS - 225
# 03/24/2022

# Action-Adventure Game



# Chapter 1


def Chap1():
    print("First time in Hong Kong is always the hardest. Coming from America and trying to get around is hard\
 you explore Hong Kong in your quest to find a grandmaster teacher. Locals tell you to find Master Chow or Master Kusama")

    choice = int(input('What would you like to do?\n1.Start to Learn\n'\
                       '2.Paitience training\n3.Talk to villagers\nEnter your choice (1, 2, or 3):'))
    if choice == 1:
        print('Great You learned about chinese culture take on another task!')
        Chap1()

    elif choice == 2:
        print('Fantastic you have learned some paitience and are set to move on.')
        Chap1()

    elif choice == 3:
        print('The villagers have told you of a great teacher who lives in the mountains are you ready to explore them?')
        choice2 = int(input("\n1. Yes \n2. No \nEnter your choice(1, 2): "))
        if choice2 == 1:
            Chap2()
        else: 
            print("Thanks for playing!")
   
    else:
        print('That is not correct. Try again.')
        Chap1()


# Chapter 2

# Impress Module Task
        
def Chap2():
    print("Grandmaster Chow leaves in the Mountains. He has the knowledge you need to win the competition. You meet Mr. Chow and start to gain understanding")
    choice = int(input("Would you like to begin holding your breath for two minutes? \n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print("Lets get started")
    if choice == 2:
        print('You are back at chapter 1')
        Chap1()

#player continues with module to hold breath

    choice = int(input("Have you succeded at holding your breath? \n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print("Great job!")
        Chap3()

    elif choice == 2:
        print("Game has returned you back to chapter 1!")
        Chap1()
        
    else:
        print('Game over!')        

    


# Chapter 3

# Training Module Task
       

def Chap3():
    print( " You succeeded by holding your breath for 2 minutes, Mr. Chow agrees to teach and train you. You start to learn.")

    choice = int(input(" Are you ready to train with Grandmaster Chow? \n1. Yes \n2. No \nEnter your choice(1, 2): "))

    if choice == 1:
        print("Excellent!")
    if choice == 2:
        print('You are back at chapter 2')
        Chap2()

# Player continues with module to train with Grandmaster Chow

    choice = int(input("Are you ready to learn the four elements? \n1. Yes \n2. No \nEnter your choice(1, 2): "))

    if choice == 1:
        print("Terrific! Tell Master Chow")
    if choice == 2:
        print('You are back at chapter 2')
        Chap2()

# Dialogue with Master Chow

    choice = int(input(" Duke have you Masterd the four elements water, earth, fire, air through your mind? \n1. Yes \n2. No \nEnter your choice(1, 2): "))

    if choice == 1:
        print(" You getting closer to learning what it takes to be a champion move on!")
        Chap4()

    elif choice == 2:
        print("You are back to chapter one you can also call home and speak to your family!")
        Chap1()

    else:
        print(' Not an option. Try again.')
        Chap3()

        

# Chapter 4

# Mastering meditation task

def Chap4():
    print(" You have made great progress in your training, it is now time for you to learn the secret of Kung Fu. Mr. Chow tells\
you to take a deep breath and concentrate, the secret of Kung Fu is to become one with yourself nothing should disturb you.")

    choice = int(input("Are you ready to learn the secrets of Kung Fu which are imagination and meditation? \n1. Yes \n2. No \nEnter your choice(1, 2): "))

    if choice == 1:
        print("Amazing lets get started!")
    if choice == 2:
        print('You are back at chapter 3')
        Chap3()

# Player continues with module to train with Grandmaster Chow

    choice = int(input(" Are you ready to master these three actions: close eyes and meditate, imagine seeing black belt, & imagine fighting opponent?\
                       \n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print("You are gaining wisdom tell Master Chow you understand!")
    if choice == 2:
        print('You are back at chapter 3')
        Chap3()

# Dialogue with Master Chow

    choice = int(input("Duke have you learned the secrets & Masterd the three actions? \n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print(" Terrific You are almost ready for the finals!")
        Chap5()

    elif choice == 2:
        print("You are back at chapter three and will sleep and dream of what you desire")
        Chap3()
        
    else:
        print('Not a valid choice. Try again.')
        Chap4()


# Chapter 5

# All actions lead to the end

        
def Chap5():
    print("You can’t believe it with your eyes closed you are actually in the battle for the black belt that you desire.")

    choice = int(input("Are you ready to master speed, body strenght,and Kung Fu?\n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print("Excellent! From this day forward Kung Fu will be like the air you breath.")
    if choice == 2:
        print('You are back at chapter 4')
        Chap4()

# player continues to speed

    choice = int(input("Have you used your speed moves?\n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print("You can move as fast as Bruce Lee Now!.")
    if choice == 2:
        print('You are back at chapter 4')
        Chap4()

# player continues to body strenght

    choice = int(input("Duke have you used your body strenght moves?\n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print("You are as strong as Bear Now!.")
    if choice == 2:
        print('You are back at chapter 4')
        Chap4()

# player continues to Kung Fu

    choice = int(input("Duke have you used your Kung fu moves?\n1. Yes \n2. No \nEnter your choice(1, 2): "))
    if choice == 1:
        print( "You fight for the black belt and win, you open your eyes with the belt in your hands! End of story")
        print("You are now a champion!.")


    elif choice == 2:
        print(" You are going back to chapter 4 to learn the secrets!")
        chap4()

    else: 
      print("Not a valid choice. Try again!")
      Chap5()


name = input('Welcome to the adventure game of Duke in Hong Kong! What is your name? ')
print("Hi",name,"! In this game you will be taking on the role of Duke. Duke is A fighter trying\
to learn Kung Fu so he can win a black belt competition in Hong Kong. In this game you\
will Fight for the black belt and win, visit a martial arts master in the town to learn,\
talk to other people, and learn about the secret of Kung Fu.")

Chap1()














        
