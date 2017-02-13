def welcome():
    print('''
Python CLI Calculator
''')

def calculate():
    operation = input('''
Type:
+ to add
- to subtract
* to multiply
/ to divide
''')

    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))

# addition
    if operation == '+':
        print('{} + {} = '.format(num_1, num_2), num_1 + num_2)

# subtraction
    elif operation == '-':
        print('{} - {} = '.format(num_1, num_2), num_1 - num_2)

# multiplication
    elif operation == '*':
        print('{} * {} = '.format(num_1, num_2), num_1 * num_2)

# division
    elif operation == '/':
        print('{} / {} = '.format(num_1, num_2), num_1 / num_2)


    else:
        print('That is not a valid operator.')

    again()

def again():
    calc_again = input('''
Do you want to use the calculator again?
Type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

welcome()
calculate()
