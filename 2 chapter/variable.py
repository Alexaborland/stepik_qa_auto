# var1 = 10  # global variable
# var2 = 20  # global variable
# print(var1, var2)
#
# def summ():
#     var1 = 30  # local variable
#     var2 = 40  # local variable
#     result = var1 + var2
#     print(result)
#
# summ()

# age = 20
# name = 'Alexa'
# if age == 25 or name == 'Alexa':
#     print('I am 25 yo')
# else:
#     print('I am not 25 yo')

pin = 1234
print('Input the pin')
user_pin = int(input())

if pin == user_pin:
    print('What a summ yo want to take?')
else:
    print('Error, you have only 2 try')
    user_pin = int(input())
    if pin == user_pin:
        print('What a summ yo want to take?')
    else:
        print('Error, you have only 1 try')
        user_pin = int(input())
        if pin == user_pin:
            print('What a summ yo want to take?')
        else:
            print('You card is blocked')