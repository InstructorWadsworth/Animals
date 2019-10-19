class Animal:

# instance method
    def __init__(self, name, age, animalType):
        self.name = name
        self.age = age
        self.animalType = animalType

    # instance method
    def hungry(self):
        return f'{self.name} is one hungry {self.animalType}'

    # static method
    @staticmethod
    def runs(speed = '2000 miles per hour'):
        return f'Your animal runs at {speed}'

