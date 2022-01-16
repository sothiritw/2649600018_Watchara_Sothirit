x = 5
def function1():
    print("Value in 1st function :",x)

def function2():
    #global x
    x = 555
    print("Value in 2st function :",x)

def function3():
    print("Value in 3st function :",x)

function1()
function2()
function3()