import os
import sys
import json
import re
import itertools

cpaneluser = 'borislav'

with open("installations.php", 'r') as softaculousFile:
    softInstalls = softaculousFile.read().replace("\n", '')
    m = re.match('^[\'"]?(?:\/[^\/]+)*[\'"]?$', softInstalls)
    split_arr = re.split(": |\"", softInstalls)
    for n in split_arr:
        if re.match('^;[a-z]\:[0-9]+\:$', n):
            print n
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
    indicesUsers = [i for i, x in enumerate(split_arr) if x == "softdbuser"]
    usersArr = []
    dbsArr = []
    passwordsArr = []
    for k in indicesUsers:
        print split_arr[k + 1]
        if cpaneluser in split_arr[k + 1]:
            usersArr.append(split_arr[k + 1])
        elif cpaneluser in split_arr[k + 2]:
                usersArr.append(split_arr[k + 2])
    indicesDbs = [i for i, x in enumerate(split_arr) if x == "softdb"]
    for k in indicesDbs:
        print split_arr[k+1]
        dbsArr.append(split_arr[k+1])
    indicesPasswords = [i for i, x in enumerate(split_arr) if x == "softdbpass"]
    for k in indicesPasswords:
        passwordsArr.append(split_arr[k+1])
        print split_arr[k+1]
    dbCollection = dict()
    for i,m,n in zip(dbsArr, usersArr, passwordsArr):
        dbCollection.update({i:{'dbuser': m, 'dbpass': n}})
    for keys in dbCollection.iteritems():
        print 'mysql -u {0}, -p {1}'.format(values['dbuser'], values['dbpass'])
    print dbCollection
