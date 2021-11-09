import mysql.connector
import time
from prettytable import PrettyTable

def connectdb():
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
def showtableval():
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    y=curzor.execute("select * from task")
    x=curzor.fetchall()
    for i in x:
        print(i)
    curzor.execute("select Count(*) from task")
    print(curzor.fetchall())
def insert(tid, tname, tdesc, tstatus, tpriority, tnotes, tbm, townid, tcrtid, crton, modon):
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    command = ("insert into task(tid,tname,tdesc,tstatus,tpriority,tnotes,tbm,townid,tcrtid,crton,modon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (tid, tname, tdesc, tstatus, tpriority, tnotes, tbm, townid, tcrtid, crtdon, modon)
    curzor.execute(command, data)
    db.commit()
def deleterow(tid):
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    command=("delete from task where taskid=%s"%(tid))
    data=(tid)
    curzor.execute(command,data)
    db.commit()
    time.sleep(2)
    print("Deleted Successfully..")
    showtableval()

def prioritize(tpriority,tid):
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    #db,curzor=connectdb()
    print("Prioritizing the tasks......")
    time.sleep(1)
    curzor.execute("update task set priority=%s where taskid=%s",(tpriority,tid))
    db.commit()
    print("Successfully set the priority.\ntaskid:"+str(tid)+"-->priority:"+str(tpriority))
    showtableval()

def addbooknotes(tnotes,tbm,tid):
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    #db,curzor = connectdb()
    print("Adding Notes and Bookmarks")
    time.sleep(1)
    curzor.execute("UPDATE task SET notes=%s,bookmark=%s WHERE taskid=%s",(tnotes,tbm,tid))
    db.commit()
    print("Successfully added notes,bookmarks. ")
    showtableval()
def searchtasks(tid):
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    print("searching the Tasks.......")
    time.sleep(2)
    command=("select taskname from task where taskid=%s"%(tid))
    data=(tid)
    curzor.execute(command,data)
    x=str(curzor.fetchall())
    time.sleep(1)
    t=PrettyTable(['Task Name'])
    t.add_row([x[3:len(x)-4]])
    print(t)

def trackcomp():
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    print("COMPLETED TASKS")
    curzor.execute("select taskname,taskid from task where stats='completed'")
    x=curzor.fetchall()
    t=PrettyTable(['Taskname','Task ID'])
    for i in x:
        t.add_row([i[0],i[1]])
    print(t)

def insert(tk):
    #db,curzor = connectdb()
    db = mysql.connector.connect(host="localhost", user="root", password="Venkat@970", database="casestudy")
    curzor = db.cursor()
    command = ("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (tk.tid, tk.tname, tk.tdesc, tk.tstatus, tk.tpriority,tk.tnotes,tk.tbm,tk.townid,tk.tcrtid,tk.crton,tk.modon)
    curzor.execute(command, data)
    db.commit()
    time.sleep(2)
    print("Inserted Successfully..")
    showtableval()
