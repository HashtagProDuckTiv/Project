#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi

queerE = cgi.FieldStorage()
user = queerE['user'].value
html ="""<!DOCTYPE HTML>
<html>
  <head>
    <title>ProDuckTiv</title>
    <link rel="stylesheet" href="css/fluidgrid.css" />
    <link rel="stylesheet" href="css/main.css" />
    <link rel="stylesheet" href="css/navigation.css" />
    <link rel="stylesheet" href="css/font-awesome.min.css" />
  </head>

  <body>
    <header>
      <nav id="navHorizontal">
        <ul>
          <li class="logo"><a href="index.html"><h1>ProDuckTiv</h1></a></li>
          <li class="loginbutton"><a href="login.html" class="navButton"><i class="fa fa-sign-in" aria-hidden="true"></i>&nbsp; &nbsp;Login</a></li>
          <li class="loginbutton"><a href="signup.html" class="navButton" class="active"><i class="fa fa-user-plus" aria-hidden="true"></i>&nbsp; &nbsp;Sign Up</a></li>
        </ul>
      </nav>
      <nav id="navVertical">
        <ul>
          <li><a href="#" class="active"><i class="fa fa-list-ul" aria-hidden="true"></i> &nbsp; &nbsp; &nbsp;Tasks To-Do</a></li>
          <li><a href="completed.html"><i class="fa fa-check" aria-hidden="true"></i> &nbsp; &nbsp; &nbsp;Tasks Completed</a></li>
          <li><a href="calendar.html"><i class="fa fa-calendar" aria-hidden="true"></i> &nbsp; &nbsp; &nbsp;Calendar</a></li>
        </ul>
      </nav>
    </header>

<!--=====================================================NEW TASK FORM=======================================================-->
    <div class="row">
      <div class="column col-4u">
      </div>
      <div class="column col-8u">
        <form name="newTask" method="GET" action="python/newTask.py?=">
        <input type="hidden" name="user" value=""" + str(user) + """>
          <center><h1><i class="fa fa-pencil" aria-hidden="true"></i>&nbsp; &nbsp; &nbsp;New Task</h1></center>
          <div class="row">
            <div class="column col-6u">
              <input id="name" type="text" name="taskName" placeholder="Task Name" />
            </div>
            <div class="column col-6u">
              <input id="name" type="text" name="dueDate" placeholder="Due Date MM/DD/YYYY" />
            </div>
            <br />
            <br />
            <br />
            <div class="column col-12u">
              <textarea id="description" type="textarea" name="taskDescription" placeholder="Enter your task here..."></textarea>
            </div>
          </div>
          <div class="row">
          </div>
            <center><input class="taskadd" type="submit" value="Submit"></center>
        </form>
      </div>
    </div>

    <!--=====================================================TABLE==========================================================-->
   <div class="row">
      <div class="column col-4u">
      </div>
      <div class="column col-8u">
        <br />
        <br />
        <table>
          <th>Due Date</th>
          <th>Task Name</th>
          <th>Task Description</th>
          <th>Remove</th>
          <tr>
            <td>Test</td>
            <td>Test</td>
            <td>Test</td>
            <td>
              <form name="completeTask" method="GET" action="python/completeTask.py">
                <input class="taskremove" type="submit" value="Completed">
              </form>
	     </table>
      </div>
    </div>


  </body>
</html>"""

print html
