import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="David",
    passwd='Sword',
    database="DMSN"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE movies (id INT PRIMARY KEY, movie VARCHAR(255))")
