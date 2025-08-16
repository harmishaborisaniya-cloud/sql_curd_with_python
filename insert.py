import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="harmi@2510",database="Learncoding")
db_cursor=mydb.cursor()
#for single insertion
# db_cursor.execute("insert into Emp(roll,Ename) values(%s,%s)",(10,"Shubham"))
# mydb.commit()# without commit no one data will insert in database
# print(db_cursor.rowcount,"Record inserted....")

#for multiple insertion
db_insert="insert into Emp(roll,Ename) values(%s,%s)"
db_values_list=[(1,"riya"),(2,"meet"),(3,"soha")]
db_cursor.executemany(db_insert,db_values_list)         #executemany
mydb.commit()# without commit no one data will insert in database
print(db_cursor.rowcount,"Record inserted....")


#cmd mathi jova mate....
# C:\Users\harmi>mysql -u root -p
# Enter password: **********#harmi@2510

# mysql> select * from Learncoding.Emp;


# mysql> srttcg         # if jo aavi rite kuch bhi lakhi enter thai gyu hoy...
#     ->
#     ->
#     -> \c             #command clear karva mate 
# mysql> 