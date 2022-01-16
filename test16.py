class Father:
    def __init__(self):
        print('I have 5 acres of land.')
    def printF(self):
        print('===== Benny ======')

class Mother:
    def __init__(self):
        print('I have 2 houses.')

class Son(Father,Mother):
    def __init__(self):
        print('I have 40000 bath of money.')
        Father.__init__(self)
        Mother.__init__(self)

s = Son()
