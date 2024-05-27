class Person():
    """Create a person"""

    def __init__(self, name, age, height):
        """Initialising the persons attributes"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Getting the persons description"""
        print(f'My name is {self.name}, my age is {self.age}, my height is {self.height}, my weight is {self.weight}')

    def get_weight(self):
        """Getting the persons weight"""
        print(f"The persons weight is {self.weight}")

    def update_weight(self, kg):
        """Changing the persons description"""
        self.weight = kg


# man = Person("Alexa", 26, 175)
# man.description_person()
# man.update_weight(110)
# man.get_weight()


class Warrior(Person):
    """Create a class warrior"""

    def __init__(self, name, age, height):
        """Initialising the warrior attributes"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Getting the charge of rage"""
        print(f"The charge of rage is {str(self.rage)}")

    def description_warrior(self):
        """Redefinition of the parent method"""
        # print(f'His is {self.name}, his age is {self.age}, his charge of rage is {str(self.rage)}')
        description = f'He is {self.name}, his age is {self.age}, his charge of rage is {str(self.rage)}'
        return description


warrior = Warrior("Connan", 32, 200)
print(f'New person is : {warrior.description_warrior()}')
# warrior.get_rage()
# warrior.description_warrior()
# warrior.update_weight(150)
# warrior.description_person()
