from person_base import Person


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
