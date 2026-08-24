def game():
    print('You woke up as your cat! Can you find a way to switch back to your human form?')
    print('What would you like to do first?')
    print('1. Explore the world')
    print('2. Look for food')
    print('3. Find yourself')
    print('4. Take a nap')
    choice1 = input('Enter the number of your choice: ')
    if choice1 == '1':
        print('You walk around your home, finding it difficult to get used to your new feline body.')
        print('Thud...')
        print('Squeak!')
        print('A mouse appears!')
        print('What would you like to do next?')
        print('1. Hunt the mouse')
        print('2. Find yourself')
        print('3. Take a nap')
        print('4. Look for food')
        choice2 = input('Enter the number of your choice: ')
        if choice2 == '1':
            print('You chase the mouse, but it escapes. You feel frustrated.')
            print('What would you like to do next?')
            print('1. Find yourself')
            print('2. Take a nap')
            print('3. Look for food')
            choice3 = input('Enter the number of your choice: ')
            if choice3 == '1':
                print('You are unable to find yourself.')
                print('What would you like to do next?')
                print('1. Take a nap')
                print('2. Look for food')
                choice4 = input('Enter the number of your choice: ')
                if choice4 == '1':
                    print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                    print('Congratulations! You have completed the game.')
                    print('Thank you for playing!')
                    print('Would you like to play again? (yes/no)')
                    loop_choice = input('Enter your choice: ')
                    if loop_choice == 'yes':
                        print('Restarting the game...')
                        game()
                    else:
                        print('Thank you for playing! Goodbye!')
                elif choice4 == '2':
                    print('You wait for the automatic feeder to go off.')
                    print('Tick tock tick tock...')
                    print('The feeder goes off on schedule!')
                    print('What would you like to do now?')
                    print('1. Eat the food')
                    print('2. Take a nap')
                    choice5 = input('Enter the number of your choice: ')
                    if choice5 == '1':
                        print('You eat the food and do not get satisfaction.')
                        print('You feel frustrated and tired.')
                        print('What would you like to do now?')
                        print('1. Take a nap')
                        choice6 = input('Enter the number of your choice: ')
                        if choice6 == '1':
                            print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                            print('Congratulations! You have completed the game.')
                            print('Thank you for playing!')
                            print('Would you like to play again? (yes/no)')
                            loop_choice = input('Enter your choice: ')
                            if loop_choice == 'yes':
                                print('Restarting the game...')
                                game()
                            else:
                                print('Thank you for playing! Goodbye!')
            elif choice3 == '2':
                print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                print('Congratulations! You have completed the game.')
                print('Thank you for playing!')
                print('Would you like to play again? (yes/no)')
                loop_choice = input('Enter your choice: ')
                if loop_choice == 'yes':
                    print('Restarting the game...')
                    game()
                else:
                    print('Thank you for playing! Goodbye!')
            elif choice3 == '3':
                print('You wait for the automatic feeder to go off.')
                print('Tick tock tick tock...')
                print('The feeder goes off on schedule!')
                print('What would you like to do now?')
                print('1. Eat the food')
                print('2. Take a nap')
                choice5 = input('Enter the number of your choice: ')
                if choice5 == '1':
                    print('You eat the food and do not get satisfaction.')
                    print('You feel frustrated and tired.')
                    print('What would you like to do now?')
                    print('1. Take a nap')
                    choice6 = input('Enter the number of your choice: ')
                    if choice6 == '1':
                        print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                        print('Congratulations! You have completed the game.')
                        print('Thank you for playing!')
                        print('Would you like to play again? (yes/no)')
                        loop_choice = input('Enter your choice: ')
                        if loop_choice == 'yes':
                            print('Restarting the game...')
                            game()
                        else:
                            print('Thank you for playing! Goodbye!')
        elif choice2 == '2':
            print('You are unable to find yourself.')
            print('What would you like to do next?')
            print('1. Take a nap')
            print('2. Look for food')
            choice3 = input('Enter the number of your choice: ')
            if choice3 == '1':
                print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                print('Congratulations! You have completed the game.')
                print('Thank you for playing!')
                print('Would you like to play again? (yes/no)')
                loop_choice = input('Enter your choice: ')
                if loop_choice == 'yes':
                    print('Restarting the game...')
                    game()
                else:
                    print('Thank you for playing! Goodbye!')
            elif choice3 == '2':
                print('You wait for the automatic feeder to go off.')
                print('Tick tock tick tock...')
                print('The feeder goes off on schedule!')
                print('What would you like to do now?')
                print('1. Eat the food')
                print('2. Take a nap')
                choice4 = input('Enter the number of your choice: ')
                if choice4 == '1':
                    print('You eat the food and do not get satisfaction.')
                    print('You feel frustrated and tired.')
                    print('What would you like to do now?')
                    print('1. Take a nap')
                    choice5 = input('Enter the number of your choice: ')
                    if choice5 == '1':
                        print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                        print('Congratulations! You have completed the game.')
                        print('Thank you for playing!')
                        print('Would you like to play again? (yes/no)')
                        loop_choice = input('Enter your choice: ')
                        if loop_choice == 'yes':
                            print('Restarting the game...')
                            game()
                        else:
                            print('Thank you for playing! Goodbye!')
                elif choice4 == '2':
                    print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                    print('Congratulations! You have completed the game.')
                    print('Thank you for playing!')
                    print('Would you like to play again? (yes/no)')
                    loop_choice = input('Enter your choice: ')
                    if loop_choice == 'yes':
                        print('Restarting the game...')
                        game()
                    else:
                        print('Thank you for playing! Goodbye!')
                else:
                    print('Invalid choice. Please select a valid option.')
        elif choice2 == '3':
            print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
            print('Congratulations! You have completed the game.')
            print('Thank you for playing!')
            print('Would you like to play again? (yes/no)')
            loop_choice = input('Enter your choice: ')
            if loop_choice == 'yes':
                print('Restarting the game...')
                game()
            else:
                print('Thank you for playing! Goodbye!')
        elif choice2 == '4':
            print('You wait for the automatic feeder to go off.')
            print('Tick tock tick tock...')
            print('The feeder goes off on schedule!')
            print('What would you like to do now?')
            print('1. Eat the food')
            print('2. Take a nap')
            choice3 = input('Enter the number of your choice: ')
            if choice3 == '1':
                print('You eat the food and do not get satisfaction.')
                print('You feel frustrated and tired.')
                print('What would you like to do now?')
                print('1. Take a nap')
                choice4 = input('Enter the number of your choice: ')
                if choice4 == '1':
                    print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                    print('Congratulations! You have completed the game.')
                    print('Thank you for playing!')
                    print('Would you like to play again? (yes/no)')
                    loop_choice = input('Enter your choice: ')
                    if loop_choice == 'yes':
                        print('Restarting the game...')
                        game()
                    else:
                        print('Thank you for playing! Goodbye!')
            if choice3 == '2':
                print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                print('Congratulations! You have completed the game.')
                print('Thank you for playing!')
                print('Would you like to play again? (yes/no)')
                loop_choice = input('Enter your choice: ')
                if loop_choice == 'yes':
                    print('Restarting the game...')
                    game()
                else:
                    print('Thank you for playing! Goodbye!')
    elif choice1 == '2':
        print('You wait for the automatic feeder to go off.')
        print('Tick tock tick tock...')
        print('The feeder goes off on schedule!')
        print('What would you like to do now?')
        print('1. Eat the food')
        print('2. Take a nap')
        choice2 = input('Enter the number of your choice: ')
        if choice2 == '1':
            print('You eat the food and do not get satisfaction.')
            print('You feel frustrated and tired.')
            print('What would you like to do now?')
            print('1. Take a nap')
            choice3 = input('Enter the number of your choice: ')
            if choice3 == '1':
                print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                print('Congratulations! You have completed the game.')
                print('Thank you for playing!')
                print('Would you like to play again? (yes/no)')
                loop_choice = input('Enter your choice: ')
                if loop_choice == 'yes':
                    print('Restarting the game...')
                    game()
                else:
                    print('Thank you for playing! Goodbye!')
            if choice3 == '2':
                print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                print('Congratulations! You have completed the game.')
                print('Thank you for playing!')
                print('Would you like to play again? (yes/no)')
                loop_choice = input('Enter your choice: ')
                if loop_choice == 'yes':
                    print('Restarting the game...')
                    game()
                else:
                    print('Thank you for playing! Goodbye!')
    elif choice1 == '3':
        print('You are unable to find yourself.')
        print('What would you like to do next?')
        print('1. Take a nap')
        print('2. Look for food')
        choice2 = input('Enter the number of your choice: ')
        if choice2 == '1':
            print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
            print('Congratulations! You have completed the game.')
            print('Thank you for playing!')
            print('Would you like to play again? (yes/no)')
            loop_choice = input('Enter your choice: ')
            if loop_choice == 'yes':
                print('Restarting the game...')
                game()
            else:
                print('Thank you for playing! Goodbye!')
        elif choice2 == '2':
            print('You wait for the automatic feeder to go off.')
            print('Tick tock tick tock...')
            print('The feeder goes off on schedule!')
            print('What would you like to do now?')
            print('1. Eat the food')
            print('2. Take a nap')
            choice3 = input('Enter the number of your choice: ')
            if choice3 == '1':
                print('You eat the food and do not get satisfaction.')
                print('You feel frustrated and tired.')
                print('What would you like to do now?')
                print('1. Take a nap')
                choice4 = input('Enter the number of your choice: ')
                if choice4 == '1':
                    print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                    print('Congratulations! You have completed the game.')
                    print('Thank you for playing!')
                    print('Would you like to play again? (yes/no)')
                    loop_choice = input('Enter your choice: ')
                    if loop_choice == 'yes':
                        print('Restarting the game...')
                        game()
                    else:
                        print('Thank you for playing! Goodbye!')
            if choice3 == '2':
                print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
                print('Congratulations! You have completed the game.')
                print('Thank you for playing!')
                print('Would you like to play again? (yes/no)')
                loop_choice = input('Enter your choice: ')
                if loop_choice == 'yes':
                    print('Restarting the game...')
                    game()
                else:
                    print('Thank you for playing! Goodbye!')
    elif choice1 == '4':
        print('You take a nap and wake up as a human again! You have successfully switched back to your human form.')
        print('Congratulations! You have completed the game.')
        print('Thank you for playing!')
        print('Would you like to play again? (yes/no)')
        loop_choice = input('Enter your choice: ')
        if loop_choice == 'yes':
            print('Restarting the game...')
            game()
        else:
            print('Thank you for playing! Goodbye!')
game()