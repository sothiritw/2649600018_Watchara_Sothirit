class Mom:
    def print(self):
        print('This is method of class mom.')

class Child(Mom):
    def print(self):
        print('This is method of class Child.')

objA = Mom()
objB = Child()

objA.print()
objB.print()




