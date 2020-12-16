height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))
total = round(weight / (height * height), 2)
print("Your BMI is: ", total)

if(total <= 18.5) :
    print("{0} : Till Now You Are An Underweight Person".format(total))
elif(total <= 24.9) :
    print("{0} : Till Now You Are A Normal Person".format(total))
elif(total <= 29.9) :
    print("{0} : Till Now You Are An Overweight Person".format(total))
else :
    print("{0} :Till Now You Are An Obese Person".format(total))