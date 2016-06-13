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

#print users
#print "<br>"

uzer = users[uind]
newThing = uzer.pop(ind)
users[uind] = uzer
#print uzer
#print "<br>"
#print newThing

wryt = open('users.txt', 'w')
wryt.write(unformatit(users))
wryt.close()

raw2 = open('delUsers.txt', 'r')
dusers = formatit(raw2.readlines())
raw2.close()

#print dusers
 
def findDUserInd(user):
    for i in dusers:
        if i[0] == user:
            return dusers.index(i)


dusers[uind].append(newThing)

writ = open('delUsers.txt', 'w')
writ.write(unformatit(dusers))
writ.close()

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
                <center><input class="signlog" type="submit" value="Completed Tasks"></center>
              </div>
              <div class="column col-3u">
              </div>
            </div>
          </form>
          <form action='todo.py?user=""" + str(user) + """"'>
            <div class="row">
              <div class="column col-3u">
              </div>
              <div class="column col-6u">
                <input type="hidden" name="user" value='""" + str(user) + """'>
                <center><input class="signlog" type="submit" value="Todo List"></center>
              </div>
              <div class="column col-3u">
              </div>
              <br />
              <br />
              <br />
            </div>
          </form>
        </center>
      </div>
    </div>


  </body>
</html>
"""

print html




