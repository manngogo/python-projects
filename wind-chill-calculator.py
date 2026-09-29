t = float(input('Please enter the air temperature in fahrenheit: '))
v = float(input('Please enter the wind speed in mph: '))
w = 35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * (v ** 0.16)) #equation provided in the pdf

print(f' Wind chill is calculated to be: {w}')