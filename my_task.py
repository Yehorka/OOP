import sys

sys.argv.pop(0)
try:
    print(eval(' '.join(sys.argv)))
except (NameError, SyntaxError):
    print("Incorrect data")
