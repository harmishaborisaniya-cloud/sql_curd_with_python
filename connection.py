import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="harmi@2510")
print(mydb," connection is ohkk done")