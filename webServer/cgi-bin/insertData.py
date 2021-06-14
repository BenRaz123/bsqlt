#!/usr/bin/env python3
import psycopg2
import cgi, cgitb
import datetime

conn = psycopg2.connect(
    host="localhost",
    database="usercolors",
    user="postgres"
)

#New Stuff
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
userName = form.getvalue('userName')
userColor  = form.getvalue('userColor')
curDate = str(datetime.date.today())
cur = conn.cursor()
# execute the INSERT statement
sqlStr= "INSERT INTO userInfo (username, color, entryDate) VALUES ('"+userName+"', '"+userColor+"', '"+curDate+"');"
cur.execute(sqlStr)
# commit the changes to the database
conn.commit()
# close communication with the database



print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Your Choices Are: %s %s %s</h2>" % (userName, userColor, curDate))

print('<table>')
cur.execute('SELECT * FROM userInfo;')
mobile_records = cur.fetchall() 

for row in mobile_records:
    print('<tr><td>'+row[0]+'</td><td>'+row[1]+'</td><td>'+str(row[2])+'</td></tr>')

print('</table>')
print ("</body>")
print ("</html>")
print("")



cur.close()

