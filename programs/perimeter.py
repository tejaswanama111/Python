def circle(r): 
    PI = 22/7
    return 2 * PI * r 

def square(x):
    return 4 * x

def multiply(x, y):
    return 2*x+2*y

def triangle(x,y,z):
    x +y +z

def perimeter(x, y):
    return 1/2 * x * y

def polygon(x, y):
    return x * y

def trapezoid(w, x, y, z):
    return w +x +y +z

print("Select operation.")
print("1. Perimeter of Circle")
print("2. Perimeter of Square")
print("3. Perimeter of Rectangle")
print("4. Perimeter of Triangle")
print("5. Perimeter of Parallelogram")
print("6. Perimeter of Kite")
print("7. Perimeter of Rhombus")
print("8. Perimeter of Regular Polygon")
print("9. Perimeter of Trapezoid")

while True:
   
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):

        if choice == '1':
            r = float(input("Enter the radius of circle: "))
            print("2", "*", "PI", "*", r, "=",'%.2f'% circle(r))

        elif choice == '2':
            x = float(input("Enter the length of side in square : "))
            print("4", "*", x, "=",'%.2f'% square(x))

        elif choice == '3':
             x = float(input("Enter the length of rectangle: "))
             y = float(input("Enter the width of rectangle: "))
             print("2(", x, "+", y,")","=",'%.2f'% multiply(x, y))
            
        elif choice == '4':
             x = float(input("Enter the first length of triangle: "))
             y = float(input("Enter the second length of triangle: "))
             z = float(input("Enter the third length of triangle: "))
             print(x, "+", y, "+", z,"=",'%.2f'% triangle(x,y,z))

        elif choice == '5':
             x = float(input("Enter the length of parallelogram: "))
             y = float(input("Enter the width of parallelogram: "))
             print("2(", x, "+", y,")","=",'%.2f'% multiply(x, y))

        elif choice == '6':
            x = float(input("Enter the length of kite: "))
            y = float(input("Enter the width of kite: "))
            print("2(", x, "+", y,")","=",'%.2f'% multiply(x, y))

        elif choice == '7':
            x = float(input("Enter the length of diagonals (a): "))
            y = float(input("Enter the length of diagonals (b): "))
            print("1/2 *", x, "*", y, "=",'%.2f'% perimeter(x,y))

        elif choice == '8':
            x = float(input("Enter the length of side in rhombus: "))
            print("4", "*", x, "=",'%.2f'% square(x))

        elif choice == '9':
            w = float(input("Enter the first length of trapezoid: "))
            x = float(input("Enter the first second of trapezoid: "))
            y = float(input("Enter the first third of trapezoid: "))
            z = float(input("Enter the first fourth of trapezoid: "))
            print(w, "+", x, "+", y, "+", z,"=",'%.2f'% trapezoid(w, x, y, z))

        break
    else:
        print("Invalid Input")
        