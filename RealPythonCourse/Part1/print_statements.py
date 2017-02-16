name = "Zaphod"
num_heads = 2
num_arms = 3

#string interpolation
print(name, "has", str(num_heads), "heads and", str(num_arms), "arms")

#second way, using + sign
print(name+" has "+str(num_heads)+" heads and "+str(num_arms)+" arms")

#using the format() method
print("{} has {} heads and {} arms".format(name, num_heads, num_arms))

print("{name} has {num_heads} heads and {num_arms} arms".format(
    name="Zaphod", num_heads=2, num_arms=3
))

#the str method transforms the value into a string
weight = 0.2
animal = "newt"
print(str(weight), "kg is the weight of", str(animal))
print("{} ks is the weight of {}".format(weight, animal))
print("{1} ks is the weight of {0}".format(animal, weight))

#assign variables inside the format method
print("{kilo} kg is the weight of {the_animal}".format(kilo = 0.3, the_animal = "dog"))
