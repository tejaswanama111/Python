def kelvin(x):
   return x - 273.15

def fahrenhite(x):
   return (x - 273.15) * 9/5 + 32

def celcius(x):
   return x + 273.15
    
print("Select operation.")
print("1. Kelvin To Celcius")
print("2. Kelvin To Fahrenhite")
print("3. Celcius To Kelvin")
print("4. Celcius To Fahrenhite")
print("5. Fahrenhite To Kelvin")
print("6. Fahrenhite To Celcius")

while True:
   
   choice = input("Enter choice(1/2/3/4/5/6): ")

   if choice in ('1', '2', '3', '4', '5', '6'):

        if choice == '1':
            x = float(input("Enter the temperature(in Kelvin) : "))
            print(x,"K","-273.15", "=", kelvin(x))

            break
else:
    print("Invalid Input")