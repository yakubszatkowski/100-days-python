class Animal:
    def __init__(self, name, species):
        self.sound = None
        self.name = name
        self.species = species

    def make_sound(self):
        print(f'{self.sound}')


class Lion(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.sound = '*Roar!*'


class Elephant(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.sound = '*Trumpet!*'


class Snake(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.sound = '*Hiss!*'


lion = Lion('John', 'Panthera leo')
elephant = Elephant('Roger', 'Loxodonta africana')
snake = Snake('Michael', 'Python regius')

lion.make_sound()
elephant.make_sound()
snake.make_sound()
