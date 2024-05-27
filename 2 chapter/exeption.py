a = int(input("Put the first value "))
b = int(input("Put the second value "))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print('Cant divide by zero')
print('The result: ' + str(result))

