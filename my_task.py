import sys
a = float(sys.argv[1]) #first element of equation
sign = sys.argv[2] #sign
b = float(sys.argv[3]) #second element of equation
if sign == "*":
    print(a * b)
elif sign == "/":
    print(a / b)
elif sign == "+":
    print(a + b)
elif sign == "-":
    print(a - b)
else:
    print("Error! Wrong arguments!")
