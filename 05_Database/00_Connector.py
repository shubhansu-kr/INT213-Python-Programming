import mysql.connector 

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '2021',
    database = 'python'
)

# Check if connection is established or not 
print(mydb.connection_id)   

# Create a new database once the connection is established or open a 
# pre existing database 

# cursor is used to create a memory within the server to execute commands
cur = mydb.cursor()

# Execute commands 
# cur.execute('CREATE DATABASE PYTHON')
# cur.execute('SHOW DATABASES')
# cur.execute('CREATE TABLE STUDENT(NAME VARCHAR(22), ROLL INT(10))')

A = 'INSERT INTO STUDENT VALUES (%s, %s)'
R = ('AVI', 21)
cur.execute(A, R)

# We need to commit our changes. 
mydb.commit()

print(cur.rowcount)