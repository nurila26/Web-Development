class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def __str__(self):
        return f"{self.name}, {self.species}, {self.age} years old"



class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed
    def speak(self):
        return f"{self.name} says: Woof!"

    def eat(self):
        return f"{self.name} the dog is munching on dog food."

    class Cat(Animal):
        def __init__(self, name, age, color):
            super().__init__(name, age, "Cat")
            self.color = color

        def speak(self):
            return f"{self.name} says: Meow!"

        def sleep(self):
            return f"{self.name} the cat is napping on the sofa."


dog1 = Dog("Rex", 3, "Labrador")
cat1 = Cat("Whiskers", 2, "Gray")

print(dog1)
print(dog1.eat())
print(dog1.speak())

print(cat1.sleep())
print(cat1.speak())