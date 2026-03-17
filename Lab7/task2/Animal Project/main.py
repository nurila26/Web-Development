from models import Animal, Dog, Cat

def main():
    animal1 = Animal("Buddy", 5, "Generic Animal")
    dog1 = Dog("Rex", 3, "Labrador")
    cat1 = Cat("Whiskers", 2, "Gray")

    animals = [animal1, dog1, cat1]

    for a in animals:
        print(a)
        print(a.eat())
        print(a.sleep())
        if isinstance(a, Dog):
            print(a.speak())
        elif isinstance(a, Cat):
            print(a.speak())
        print("-" * 40)

if __name__ == "__main__":
    main()