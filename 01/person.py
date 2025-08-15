class Person:
    def __init__(self, name, height, age, weight):
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight

    def get_bmi(self):
        return self.weight / (self.height ** 2)

    def is_legal_age(self):
        return self.age >= 21