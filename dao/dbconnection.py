import mysql.connector
def getdbconnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sonata@123",
        database="casestudy"
    )
    return mydb
