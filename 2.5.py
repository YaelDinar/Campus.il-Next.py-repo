#task 2.5 from chapter 2

#Animal super class
class Animal():

    #the name of the zoo a value that should be accessible for all Animal objects and sub-objects
    zoo_name = "Hayaton"

    #initialize of Animal with default hunger that is 0
    def __init__(self, name, hunger = 0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        function to get an animal's name
        :return: the animal's name
        :rtype: string
        """
        return self._name

    def is_hungry(self):
        """
        A function that return if an anumal is hungry (if the value of it's hungry is above 0)
        :return: if the animal is hungry
        :rtype: boolean
        """
        return self._hunger > 0

    def feed(self):
        """
        a function to feed the animal (make it less hungry)
        :return: the function subs 1 from the hunger value of an animal
        :rtype: None
        """
        self._hunger -= 1

    def talk(self):
        pass

#sub class that extends Animal
class Dog(Animal):
    def talk(self):
        """
        a function that prints a specific dog talk
        :rtype: None
        """
        print("woof woof")

    def fetch_stick(self):
        """
        a special dog function for fetching a stick and prints it's reaction
        :rtype: None
        """
        print('There you go, sir!')

#sub class that extends Animal
class Cat(Animal):
    def talk(self):
        """
        a function that prints a specific cat talk
        :rtype: None
        """
        print("meow")

    def chase_laser(self):
        """
        a special cat function for chasing laser and prints it's reaction
        :rtype: None
        """
        print("Meeeeow")

#sub class that extends Animal
class Skunk(Animal):
    def __init__(self, name, hunger = 0, stink_count = 6):
        """
        initiolize of a skunk
        :param Name: the name of the skunk
        :type: string
        :param Hunger: the hunger level of the skunk
        :type: int
        :param stink_count: it's stink count, default : 6
        :type: int
        """
        #call the super class (animal) initiolize
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        a function that prints a specific skunk talk
        :rtype: None
        """
        print("tsssss")

    def stink(self):
        """
        a special skunk function for stinking and prints a reaction
        :rtype: None
        """
        print("Dear Lord!")

#sub class that extends Animal
class Unicorn(Animal):
    def talk(self):
        """
        a function that prints a specific unicorn talk
        :rtype: None
        """
        print("Good day, darling")

    def sing(self):
        """
        a special unicorn function for singing and prints it's singing
        :rtype: None
        """
        print("I'm not yout toy...")

#sub class that extends Animal
class Dragon(Animal):
    def __init__(self, name, hunger = 0, color = 'Green'):
        """
        initiolize of a dragon
        :param Name: the name of the dragon
        :type: string
        :param Hunger: the hunger level of the dragon
        :type: int
        :param color: the dragons color default: Green
        :type: string
        """
        #call the super class (animal) initiolize
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        a function that prints a specific unicorn talk
        :rtype: None
        """

        print("Raaaawr")

    def breath_fire(self):
        """
        a special dragon function for fire breathing and prints it's sound
        :rtype: None
        """
        print("$@#$#@$")

def main():

    #a list of the zoo animals
    zoo_lst = zoo_lst = (
        Dog('Brownie', 10), Cat('Zelda', 3), Skunk('Stinky', 0),
        Unicorn('Keith', 7), Dragon('Lizzy', 1450),
        Dog('Doggo', 80), Cat('Kitty', 80), Skunk('Stinky Jr.', 80),
        Unicorn('Clair', 80), Dragon('McFly', 80)
    )

    #for each animal if it's hungry feed it until it's full
    for animal in zoo_lst:
        if animal.is_hungry():
            print( f'{type(animal).__name__}: ' + animal.get_name() + " is hungry. let's feed it!")
            while animal.is_hungry():
                animal.feed()

        #make each animal animal talk
        animal.talk()

        #run the special function for each sun animal
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    #print the zoo's name
    print(Animal.zoo_name)

if __name__ == "__main__":
    main()
