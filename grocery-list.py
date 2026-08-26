grocerylist = []

def addtolist():
    groceryitem = input('What would you like to add to your grocery list? ')
    if groceryitem:
        grocerylist.append(groceryitem)
        print('Item added.')
    else:
        print('Item cannot be empty.')
def removefromlist():
    if not grocerylist:
#if not checks if a condition is false. empty lists are treated as false in python
        print('Your grocery list is empty.')
        return
    printlist()
    try:
        #contains code that may produce an error, ex. 0-1 = negative number
        item_number = int(input('Which item number would you like to remove? '))
        grocerylist.pop(item_number - 1)
        print('Item removed.')
    except (ValueError, IndexError):
        #handles 2 errors, value (enters value that cant be turned into an integer)
        #and index (number refers to an item outside the lists' valid range)
        print('Please enter a valid item number.')
def printlist():
    if not grocerylist:
        print('Your grocery list is empty.')
        return
    for number, item in enumerate(grocerylist, start=1):
        #for goes through each grocery item
        #enumerate supplies both the item's number and its value
        #start = 1 makes numbering start at 1 instead of the python default zero
        print(f'{number}. {item}')
        #it will show up as '1. item' '2. item'
def put2bottom():
    if not grocerylist:
        print('Your grocery list is empty.')
        return
    #immediately ends the current function
    printlist()
    try:
        item_number = int(input('Which item number would you like to move to the bottom? '))
        grocerylist.append(grocerylist.pop(item_number - 1))
        print('Item moved.')
    except (ValueError, IndexError):
        print('Please enter a valid item number.')
def moretodo(action):
    return input(f'Would you like to {action} anything else? (y/n): ').strip().lower() in ('y', 'yes')
#.strip() removes whitespace from the beginning and end
#.lower() converts the response to lowercase

def menu():
    print('\n1. See list\n2. Add to list\n3. Remove item\n4. Move item to bottom\n5. Exit')
    #\n adds each on a seperate line
    try:
        return int(input('What would you like to do? Number answer only: '))
    except ValueError:
        print('Please enter a number.')
        return 0

def repeat_action(action, function):
    while True:
        function()
        if not moretodo(action):
            break

def welcome():
    print('Hello! This is your grocery list!')
    welcomequestion = menu()
    if welcomequestion == 1:
        printlist()
    elif welcomequestion == 2:
        repeat_action('add', addtolist)
    elif welcomequestion == 3:
        repeat_action('remove', removefromlist)
    elif welcomequestion == 4:
        repeat_action('move', put2bottom)
    elif welcomequestion == 5:
        print('Thank you, have a nice day.')
        return
    #breaks the loop
    else:
        print('Please choose an option from 1 to 5.')

welcome()