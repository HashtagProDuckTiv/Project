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

def formatTask():
    newTask = "<tr>\n"
    newTask += "\t\t <td>" + str(query['dueDate']) + "</td>\n"
    newTask += "\t\t <td>" + str(query['taskName']) + "</td>\n"
    newTask += "\t\t <td>" + str(query['taskDescription']) + "</td>\n"
    newTask += """\t\t<td>
              <form name="completeTask" method="GET" action="python/completeTask.py">
                <input class="taskremove" type="submit" value="Completed">
              </form>
            </td>"""
    newTask += "\t</tr>\n"
    return newTask

code = formatTask()

raw = open('../todo.html', 'r')
homepage = raw.read()
raw.close()

before = homepage.find('</table>')
homepage = homepage[:before] + code + homepage[before:]
#print homepage

taskpage = open('../todo.html', 'w')
taskpage.write(homepage)
taskpage.close()

print "<a href='../todo.html'>Task Successfully added! Click here to return to the main site</a>"
