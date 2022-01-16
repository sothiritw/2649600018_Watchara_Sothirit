def addition(*numbers):
    total = 0
    for no in numbers:
        total = total + no
    print("Sum is:", total)

addition()
addition(10,5,2,5,4)
addition(78,7,2.5)