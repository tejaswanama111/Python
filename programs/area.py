def circle(r): 
    PI = 22/7
    return PI * r * r 

def square(x):
    return x * x

def multiply(x, y):
    return x * y

def area(x, y):
    return 1/2 * x * y

def ellipse(x, y):
    PI = 3.142
    return PI * x * y

def trapezoid(x, y, z):
    return 1/2 * (x + y) * z

print("Select operation.")
print("1. Area of Circle")
print("2. Area of Square")
print("3. Area of Rectangle")
print("4. Area of Triangle")
print("5. Area of Parallelogram")
print("6. Area of Kite")
print("7. Area of Rhombus")
print("8. Area of Regular Polygon")
print("9. Area of Ellipse")
print("10. Area of Trapezoid")

while True:
   
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):

        if choice == '1':
            r = float(input("Enter the radius of circle: "))
            print("PI", "*", r, "*", r, "=",'%.2f'% circle(r))

        elif choice == '2':
            x = float(input("Enter the length of side in square : "))
            print(x, "*", x, "=",'%.2f'% square(x))

        elif choice == '3':
             x = float(input("Enter the length of rectangle: "))
             y = float(input("Enter the width of rectangle: "))
             print(x, "*", y, "=",'%.2f'% multiply(x, y))
            
        elif choice == '4':
             x = float(input("Enter the base of triangle: "))
             y = float(input("Enter the height of triangle: "))
             print("1/2 *", x, "*", y, "=",'%.2f'% area(x,y))

        elif choice == '5':
             x = float(input("Enter the length of parallelogram: "))
             y = float(input("Enter the perpendicular height of parallelogram: "))
             print(x, "*", y, "=",'%.2f'% multiply(x, y))

        elif choice == '6':
            x = float(input("Enter the length of diagonals (a): "))
            y = float(input("Enter the length of diagonals (b): "))
            print("1/2 *", x, "*", y, "=",'%.2f'% area(x,y))

        elif choice == '7':
            x = float(input("Enter the length of diagonals (a): "))
            y = float(input("Enter the length of diagonals (b): "))
            print("1/2 *", x, "*", y, "=",'%.2f'% area(x,y))

        elif choice == '8':
            x = float(input("Enter the perimeter of Regular polygon: "))
            y = float(input("Enter the apothem of Regular polygon: "))
            print("1/2 *", x, "*", y, "=",'%.2f'% area(x,y))

        elif choice == '9':
            x = float(input("Enter the 2a of ellipse: "))
            y = float(input("Enter the 2b of ellipse: "))
            print("PI", "*", x, "*", y, "=",'%.2f'% ellipse(x, y))

        elif choice == '10':
            x = float(input("Enter the base (a) of trapezium: "))
            y = float(input("Enter the base (b) of trapezium: "))
            z = float(input("Enter the perpendicular height of the trapezium: "))
            print((x + y), "/ 2 *", z, "=",'%.2f'% trapezoid(x, y, z))

        break
    else:
        print("Invalid Input")
        