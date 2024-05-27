def calculator():
    try:
        num1 = float(input('Write down the first number: '))

        while True:
            operator = input('Write down the symbol (+, -, *, /): ')
            if operator in ['+', '-', '*', '/']:
                break
            else:
                print('The operator is not correct. Try again.')

        num2 = float(input('Write down the second number: '))
        if operator == '+':
            result = num1 + num2

        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                result = 0
                print('Cant divide by zero')

            return
        print(f"The result: {(result)}")

    except ValueError:
        print('Error: numbers are incorrect')


calculator()
