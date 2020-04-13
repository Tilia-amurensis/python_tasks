class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
harry = Animal('hipogrif', 6, 'pink')
import copy
harry = Animal('hipogrif', 6, 'pink')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)

harry = Animal('hipogrif', 6, 'pink')
carrie = Animal('cat', 4, 'grey')
bobr = Animal('dog', 4, 'white')
my_animals = [harry, carrie, bobr]
more_animals = copy.copy(my_animals)
my_animals[2].species = 'vampir'
animals_lenth = len(my_animals)
for concret_animal in my_animals:
    print(' parametrs are: %s, %s, %s' % (concret_animal.species, concret_animal.number_of_legs, concret_animal.color))
sally = Animal('parrot', 2, 'green')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'dragon'
print(my_animals[0].species)
print(more_animals[0].species)

class Car:
    pass
carl=Car()
carl.wheels = 4
car2=carl
car2.wheels = 3
print(carl.wheels)

car3 = copy.copy(carl)
car3.wheels = 6
print(carl.wheels)

