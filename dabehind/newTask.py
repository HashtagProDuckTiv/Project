def getQuery():
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d


"""
<tr>
         <td>Due Date</th>
          <td>Task Name</th>
          <td>Task Description</th>
          <td>Remove</th>
</tr>
"""
query = getQuery()

def formatTask():
    newTask = <tr>
    newTask += <td> + str(query[dueDate]) + </td>
    newTask += <td> + str(query[taskName]) + </td>
    newTask += <td> + str(query[taskDescription]) + </td>
    return newTask

code = formatTask()

raw = open('index.html', r)
homepage = raw.read()
raw.close()

before = homepage.find('</table>')
homepage = homepage[:before] + code + homepage[before:]

taskpage = open('index.html', w)
taskpage.write(homepage)
taskpage.close()
