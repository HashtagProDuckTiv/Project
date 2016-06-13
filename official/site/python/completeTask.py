#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb

cgitb.enable()

def getQuery():
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def formatit(listt):
    for i in listt:
        listt[listt.index(i)] = i.strip()
    newJuan = []
    for i in listt:
        newJuan += [i.split(',')]
    return newJuan

def unformatit(listt):
    newJuan = ""
    for i in listt:
        newJuan += ','.join(i)
        newJuan += '\n'
    return newJuan

def findUserInd(user):
    for i in users:
        if i[0] == user:
            return users.index(i)

raw = open('users.txt', 'r')
users = formatit(raw.readlines())
raw.close()

query = getQuery()
user = query['user']
ind = int(query['ind'])
uind = findUserInd(user)

print users
print "<br>"

uzer = users[uind]
newThing = uzer.pop(ind)
users[uind] = uzer
print uzer
print "<br>"
print newThing

wryt = open('users.txt', 'w')
wryt.write(unformatit(users))
wryt.close()

raw2 = open('delUsers.txt', 'r')
dusers = formatit(raw2.readlines())
raw2.close()

print dusers
 
def findDUserInd(user):
    for i in dusers:
        if i[0] == user:
            return users.index(i)

udind = findDUserInd(user)
dusers[udind].append(newThing)

writ = open('delUsers.txt', 'w')
writ.write(unformatit(dusers))
writ.close()







