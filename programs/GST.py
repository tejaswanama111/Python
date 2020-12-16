OP = float(input("Enter Original Price : "))
GST = float(input(("Enter GST : ")))
cal = OP*GST/100
total = OP + cal
print("Total : ", total)