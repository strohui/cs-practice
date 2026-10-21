c = input('Введите операцию:')
a = float(input('Введите число:'))
b = float(input('Введите число:'))

if c == '+' or c == '-' or c == '*' or c == '-' or c == '/':
    if c == '+':
        print(a + b)
    elif c == '-' or с == '-':
        print(a - b)
    elif c == '*':
        print(a*b)
    else:
        if b != 0:
            print(a/b)
        else:
            print('Нельзя делить на 0')
elif a == 228:
    print('как же я устал учиться на мехе')

else:
    print('Введена неверная операция')
    
