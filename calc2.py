import os

while True:
    print('select a number')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Exit')
    match (input('enter your choice: ')):
        case '1':
            a = int(input('enter first number: '))
            b = int(input('enter secod number: '))
            print(f'{a} + {b} is {a+b}')
        case '2':
            a = int(input('enter first number: '))
            b = int(input('enter secod number: '))
            print(f'{a} - {b} is {a-b}')
        case '3':
            a = int(input('enter first number: '))
            b = int(input('enter secod number: '))
            print(f'{a} * {b} is {a*b}')
        case '4':    
            a = int(input('enter first number: '))
            b = int(input('enter secod number: '))
            print(f'{a} / {b} is {a/b}')
            print('existing....')
            break
        case'_':
            print('Invalid Choice')
    input('press enter to continue....')
    os.system('cls') 