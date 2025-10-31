
import math

# create shapeCalculator class
class ShapeCalculator:
    def circle(self):
        while True:
            try:
                radius = float(input("Enter the radius: "))
                if radius > 0:
                    area = math.pi * radius ** 2
                    circumference = 2 * math.pi * radius
                    print(f"the area is: {area}, and the circumference is {circumference}")
                    break
                else:
                    print("Radius must be a positive number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def rectangle(self):
        while True:
            try:
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))

                if length > 0 and width > 0:
                    area = length * width
                    perimeter = 2 * (length + width)
                    is_square = length == width
                    print(f"the area of rectangle is: {int(area)}, and its perimeter is: {int(perimeter)}")
                    print("The rectangle is square" if is_square else "The rectangle is not square")
                    break
                else:
                    print("Both length and width must be positive. Please try again.\n")
            except ValueError:
                print("Invalid input. Please enter numeric values only.\n")

    def triangle(self):
        while True:
            try:
                a = float(input("Enter side A: "))
                b = float(input("Enter side B: "))
                c = float(input("Enter side C: "))

                if a > 0 and b > 0 and c > 0:
                    # Check triangle validity using triangle inequality rule
                    if (a + b > c) and (a + c > b) and (b + c > a):
                        # Classify the triangle
                        if a == b == c:
                            triangle_type = "Equilateral"
                        elif a == b or b == c or a == c:
                            triangle_type = "Isosceles"
                        else:
                            triangle_type = "Scalene"

                        perimeter = a + b + c

                        # finding area using heron's formula
                        s = a + b + c / 2
                        area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
                        print(f"The triangle is {triangle_type}. ")
                        print(f"The perimeter is {perimeter}")
                        print(f"The area of triangle is {area}")
                        break
                    else:
                        print("The given sides do not form a valid triangle. Please try again.")
                else:
                    print("All sides must be positive. Please try again.")
            except ValueError:
                print("Invalid input. Please enter numeric values only.")

    def compare_circles(self):
         while True:
            try:
                # take radii from user
                radius1 = float(input("Enter the radius for first circle: "))
                radius2 = float(input("Enter the radius for second circle: "))
                # check for radius if they are positive
                if radius1 > 0 and radius2 > 0:
                    area1 = math.pi * radius1 ** 2
                    area2 = math.pi * radius2 ** 2
                    if area1 == area2:
                        print('Areas of both Circles are equal')
                        break
                    if area1 > area2:
                        print('The area of Circle 1 is greater than Circle 2')
                        break
                    else:
                        print('The area of Circle 2 is greater than Circle 1')
                        break
                else:
                    print("Radii must be positive numbers. Please try again.")
            except ValueError:
                print("Invalid inputs. Please enter numbers.")

# create instance of ShapeCalculator
sc = ShapeCalculator()

def showOptions():
    print("choose a number from below to continue")
    print("Option 1: Circle")
    print("Option 2: Rectangle")
    print("Option 3: Triangle")
    print("Option 4: Compare Circles")
    print("Option 5: Quit")

    while True:
        try:
            user_choice = float(input("Enter a number from 1 to 5: "))

            if 1 <= user_choice <= 5:
                if user_choice == 1:
                    sc.circle()
                    break
                elif user_choice == 2:
                    sc.rectangle()
                    break
                elif user_choice == 3:
                    sc.triangle()
                    break
                elif user_choice == 4:
                    sc.compare_circles()
                    break
                elif user_choice == 5:
                    break
            else:
                print('Number must be between 1 and 5')
        except:
            print("Input must be a number")

    print('Student ID - 100536294')
    print("You want another calculation? if so then enter 'Y'")

    user_choice2 = input('Enter Y to proceed otherwise press any key other than y or press to cancel: ')

    if user_choice2.lower() == 'y':
        showOptions() 



# show menu options to user
showOptions()

# I wrote this program as the starting point of object-oriented programming. It was fun using classes in my program. The instructions were clear, and I made the program work according to them. I faced no difficulties while coding this program and used a lot of math in it. I coded in my own way since there were no restrictions or specific instructions on how to solve the problem.