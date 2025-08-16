import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="harmi@2510")
db_cursor=mydb.cursor()
db_cursor.execute("create database Learncoding")

print("database craeted....")