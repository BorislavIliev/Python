def celcius_to_fahrenheit(temp_c):
    temp_f = (temp_c * 9/5 + 32)
    return ("{0} degrees celcius = {1} degrees fahrenheit".format(temp_c, temp_f))

def fahrenheit_to_celcius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return ("{0} degrees fahrenheit = {1} degrees celcius".format(temp_f, temp_c))

print(celcius_to_fahrenheit(20))
print(fahrenheit_to_celcius(105))
