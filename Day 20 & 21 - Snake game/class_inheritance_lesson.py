# non-related to project
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, exhale')


class Fish(Animal):
    def __init__(self):     # inheritance
        super().__init__()

    def swim(self):
        print('pływu pływu')

    def breathe(self):      # modifying inherited method
        super().breathe()
        print('... underwater ...')


nemo = Fish()
nemo.breathe()
