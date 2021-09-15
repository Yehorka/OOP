import sys
function = sys.argv[1]
i = 2
while i < len(sys.argv):
    try:
        function += sys.argv[i] #Filling string with equation
        i += 1
    except (IndexError, ValueError):
        print("Error")
        break
try:
    print("True, " + str(eval(function))) #If equation runs, it is printed
except NameError:
    print("False") #If not - print false
