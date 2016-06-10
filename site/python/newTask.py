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
query = getQuery()

raw = open('../todo.html', 'r')
homepage = raw.read()
raw.close()

button = '<input class="taskremove" type="submit" value=complete'


def formatTask():
    newTask = "<tr>\n"
    newTask += "\t\t <td>" + str(query['dueDate']) + "</td>\n"
    newTask += "\t\t <td>" + str(query['taskName']) + "</td>\n"
    newTask += "\t\t <td>" + str(query['taskDescription']) + "</td>\n"
    newTask +="\t\t<td>"
    newTask += '\t\t<form name="completeTask" method="GET" action="python/completeTask.py">'
    newTask += button
    newTask += '\t\t</form>'
    newTask += '\t\t</td>'
    newTask += "\t</tr>\n"
    return newTask

#print "<pre>" + homepage + "</pre>"

code = formatTask()
#print code


before = homepage.find('<!-- Here -->')
homepage = homepage[:before] + code + homepage[before:]
#print homepage

taskpage = open('../todo.html', 'w')
taskpage.write(homepage)
taskpage.close()

print "<a href='../todo.html'>Task Successfully added! Click here to return to the main site</a>"
