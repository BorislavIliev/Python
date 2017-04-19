import sys
import os
import re


usersList = []


with open('users.txt', 'r') as usersFile:
    for line in usersFile:
        newLine = line.strip('\n')
        usersList.append(newLine)

print usersList