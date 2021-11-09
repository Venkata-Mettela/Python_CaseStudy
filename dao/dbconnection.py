import mysql.connector
def getdbconnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Venkat@970",
        database="casestudy"
    )
    return mydb
