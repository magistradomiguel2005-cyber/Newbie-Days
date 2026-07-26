from math import pi

print("=====================")
print("Area Calculator")
print("=====================")

print("1. Area OF TRIANGLE")
print("2. Area OF RECTANGLE")
print("3. Area OF SQUARE")
print("4. Area OF CIRCLE")
print("5. Quit")

anw = input("Enter your answer: ")

while anw != str(5):
    if anw == str(1):
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = (height*base)/2
        print(f'The area is {area}')
    elif anw == str(2):
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length*width
        print(f'The area is {area}')
    elif anw == str(3):
        side = float(input("Enter the side: "))
        area = side**2
        print(f'The area is {area}')
    elif anw == str(4):
        radius = float(input("Enter the radius: ")) 
        area = pi * (radius**2)
        print(f'The area is {area}')
    else:
        print("Invalid answer, Try Again")

    print("=====================")
    print("Area Calculator")
    print("=====================")

    print("1. Area OF TRIANGLE")
    print("2. Area OF RECTANGLE")
    print("3. Area OF SQUARE")
    print("4. Area OF CIRCLE")
    print("5. Quit")

    anw = input("Enter your answer: ")

print("Thank you!")
