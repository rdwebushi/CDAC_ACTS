import mysql.connector
###connect program to database###
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "rushi123",
    database= "testdb"
)
mycursor = mydb.cursor()
### mycursor.execute("SHOW DATABASES")
mycursor.execute("DELETE TEMP_DATA ( Sensor char, temp float, city char)")
#mycursor.execute("SHOW TABLE")
for db in mycursor:
    print(db)