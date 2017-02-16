def investition(amount, rate, time):
    print("Principal amount: ${} \n".format(amount))
    print("Annual interest rate: {} \n".format(rate))
    for i in range(1, time+1):
        amount += amount * rate
        print("year {}: ${}".format(i, amount))

investition(100, 0.05, 8)
investition(2000, .025, 8)
