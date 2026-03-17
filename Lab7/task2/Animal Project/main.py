from models import Animal,Dog,Cat

def main():
    animal1=Animal("aq qagaz",6,"horse")
    dog1=Dog("Qytzhol",3,"Labrador")
    cat1=Cat("Tompi",4,"white")

    animals=[animal1,dog1,cat1]

    for a in animals:
        print(a)
        print(a.eat())
        print(a.sleep())
        if isinstance(a,Dog):
            print(a.speak())
        elif isinstance(a,Cat):
            print(a.speak())



if __name__=="__main__":
    main()