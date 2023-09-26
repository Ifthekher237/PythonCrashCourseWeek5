"""
# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

def exchange_apples(you, me):
	# Here, despite G.B. Shaw's quote, our characters have started with
	#different amounts of apples so we can better observe the results.
	# We're going to have Martin and Johanna exchange ALL their apples with #one another.
	# Hint: how would you switch values of variables,
	# so that "you" and "me" will exchange ALL their apples with one another?
	# Do you need a temporary variable to store one of the values?
	# You may need more than one line of code to do that, which is OK.
	temp = you.apples
	you.apples = me.apples
	me.apples = temp
	return you.apples, me.apples


def exchange_ideas(you, me):
	# "you" and "me" will share our ideas with one another.
	# What operations need to be performed, so that each object receives
	# the shared number of ideas?
	# Hint: how would you assign the total number of ideas to
	# each idea attribute? Do you need a temporary variable to store
	# the sum of ideas, or can you find another way?
	# Use as many lines of code as you need here.
	sum = you.ideas + me.ideas
	you.ideas = sum

	me.ideas = sum

	return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
"""
'''
class Piglet:
    def speak(self):
        print("oink oink")

hamlet = Piglet()
hamlet.speak()

'''
'''
class Piglet:
    name = ""
    def speak(self):
        print("oink! i am {} oink!".format(self.name))


hamlet = Piglet()
hamlet.name = "ifth"
hamlet.speak()
'''

'''

class Calculator:
    number = 0
    numerator = 0
    denominator = 1
    def __init__(self,number, numerator, denominator):
        self.number = number
        self.numerator = numerator
        self.denominator = denominator

    def sum(self):
        result = 0
        for i in range(self.number + 1):
            result += i
        return result

    def multiply(self):
        result = 1
        for i in range(1, self.number + 1):
            result *= i
        return result

    def divison(self):
        if self.denominator == 0:
            return "denominator should be greater than zero!"
        else:
            return self.numerator / self.denominator

test = Calculator(3,0,0)
print(test.sum())
test = Calculator(3,0,0)
print(test.divison())




class Print_name:
    name = ""

    def prints_the_name(self):
        return "hi! my name is {}.".format(self.name)


ifthekher = Print_name()
ifthekher.name = "ifthekher"


class Piglet:
    name = "hamlet"  # OR name = "" OR any other strings can be used to initialize the name attribute

    def speak(self):
        print("oink! i am {}. oink!".format(self.name))


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

name2 = str("ifthekher")
print(name2)
'''
'''
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("ifthekher")
# Call the greeting method
print(some_person.greeting())
'''
'''
class Info:
    name = ""
    city= ""
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def luckyno(self):
        lucky_no = len(self.name)*7
        return lucky_no


me = Info("ifthekher","chittagong")

print("hi {}, you are from {}, your lucky number is {}".format(me.name, me.city, me.luckyno()))

'''

'''
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavour is {}.".format(self.color, self.flavor)
'''
"""
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass


granny_smith = Apple("green", "tark")
carnelian = Grape("purple", "sweet")

print(granny_smith.color)
print(carnelian.flavor)
"""
"""
class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} i am {name}! {sound}".format(sound = self.sound, name = self.name))

class Piglet(Animal):
    sound ="oink!"

hamlet = Piglet("hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "moooooo!"

milky = Cow("milky white")
milky.speak()
"""

"""
class Clothing:
    material = ""
    def __init__(self,name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))
class Shirt(Clothing):
    material="Cotton"
polo = Shirt("Polo")
polo.checkmaterial()
"""
"""



class Fruit:
    color = ""
    flavor = ""

    def __str__(self):
        return "your fruit is {color} coloured and it tastes {taste}.".format(color=self.color, taste=self.flavor)


class Apple(Fruit):
    pass


apple = Apple()
apple.color = "green"
apple.flavor = "tark"
print(apple)

print(apple.color)
print(apple.flavor)

"""
"""

import datetime
now = datetime.datetime.now()
print(type(now))
print(now)
print(now.year)
print(now+datetime.timedelta(days=2))
"""

"""
Let’s expand a bit on our Clothing classes from the previous in-video question. 
Your mission: Finish the "Stock_by_Material" method and iterate over the amount of 
each item of a given material that is in stock. When you’re finished, 
the script should add up to 10 cotton Polo shirts.



class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}
    material = ""

    def __init__(self, name):
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):  # shirt class inherits from Clothing class
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

Nice job! You successfully used composition to reuse the
Clothing.stock attribute and stock_by_material() function of
the Clothing class to take stock of the Cotton shirts!
"""
"""
class Test:
    list = []
    def __init__(self, a, b):
        Test.list.append(a)
        Test.list.append(b)
    def rint(self):
        return Test.list

test = Test(1,2)
print(test.rint())
"""
"""



class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

#Turtle = Turtle("turtle")
#print(Turtle.category)

class Snake(Animal):
    category = "reptile"


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category
"""
class Count:
    sum = 0
    called = 0
    def total(self, a):
        self.called += 1
        self.sum += a
        print(self.sum)

    def call(self):
        return self.called

test = Count()
test.total(2)
test.total(2)
print(test.call())

