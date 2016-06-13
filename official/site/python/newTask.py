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


"""
Format of the data in each column
<tr>
         <td>Due Date</th>
          <td>Task Name</td>
          <td>Task Description</td>
          <td>Remove</th>
</tr>
"""


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

query = getQuery()
user = query['user']

def findUserInd(user):
    for i in users:
        if i[0] == user:
            return users.index(i)
        

raw = open('users.txt', 'r')
users = formatit(raw.readlines())
raw.close()

user = query['user']
date = str(query['dueDate']) 
name = str(query['taskName'])
descrip = str(query['taskDescription'])
tableD = users


ind = findUserInd(user)
tabl = '<tr><td>'
tabl += str(date)
tabl += '</td><td>'
tabl += str(name)
tabl +='</td><td>'
tabl += str(descrip)
tabl += "</td>"
users[ind]+= [tabl]
#print tabl
#print "<br>"
#print "<users>"

users = unformatit(users)

form =  '<form action="todo.py">'
form += '<input type="hidden" name="user" value=' + str(user) + '>'
form += '<input type="submit" value="Click to Return to the main site.">'
form += '</form>'

print form

wryt = open('users.txt', 'w')
wryt.write(users)
wryt.close()


