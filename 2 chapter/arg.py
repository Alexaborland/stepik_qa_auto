# def identification(name):
#     print("You are")
#
#     if name == 'Alexa':
#         print('Autor')
#
#     else:
#         print('Student')
#
# name = input('Put your name')
# identification(name)


# def identification(name):
#     print("You are")
#
#     if name == 'Alexa':
#         result = 'Author'
#
#     else:
#         result = 'Student'
#
#     return result
# name = input('Put your name')
# # print(identification(name))
# n = 'Alexa '
# s = identification(name)
# print(n + s)

def identification(name):
    print("You are")

    if name == 'Alexa':
        result = 'Author'

    else:
        result = 'Student'

    return result

def status(result):
    print(result)

name = input('Put your name')
status(identification(name))