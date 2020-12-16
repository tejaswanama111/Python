def square(x) :
    return x * x

def cube(x) :
    return x * x * x

print("Select Method : ")
print("1. Square")
print("2. Cube")
print("3. Table of automatic square")
print("4. Table of automatic cube")

while True:

     choice = input("Enter choice(1/2/3/4): ")

     if choice == '1' :

         num1 = float(input("Enter any number: "))
         print(num1, "*", num1, "=", square(num1))

     if choice == '2' :

         num1 = float(input("Enter any number: "))
         print(num1, "*", num1, "*", num1, "=", cube(num1))

     if choice == '3' :

      x = int(input("Enter any number : "))

      for i in range(x):
        print("{} squared is {}".format(i, square(i)))

     if choice == '4' :

      x = int(input("Enter any number : "))

      for a in range(x):
        print("{} cube is {}".format(a, cube(a)))
    
     else :
             print("Invalid choice")
