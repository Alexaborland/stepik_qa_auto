

# login = input('Put your login: ')
#
# while True:
#     if '@' in login:
#         print('The login is valid')
#         password = input('Put your password')
#     else:
#         print('The login is invalid')
#         break
#
# numbers = [1, 3, 158, 7, 58]
# for i in numbers:
#     if i == 7:
#         print('Its 7')
#         break
#     elif i == 3:
#         print('Its 3')
#     elif i == 158:
#         print('Its 158')
#         continue
#     print(i)

# file = open('file.txt', 'w')
# file.write('Hello, my name is Alexa!\n')
# file.close()
#
# file = open('file.txt', 'r')
# read_file = file.read()
# file.close()
# print(read_file)

var = input('Put something here: ')
file_write = open('file.txt', 'a')
file_write2 = file_write.write('\n' + var)
file_write.close()
