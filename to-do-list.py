todolist = []

def addtolist():
    tasktodo = input('What would you like to add to your todo list? ')
    if tasktodo:
        todolist.append(tasktodo)
        print('Task added.')
    else:
        print('Task cannot be empty.')
def removefromlist():
    if not todolist:
#if not checks if a condition is false. empty lists are treated as false in python
        print('Your todo list is empty.')
        return
    printlist()
    try:
        #contains code that may produce an error, ex. 0-1 = negative number
        item_number = int(input('Which item number would you like to remove? '))
        todolist.pop(item_number - 1)
        print('Task removed.')
    except (ValueError, IndexError):
        #handles 2 errors, value (enters value that cant be turned into an integer)
        #and index (number refers to an item outside the lists' valid range)
        print('Please enter a valid item number.')
def printlist():
    if not todolist:
        print('Your todo list is empty.')
        return
    for number, task in enumerate(todolist, start=1):
        #for goes through each task 
        #enumerate supplies both the task's number and its value
        #start = 1 makes numbering start at 1 instead of the python default zero
        print(f'{number}. {task}')
        #it will show up as '1. task' '2.task'
def put2bottom():
    if not todolist:
        print('Your todo list is empty.')
        return
    #immediately ends the current function
    printlist()
    try:
        item_number = int(input('Which item number would you like to move to the bottom? '))
        todolist.append(todolist.pop(item_number - 1))
        print('Task moved.')
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
    print('Hello! This is your todo list!')
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