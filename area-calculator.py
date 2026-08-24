
import math
#To get the pi value for circle area calculation
def welcome():
    print("Welcome to the Area Calculator!")
    print("This program will help you calculate the area of different shapes.")
    print("You can choose from the following shapes:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Square")
def calculate_rectangle_area(length, width):
    return length * width
def calculate_circle_area(radius):
    return math.pi * radius * radius
def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_square_area(side):
    return side * side
def main():
    choice = int(input('Which shape would you like to calculate the area for? (1. rectangle, 2. circle, 3. triangle, 4. square): '))
    if choice == 1:
        length = float(input('Enter the length of the rectangle: '))
        width = float(input('Enter the width of the rectangle: '))
        area = calculate_rectangle_area(length, width)
        print(f'The area of the rectangle is: {area}')
    elif choice == 2:
        radius = float(input('Enter the radius of the circle: '))
        area = calculate_circle_area(radius)
        print(f'The area of the circle is: {area}')
    elif choice == 3:
        base = float(input('Enter the base of the triangle: '))
        height = float(input('Enter the height of the triangle: '))
        area = calculate_triangle_area(base, height)
        print(f'The area of the triangle is: {area}')
    elif choice == 4:
        side = float(input('Enter the side length of the square: '))
        area = calculate_square_area(side)
        print(f'The area of the square is: {area}')
    else:
        print('Invalid choice. Please select a valid shape.')
welcome()
main()

