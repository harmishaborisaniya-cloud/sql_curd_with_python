import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="harmi@2510",database="Learncoding")
db_cursor=mydb.cursor()
# db_cursor.execute("create table Emp(roll int,Ename varchar(20))")#creat table
# print("table is created....")
db_cursor.execute("show tables")# to show all tables in database 
for i in db_cursor:
    print(i)

