try:
    var = int(input())
except ValueError:
    print('That was not integer')


def divide(num1, num2):
    try:
        division = num1 / num2
        print(division)
    except(TypeError, ZeroDivisionError):
        print('Operation not possible')

divide(10, 5)
divide(10, 0)
divide('a', 3)
