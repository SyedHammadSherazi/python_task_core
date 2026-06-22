# Inheritance: an Animal parent class, with Dog and Cat child classes that print their
# sound. 
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)
    def info(self):
        print("Animal name:", self.name)
class Dog(Animal):
    def sound(self):
        print(self.name, "barks")
class Cat(Animal):
    def sound(self):
        print(self.name, "Meo")
do = Dog("Dog")
ca =Cat("Cat")
do.info()     
do.sound()
ca.info()
ca.sound()