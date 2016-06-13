def formatit(listt):
    for i in listt:
        listt[listt.index(i)] = i.strip()
    newJuan = []
    for i in listt:
        newJuan += [i.split(',')]
    return newJuan

raw = open('users.txt', 'r')
users = formatit(raw.readlines())
#print raw.read()
raw.close()

def findUserInd(user):
    for i in users:
        if i[0] == user:
            return users.index(i)

user = 'deez'
html = "<table>"
data = users[findUserInd(user)][2:]
print data
for i in data:
    html += i
print html


"""
user = 'AAbbas'
#print users
        

raw = open('users.txt', 'r')
users = formatit(raw.readlines())
raw.close()
print users

date = '5/10/15'
name = 'doDis'
descrip = 'i wanna do dis'

#users[findUserInd(user)] += [[date, name, descrip]]


#users[0] = ["this is some stuff"] + users[0]
#print users
def unformatit(listt):
    newJuan = ""
    for i in listt:
        newJuan += ','.join(i)
        newJuan += '\n'
    return newJuan
#print ""
#print unformatit(users)
    

#wryt = open('users.txt', 'w')
#wryt.write(users)
"""
