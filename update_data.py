import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="harmi@2510",database="Learncoding")
db_cursor=mydb.cursor()
db_update="update Emp set roll=%s where Ename=%s"
db_value=(5,"Shubham")
db_cursor.execute(db_update,db_value)
mydb.commit()
print("Data update...")