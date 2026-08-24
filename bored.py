import random
def bored():
    question = input("Type 'bored' to get started and be given a random activity to do: ")
    if question == 'bored':
        question = input("Type 'self' for a self activity and 'couple' for a couple activity: ")
        if question == 'self':
            num = random.randint(1, 40)
            #Responses based on the number generated
            if num == 1:
                print('Got any languages you want to learn?')
            elif num == 2:
                print ('How about reading a book?')
            elif num == 3:
                print ('Going for a walk?')
            elif num == 4:
                print ('Want to try some meditation?')
            elif num == 5:
                print ('How about journaling?')
            elif num == 6:
                print ('How about a movie night?')
            elif num == 7:
                print ('Can\'t hurt to work out...')
            elif num == 8:
                print ('How about trying a new recipe?')    
            elif num == 9:
                print ('Want to try a new craft or DIY project?')
            elif num == 10:
                print ('Are there any plants you can tend to or plant right now?')
            elif num == 11:
                print ('Play sudoku.')
            elif num == 12:
                print ('How about going bird watching?')
            elif num == 13:
                print ('Is there a hobby you have been wanting to pick up?')
            elif num == 14:
                print ('You know what would be fun? Dress up and fashion show!')
            elif num == 15:
                print ('How about a spa day at home?')
            elif num == 16:
                print ('Are there are chores you still need to do or would make your life easier if you did them now while you have the time?')
            elif num == 17:
                print ('Maybe try sewing something you want to wear or something you want to use?')
            elif num == 18:
                print ('Burn MLP onto a DVD and watch it!')
            elif num == 19:
                print ('Play Genshin Impact or another game you enjoy!')
            elif num == 20:
                print ('Do your makeup for funsies and try a new look.')
            elif num == 21:
                print ('Play with your cat?')
            elif num == 22:
                print ('Volunteer for your community.')
            elif num == 23:
                print ('Try a new workout or yoga routine.')
            elif num == 24:
                print ('Go somewhere you\'ve wanted to go to.')
            elif num == 25:
                print ('Plan a trip.')
            elif num == 26:
                print ('Make a pinterest board.')
            elif num == 27:
                print ('Plan your schedule.')
            elif num == 28:
                print ('Make a vision board.')
            elif num == 29:
                print ('Start a scrapbook.')
            elif num == 30:
                print ('Make a bucket list.')
            elif num == 31:
                print ('Crochet something.')
            elif num == 32:
                print ('Knit something.')
            elif num == 33:
                print ('Drink some water.')
            elif num == 34:
                print ('Invent something that would make your life easier.')
            elif num == 35:
                print ('Make a new habit.')
            elif num == 36:
                print ('Make a new friend.')
            elif num == 37:
                print ('Go window shopping.')
            elif num == 38:
                print ('Do an online trend.')
            elif num == 39:
                print ('Write a book.')
            elif num == 40:
                print ('Write a letter to someone for the future.')
            else:
                print ('Error. Try again.')
        elif question == 'couple':
            question2 = input("Type 'online' for an online activity and 'person' for a in-person activity: ")
            if question2 == 'online':
                num = random.randint(1, 40)
                if num == 1:
                    print('Play a game together.')
                elif num == 2:
                    print ('Watch a movie together.')
                elif num == 3:
                    print ('Have a virtual dinner date.')
                elif num == 4:
                    print ('Take an online class together.')
                elif num == 5:
                    print ('Do a virtual workout together.')
                elif num == 6:
                    print ('Have a video call and catch up on each other\'s lives.')
                elif num == 7:
                    print ('Play an online quiz or trivia game together.')
                elif num == 8:
                    print ('Paint and sip.')
                elif num == 9:
                    print ('Play Truth or Dare.')
                elif num == 10:
                    print ('Do a virtual escape room together.')
                elif num == 11:
                    print ('Have a virtual karaoke night.')
                elif num == 12:
                    print ('Do a virtual scavenger hunt together.')
                elif num == 13:
                    print ('Do online trends.')
                elif num == 14:
                    print ('Have a virtual book club meeting.')
                elif num == 15:
                    print ('Cook together on video.')
                elif num == 16:
                    print ('Go on a virtual museum tour.')
                elif num == 17:
                    print ('Make a care package.')
                elif num == 18:
                    print ('Have a virtual art or craft night together.')
                elif num == 19:
                    print ('Write each other letters or emails for the future.')
                elif num == 20:
                    print ('Start a digital journal or scrapbook together.')
                elif num == 21:
                    print ('Put on a fashion show.')
                elif num == 22:
                    print ('Have a spa day.')
                elif num == 23:
                    print ('Make a vision board.')
                elif num == 24:
                    print ('Make a bucket list.')
                elif num == 25:
                    print ('Play charades.')
                elif num == 26:
                    print ('Have a powerpoint party.')
                elif num == 27:
                    print ('We\'re all under the same sky. Try stargazing together at night.')
                elif num == 28:
                    print ('Pick up a new hobby together.')
                elif num == 29:
                    print ('Send "open when" letters.')
                elif num == 30:
                    print ('Send a bouquet of flowers.')
                elif num == 31:
                    print ('Take online quizzes.')
                elif num == 32:
                    print ('Ask them about their day.')
                elif num == 33:
                    print ('Answer riddles together.')
                elif num == 34:
                    print ('Guess the drawing.')
                elif num == 35:
                    print ('Roblox horror game.')
                elif num == 36:
                    print ('Take a photo at every hour of the day and compare.')
                elif num == 37:
                    print ('Make a time capsule.')
                elif num == 38:
                    print ('Make an in depth critique about something.')
                elif num == 39:
                    print ('Play headsup.')
                elif num == 40:
                    print ('Do chores together.')
                else:
                    print ('Error. Try again.')
            elif question2 == 'person':
                num = random.randint(1, 40)
                if num == 1:
                    print('Go for a walk or hike together.')
                elif num == 2:
                    print ('Have a picnic in the park.')
                elif num == 3:
                    print ('Cook a meal together.')
                elif num == 4:
                    print ('Go to a museum.')
                elif num == 5:
                    print ('Go to an art gallery.')
                elif num == 6:
                    print ('Go out to eat at a new restaurant or cafe.')
                elif num == 7:
                    print ('Go grocery shopping.')
                elif num == 8:
                    print ('Go shopping.')
                elif num == 9:
                    print ('Take a day trip to a nearby town or city.')
                elif num == 10:
                    print ('Volunteer together for a cause you both care about.')
                elif num == 11:
                    print ('Go to a local event or festival.')
                elif num == 12:
                    print ('Go to a local farmers market.')
                elif num == 13:
                    print ('Go to a local park or nature reserve.')
                elif num == 14:
                    print ('Go to a local zoo or aquarium.')
                elif num == 15:
                    print ('Go to a local botanical garden or arboretum.')
                elif num == 16:
                    print ('Go to a local historical site or landmark.')
                elif num == 17:
                    print ('Go to a local theater or performance venue.')
                elif num == 18:
                    print ('Go to a local sports game or event.')
                elif num == 19:
                    print ('Go to a local amusement park or carnival.')
                elif num == 20:
                    print ('Go to a local beach or lake.')
                elif num == 21:
                    print ('Plan a trip the two of you will go on together.')
                elif num == 22:
                    print ('Go to a local arcade or gaming center.')
                elif num == 23:
                    print ('Go to a local escape room or puzzle room.')
                elif num == 24:
                    print ('Go to a rage room.')
                elif num == 25:
                    print ('When was the last time you went to a trampoline park?')
                elif num == 26:
                    print ('Go to a cooking class.')
                elif num == 27:
                    print ('Go to an art class.')
                elif num == 28:
                    print ('Pottery.')
                elif num == 29:
                    print ('Attend a class on how to take the perfect photos.')
                elif num == 30:
                    print ('Go to a library and read together.')
                elif num == 31:
                    print ('Go sightseeing.')
                elif num == 32:
                    print ('Take advantage of a free event.')
                elif num == 33:
                    print ('Go to a pilates class.')
                elif num == 34:
                    print ('Take a self defense class.')
                elif num == 35:
                    print ('Have a picnic.')
                elif num == 36:
                    print ('Go to different state.')
                elif num == 37:
                    print ('Get egg tarts in Chinatown.')
                elif num == 38:
                    print ('Go fishing and learn how to fish.')
                elif num == 39:
                    print ('Make your own custom item.')
                elif num == 40:
                    print ('Go to some kind of pop-up event.')   
                else:
                    print ('Error. Try again.')      
            else:
                print ('Error. Try again.')   
        else:
            print ('Error. Try again.')
    else:
        print ('Error. Try again.')
        print('Please type "bored" to get started.')
bored()
def loop():
    questions = input('Do you want another activity? Type "yes" to rerun the program or "no" to exit.')
    if questions == 'yes':
        bored()
        loop()
    elif questions == 'no':
        print('Thanks for using the program! Have a great day!')
    else:
        print('Error. Try again.')
loop()