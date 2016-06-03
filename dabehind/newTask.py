def getQuery():
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def formatTask(task):
    newTask = "<Tahseen send me this>"
    newTask += task
    newTask += "</Plssend>"

query = getQuery()

task = formatTask(query[newTask])

raw = open('index.html', r)
homepage = raw.read()
raw.close()

if newTask in q:
    before = homepage.find('</table>')
    homepage = homepage[:before] + task + homepage[before:]

taskpage = open('index.html', w)
taskpage.write(homepage)
taskpage.close()
