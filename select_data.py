import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="harmi@2510",database="Learncoding")
db_cursor=mydb.cursor()

db_cursor.execute("select * from Emp")
# db_data=db_cursor.fetchall()          #fetchone for only one record show
# print(db_data)

for db_data in db_cursor.fetchall():    # loop wise
    print(db_data)