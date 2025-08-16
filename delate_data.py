import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="harmi@2510",database="Learncoding")
db_cursor=mydb.cursor()
## for one data delete:
# db_delete="delete from Emp where Ename=%s"
# db_value=("Shubham",)  #(,) is comlasory for pass value in tuple 
# db_cursor.execute(db_delete,db_value)
# mydb.commit()
# print(db_cursor.rowcount,"Data deleted...")

##full data delete:
db_delete="truncate table Emp"
db_cursor.execute(db_delete)
mydb.commit()
print("All Data deleted...")

