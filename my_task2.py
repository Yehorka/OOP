import sys
import operator

try:
    function = getattr(operator, sys.argv[1])
    print(function(float(sys.argv[2]), float(sys.argv[3])))
except Exception:
    print("Incorrect data")