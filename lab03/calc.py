c = input('Введите операцию:')
a = float(input('Введите число:'))
b = float(input('Введите число:'))

if c == '+' or c == '-' or c == '*' or c == '-':
    if c == '+':
        print(a + b)
    elif c == '-' or с == '-':
        print(a - b)
    else:
        print(a*b)



else:
    print('Введена неверная операция')
