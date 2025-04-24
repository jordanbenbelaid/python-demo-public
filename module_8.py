class Person:
    def __init__(self, age: int, name: str, wears_glasses: bool):
        self.age = age
        self.name = name
        self.wears_glasses = wears_glasses
        
    def speak(self):
        print(self.name + " says hi!")
        
        
person_one = Person(28, "Jordan", True)
person_two = Person(25, "Sarah", False)

person_one.speak()
person_two.speak()

print(person_one.name + " is " + str(person_one.age) + " and it is " 
      + str(person_one.wears_glasses) + " they wear glasses")

print(f"{person_one.name} is {person_one.age} and it is {person_one.wears_glasses} they wear glasses")

print(person_two.name + " is " + str(person_two.age) + " and it is " 
      + str(person_two.wears_glasses) + " they wear glasses")

people = [person_one, person_two]