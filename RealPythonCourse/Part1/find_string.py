"""How to find a string in another string:
The method find searches for the string
and prints the starting position, if anything is found.
If there is no match, it will return -1.
It returns the position of the first occurance only.
"""

phrase = "the surprise is somewhere here"
print(phrase.find("surprise"))
print("yet another surprise".find("another"))

#replacing a string
speech = "He spoke the truth!"
print(speech.replace("the truth", "lies"))

userline = input()
print(userline.find("a"))
