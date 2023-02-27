import os

while True:
    print('select a number')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Exit')
    ch = input('enter your choice: ')
    if ch == '1':
        a = int(input('enter first number: '))
        b = int(input('enter secod number: '))
        print(f'{a} + {b} is {a+b}')
    elif ch == '2':
        a = int(input('enter first number: '))
        b = int(input('enter secod number: '))
        print(f'{a} - {b} is {a-b}')
    elif ch == '3':
        a = int(input('enter first number: '))
        b = int(input('enter secod number: '))
        print(f'{a} * {b} is {a*b}')
    elif ch == '4':    
        a = int(input('enter first number: '))
        b = int(input('enter secod number: '))
        print(f'{a} / {b} is {a/b}')
        print('existing....')
        break
    else:
        print('Invalid Choice')
    input('press enter to continue.....')
    os.system('cls')    