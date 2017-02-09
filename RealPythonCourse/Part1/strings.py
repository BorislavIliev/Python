long_phrase = """This is a long line
that spans accross multiple lines
preserving white spaces"""

long_phrase_length = len(long_phrase)

my_long_string = "Here's a string that I want to \
write across multiple lines since it is long."

double_quotes_string = 'This string contains "double quotes".'

apostrophe_string = "This string contains an 'apostrophe."

#Concatenating strings
string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2

print(long_phrase)
print(my_long_string)
print(double_quotes_string)
print(apostrophe_string)
print("The length of long_phrase is {0}".format(long_phrase_length))
print(magic_string)

#print single char from string
print(string1[0])
#string slicing and dicing
flavor = "birthday cake"
print(flavor[:5])
print(flavor[5:])
print(flavor[:])

#changing character in string
#Strings are immutable, so we have to create a new string, i.e. reassign it.
my_string = "goal"
print(my_string)
my_string = "f" + my_string[1:]
print(my_string)

#cut a part of a string
#from char 2(the third, beginning from 0), to BUT NOT INCLUDING char 6.
zing = "bazinga"
print(zing[2:6])

#convert to UPPER
loud_voice = "Can you hear me yet?"
print(loud_voice.upper())
