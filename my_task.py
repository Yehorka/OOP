import sys
a = float(sys.argv[1])
sign = sys.argv[2]
b = float(sys.argv[3])
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
