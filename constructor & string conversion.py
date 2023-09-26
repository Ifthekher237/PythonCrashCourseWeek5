# this program shows how to use constructor(__init__()) and string conversion(__str__())

class Fruit:
    def __init__(self, fruit_name, color, taste):
        self.fruit_name = fruit_name
        self.color = color
        self.taste = taste

    def __str__(self):
        return "{fruit} is a fruit.".format(fruit=self.fruit_name)


apple = Fruit("apple", "green", "tark")
print(apple)
print(apple.color)
