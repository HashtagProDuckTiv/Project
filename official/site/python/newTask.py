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

wryt = open('users.txt', 'w')
wryt.write(users)
wryt.close()

html="""<!DOCTYPE HTML>
<html>
  <head>
    <title>ProDuckTiv</title>
    <link rel="stylesheet" href="../css/fluidgrid.css" />
    <link rel="stylesheet" href="../css/main.css" />
    <link rel="stylesheet" href="../css/navigation.css" />
    <link rel="stylesheet" href="../css/font-awesome.min.css" />
  </head>

  <body>
    <header>
      <nav id="navHorizontal">
        <ul>
          <li class="logo"><a href="../index.html"><h1>ProDuckTiv</h1></a></li>
          <li class="loginbutton"><a href="../login.html" class="navButton"><i class="fa fa-sign-in" aria-hidden="true"></i>&nbsp; &nbsp;Login</a></li>
          <li class="loginbutton"><a href="../signup.html" class="navButton" class="active"><i class="fa fa-user-plus" aria-hidden="true"></i>&nbsp; &nbsp;Sign Up</a></li>
        </ul>
      </nav>
    </header>

    <!--=========================BANNER============================-->

    <div class="row">
      <div class="column col-2u">
      </div>
      <div class="column col-10u">
        <center>
          <form action='completed.py?user=""" + str(user) + """'>
            <div class="row">
              <div class="column col-3u">
              </div>
              <div class="column col-6u">
                <input type="hidden" name="user" value='""" + str(user) + """'>
                <center><input class="signlog" type="submit" value="Back to To-Do"></center>
              </div>
              <div class="column col-3u">
              </div>
            </div>
          </form>
        </center>
      </div>
    </div>
  </body>
</html>
"""

print html



