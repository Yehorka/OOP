import sys
function = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])
if function == "multiply":
    print(a * b)
elif function == "divide":
    print(a / b)
elif function == "add":
    print(a + b)
elif function == "subtract":
    print(a - b)
else:
    print("Error! Wrong arguments!")
