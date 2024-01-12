class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the base class (Animal)
        super().__init__(name, sound="Woof")
        self.breed = breed

    def wag_tail(self):
        print(f"{self.name} is wagging its tail")

class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the base class (Animal)
        super().__init__(name, sound="Meow")
        self.color = color

    def purr(self):
        print(f"{self.name} is purring")

# Example usage:
dog_instance = Dog(name="Buddy", breed="Golden Retriever")
cat_instance = Cat(name="Whiskers", color="Calico")

# Use methods and attributes specific to each subclass
dog_instance.make_sound()
dog_instance.wag_tail()

cat_instance.make_sound()
cat_instance.purr()
