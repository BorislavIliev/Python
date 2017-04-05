from random import randint
tails = 0
heads = 0

for trials in range (0, 10000):
    if randint(0, 1) == 0:
        tails = tails + 1
    else:
        heads = heads + 1

print("tails/heads", tails, "/", heads)

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for tries in range(0, 10000):
    result = randint(1,6)
    if result == 1:
        one += 1
    elif result == 2:
        two += 1
    elif result == 3:
        three += 1
    elif result == 4:
        four +=1
    elif result == 5:
        five +=1
    elif result == 6:
        six +=1

print("Dice Rolls Results: ","\n","One: {}, Two: {}, Three: {}, Four: {}, Five: {}, Six: {} ".format(one, two, three, four, five, six))