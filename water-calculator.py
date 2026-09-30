# To find the minimum amount of water you should be drinking per day
def qanda():
     print('All liquid values must be in ounces, the final result will be converted for you later.')
     print('Please input these values as floats, ex. 000.00000')
     weight = float(input('What is your body weight in pounds?: '))
     activity_minutes = float(input('About how many minutes of physical activity do you do each day?: '))
     print('Please enter a "yes" or "no" for these remaining questions')
     climate_answer = input('Do you live in a hot, humid, or high-altitude environment?: ').lower()
     protein_answer = input('Do you eat a high protein diet?: ').lower()
     sodium_answer = input('Do you eat a high sodium diet?: ').lower()
     fiber_answer = input('Do you eat a high fiber diet?: ').lower()
     return weight / 2, activity_minutes, climate_answer, protein_answer, sodium_answer, fiber_answer

#if one is living in a humid, hot, or high-altitude environment, instead of half of your weight in ounces it should be your weight in ounces
def climate(baseline):
     return baseline + 12.0

#per every 30 minutes of physical activity, you must drink 12 extra ounces of water
def activity(baseline, activity_minutes):
     return baseline + min((activity_minutes / 30) * 12, 24.0)

#if one has a high protein diet, drink 2-4 cups extra to help your body process the protein
#2-4 cups is 16-32oz
def protein(baseline):
     print('Please enter the next values as floats 00.0000')
     program = float(input('How many grams of protein do you consume in a day?: '))
     print('Please enter either a "yes" or a "no" for the following questions.')
     muscle = input('Are you actively trying to build muscle?: ').strip().lower()
     bodybuilder = input('Are you a bodybuilder?: ').strip().lower()
     diet = input('Are you on a carnivore or keto diet?: ').strip().lower()
     if bodybuilder == 'yes' or diet == 'yes':
          return 16.0
     elif muscle == 'yes' or program > 120:
          return 12.0
     return 8.0

#if one has a high fiber diet, drink 8-16oz extra
def fiber(baseline):
     print('Please enter your answer as a float 00.0000')
     totalfiber = float(input('How much total grams of fiber do you think you eat a day?: '))
     print('Please enter either a "yes" or a "no" for the following questions.')
     wholefoods = input('Does your fiber come entirely from whole foods?: ').strip().lower()
     supplements = input('Do you take fiber supplements?: ').strip().lower()
     if supplements == 'yes':
          return 16.0
     return 8.0

#if one has a high sodium diet, not to drink a set amount, but as much as they are thirsty, so a range of values
def sodium(baseline):
     print('Since you drink a lot of sodium, make sure to drink your minimum amount of water.')
     print('Drink more water as you feel thirsty.')
     return baseline

def calculation():
     baseline, activity_minutes, climate_answer, protein_answer, sodium_answer, fiber_answer = qanda()

     if climate_answer == 'yes':
          baseline = climate(baseline)
     else:
          baseline = activity(baseline, activity_minutes)
     if protein_answer == 'yes':
          protein_adjustment = protein(baseline)
     else:
          protein_adjustment = 0.0
     if fiber_answer == 'yes':
          fiber_adjustment = fiber(baseline)
     else:
          fiber_adjustment = 0.0
     baseline += max(protein_adjustment, fiber_adjustment)
     if sodium_answer == 'yes':
          baseline = sodium(baseline)

     print(f'Minimum water recommendation: {baseline:.2f} ounces per day.')
     return baseline


if __name__ == '__main__':
     calculation()
