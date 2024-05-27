class Person():
    """Create a person"""

    def __init__(self, name, age, height):
        """Initialising the persons attributes"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 60

    def description_person(self):
        """Getting the persons description"""
        print(f'My name is {self.name}, my age is {self.age}, my height is {self.height}, my weight is {self.weight}')

    def get_weight(self):
        """Getting the persons weight"""
        print(f"The persons weight is {self.weight}")

    def update_weight(self, kg):
        """Changing the persons description"""
        self.weight = kg


