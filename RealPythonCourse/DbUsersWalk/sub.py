import re

with open("installations.php", 'r') as softaculousFile:
    softInstalls = softaculousFile.read().replace("\n", '')
    m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', softInstalls)
    split_arr = re.split(": |\"", softInstalls)
    for n in split_arr:
        if re.match('^;[a-z]\:[0-9]+\:$', n):
            print n