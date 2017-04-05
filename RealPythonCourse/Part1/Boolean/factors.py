var = input()
var_int = int(var)
for i in range(1, var_int):
    if var_int % i == 0:
        print(i, 'is a divisor of',var_int)
