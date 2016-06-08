#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

raw = open('../todo.html', 'r')
homepage = raw.read()
raw.close()

before = homepage.rfind('<!-- Here -->')
after = homepage.find('</table>')
homepage = homepage[:before] + homepage[after:]
print homepage

taskpage = open('../todo.html', 'w')
taskpage.write(homepage)
taskpage.close()
#print homepage

print "<a href='../todo.html'>Tasks have been cleared! Click here to return to the main site</a>"
