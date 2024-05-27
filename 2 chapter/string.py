str1 = 'Bang Chan'
print(dir(str1))  # dir shows what function we can apply
print(str1.upper())  # upper for up case
print(str1.title())  # upper case for the first character
print(str1.lower())  # lower case for every character


name = 'Jeongin'
a = 'Hello, {}!'
result = a.format(name)
print(result)

result2 = f'Hello, {name}'
print(result2)