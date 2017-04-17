import os
import sys
import json
import re


with open("installations.php", 'r') as softaculousFile:
    softInstalls = softaculousFile.read().replace("\n", '')
    m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', softInstalls)
    split_arr = re.split(": |\"", softInstalls)
    for n in split_arr:
        if re.match('^\;[a-z]\:[0-9]+\:$', n):
            split_arr.remove(n)
        elif re.match('^.[a-z]', n):
            split_arr.remove(n)
    print split_arr
    for i in split_arr:
        if re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i):
            m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i)
            print m.group()
        if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i):
            n = re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i)
            print n.group()