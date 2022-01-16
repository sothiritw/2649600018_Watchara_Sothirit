def add(num1,num2):
    print("Number 1:", num1)
    print("Number 2:", num2)
    addition = num1 + num2
    return addition

def multiple(num1,num2):
    print("Number 1:", num1)
    print("Number 2:", num2)
    mul = num1 * num2
    return mul

res = multiple(2,4)
print(res)

def message():
    print("Welcome to PYnative")

message()

def course_func(name, course_name):
    print("Hello" , name, "Welcome to PYnative")
    print("Your course name is", course_name)

course_func('Benny','Python')

def calculator(a,b):
    add = a + b
    return add
res = calculator(4,6)
print("Addition :",res)


def even_odd(n):
    if n % 2 == 0:
        print('Even number')
    else:
        print('Odd Number')

even_odd(19)



