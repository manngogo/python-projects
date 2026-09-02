
from time import time


def calculate_sleep_to_wake(bed_time):
    import datetime
    bed_time_obj = datetime.datetime.strptime(bed_time, "%H:%M")
    sleep_duration1 = datetime.timedelta(hours=3)
    sleep_duration2 = datetime.timedelta(hours=6)
    sleep_duration3 = datetime.timedelta(hours=9)
    wake_time1 = bed_time_obj + sleep_duration1
    wake_time2 = bed_time_obj + sleep_duration2
    wake_time3 = bed_time_obj + sleep_duration3
    print(f'If you go to bed at {bed_time}, you should wake up at {wake_time1}, for 3 hours of sleep and 1 sleep cycle.')
    print(f'If you go to bed at {bed_time}, you should wake up at {wake_time2}, for 6 hours of sleep and 2 sleep cycles.')
    print(f'If you go to bed at {bed_time}, you should wake up at {wake_time3}, for 9 hours of sleep and 3 sleep cycles.')

def calculate_wake_to_sleep(wake_time):
    import datetime
    wake_time_obj = datetime.datetime.strptime(wake_time, "%H:%M")
    sleep_duration1 = datetime.timedelta(hours=3)
    sleep_duration2 = datetime.timedelta(hours=6)
    sleep_duration3 = datetime.timedelta(hours=9)
    bed_time1 = wake_time_obj - sleep_duration1
    bed_time2 = wake_time_obj - sleep_duration2
    bed_time3 = wake_time_obj - sleep_duration3
    print(f'If you want to wake up at {wake_time}, you should go to bed at {bed_time1}, for 3 hours of sleep and 1 sleep cycle.')
    print(f'If you want to wake up at {wake_time}, you should go to bed at {bed_time2}, for 6 hours of sleep and 2 sleep cycles.')
    print(f'If you want to wake up at {wake_time}, you should go to bed at {bed_time3}, for 9 hours of sleep and 3 sleep cycles.')

def sleep_calculator():
    print('To start, please enter what time you want to wake up or what time you\'re going to bed.')
    time = input("Enter the time (HH:MM): ")
    type = input("Is this the time you want to wake up or go to bed? (wake/bed): ").lower()
    if type == 'wake':
        wake_time = time
        calculate_wake_to_sleep(wake_time)
    elif type == 'bed':
        bed_time = time
        calculate_sleep_to_wake(bed_time)
    else:
        print('Invalid input. Please enter "wake" or "bed".')

sleep_calculator()