class Animal:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def __str__(self):
        return f"{self.name},{self.species},{self.age} years old"



class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age,"Dog")
        self.breed=breed

    def speak(self):
        return f"{self.name} says:Woof!"

    def eat(self):
        return f"{self.name} eats the food"



class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age,"Cat")
        self.color=color

    def speak(self):
        return f"{self.name} says:Meow"

    def sleep(self):
        return f"{self.name} napping on the sofa"
dog1=Dog("Aqtos",3,"Alabai")
cat1=Cat("Poti",1,"gray")

print(dog1)
print(dog1.eat())
print(dog1.sleep())

print(cat1.sleep())