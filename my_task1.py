import sys
function = sys.argv[1] #function
a = float(sys.argv[2]) #first element of equation
b = float(sys.argv[3]) #second element of equation
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
