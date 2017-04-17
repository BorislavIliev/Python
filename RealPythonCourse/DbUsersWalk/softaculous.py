import os
import sys
import json
import re


with open("installations.php", 'r') as softaculousFile:
    softInstalls = softaculousFile.read().replace("\n", '')
    m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', softInstalls)
    split_arr = re.split(": |\"", softInstalls)
    print split_arr
    print type(split_arr)
    for i in split_arr:
        if re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i):
            m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', i)
            print m.group()
        if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i):
            n = re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i)
            print n.group()