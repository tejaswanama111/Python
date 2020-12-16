print("In this statement if 'a' is written anywhere then the name writing process is stop there")

a = str(input("Enter any name : "))

for i in a:
     if i == 'a':
         print("You lost !! Here a is written")
         break
     else:
         print(i)
         print("You Won !!")
