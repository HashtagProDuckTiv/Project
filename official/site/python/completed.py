#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi,cgitb

cgitb.enable()

queerE = cgi.FieldStorage()
user = queerE['user'].value

def formatit(listt):
    for i in listt:
        listt[listt.index(i)] = i.strip()
    newJuan = []
    for i in listt:
        newJuan += [i.split(',')]
    return newJuan

raw = open('delUsers.txt', 'r')
delusers = formatit(raw.readlines())
raw.close()

def findUserInd(user):
    for i in delusers:
        if i[0] == user:
            return delusers.index(i)
        
ind = findUserInd(user)

        
html = """
<!DOCTYPE HTML>
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
      <nav id="navVertical">
        <ul>
          <li><a href='todo.py?user=""" + str(user) + """'><i class="fa fa-list-ul" aria-hidden="true"></i> &nbsp; &nbsp; &nbsp;Tasks To-Do</a></li>
          <li><a href='completed.html?user=""" + str(user) + """' class="active"><i class="fa fa-check" aria-hidden="true"></i> &nbsp; &nbsp; &nbsp;Tasks Completed</a></li>
        </ul>
      </nav>
    </header>

    <br />
    <br />
    <center><h1><i class="fa fa-check" aria-hidden="true"></i>&nbsp; &nbsp; &nbsp;Completed Tasks</h1></center>

    <!--=====================================================TABLE==========================================================-->
    <div class="row">
      <div class="column col-4u">
      </div>
      <div class="column col-8u">
        <table>
          <th>Due Date</th>
          <th>Task Name</th>
          <th>Task Description</th>"""

data = delusers[ind][2:]
for i in data:
    html += i
    
html += """</table>
      </div>
    </div>

  </body>
</html>
"""

print html
