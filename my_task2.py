import sys
function = sys.argv[1]
i = 2
while i < len(sys.argv):
    try:
        function += sys.argv[i]
        i += 1
    except (IndexError, ValueError):
        print("Error")
        break
try:
    print("True, " + str(eval(function)))
except NameError:
    print("False")
