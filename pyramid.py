class Pyramid:

    def upper(self, row):
        """prints a normal pyramid"""
        space = row
        j = 0
        while space >= 0:
            for i in range(space):
                print(" ", end="")

            for k in range(2 * j + 1):
                print("*", end="")
            print()
            space -= 1
            j += 1

    def lower(self, row):
        """prints a pyramid with downside up and upside down"""
        space = 0
        j = row
        while space <= row:
            for i in range(space):
                print(" ", end="")

            for k in range(2 * j + 1):
                print("*", end="")
            print()
            space += 1
            j -= 1

test = Pyramid()
test.lower(4)







