from person_base import *
from selenium import webdriver

man = Person("Alexa", 26, 175)
man.description_person()
warrior = Warrior("Connan", 32, 200)
print(f'New person is : {warrior.description_warrior()}')

# import person_base
#
#
# man = person_base.Person("Alexa", 26, 175)
# man.description_person()
# warrior = person_base.Warrior("Connan", 32, 200)
# print(f'New person is : {warrior.description_warrior()}')
