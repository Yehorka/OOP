signs = ['+', '-', '/', '*']
formula = input("Enter your math expresion: ")
formula = formula.replace(' ', '')
try:
    for i in range(0, len(formula) - 1):
        if (formula[i] in signs) and (formula[i + 1] in signs):
            raise ValueError
    print(True, '\b,', eval(formula))
except (ValueError, NameError, SyntaxError, ZeroDivisionError):
    print(False, '\b,', None)
