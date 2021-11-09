from service.task import *
def create_task(task):
    mydb=getconnection()
    mycursor=mydb.cursor()
    #command = "insert into task(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)" % (Task.tid,Task.tname,Task.tdesc,Task.tstatus,Task.tpriority,Task.tnotes,Task.tbm,Task.townid,Task.tcrtid,Task.crton,Task.modon)
    #command=("insert into task(tid,tname,tdesc,tstatus,tpriority,tnotes,tbm,townid,tcrtid,crtdon,modon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    sql="inster into task(tid,tname,tdesc ,tstatus ,tpriority  ,tnotes ,tbm  ,townid,tcrtid ,crton ,modon)"
    val=(task.tid,task.tname,task.tdesc,task.tstatus,task.tpriority,task.tnotes,task.tbm,task.townid,task.tcrtid,task.crton,task.modon)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()
def assign_task(tid,townid):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "update task set ownerid=%s where taskid=%s"
    val = (townid,tid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
def assign_priority(taskid,priority):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "update task set priority=%s where taskid=%s"
    val = (tpriority, tid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
def searchtask(tid,tname):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "select * from task  where taskid=%s and taskname=%s"
    val = (tname, tid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
def deletetask(tid,tname):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "select * from task  where taskid=%s and taskname=%s"
    val = (tname, tid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
import dbconnection #module import
from service import task #from the package
import time
def run(t):#getting object as para
    print("<<<<<<<<<<<<      WELCOME TO TASK TRACKER      >>>>>>>>>>>>")
    time.sleep(2)#its just to show
    print("connecting to Database........... ")
    time.sleep(2)
    dbconnection.connectdb()#connecting db
    print("Inserting the values.....")
    time.sleep(2)#task object is created here
    print("Inserted Successfully,getting tables ready with newly inserted values....")
    time.sleep(2)
    dbconnection.showtableval()
    print("All values are commited successfully..")#showing table from dbconnect module'''

import dbconnection
from service import task
import time
from prettytable import PrettyTable
def welcome():
    t=PrettyTable(['WELCOME TO TASK TRACKER'])
    t.add_row(['Database Connection Status:Connected'])
    t.add_row([''])
    t.add_row(['USER==root          DATABASE==python'])
    print(t)

def run(op):#getting object as para
    welcome()
    if (op==1):
        tid = 1020
        tname = 'web'
        tdesc = 'js'
        tstatus = 'completed'
        tpriority = 2
        tnotes = 'some notes'
        tbookmark = 'bookm1'
        townid = 115
        tcrtid = 225
        crtdon = '2021-10-30'
        modon = '2021-11-03'
        tsk = task.Task(tid, tname, tdesc, tstatus, tpriority, tnotes, tbm, townid, tcrtid, crton,modon)
        dbconnection.insert(tsk)
    elif(op==2):
        print("DELETION")
        x=int(input("Enter Task id to delete: "))
        dbconnection.deleterow(x)
    elif(op==3):
        dbconnection.showtableval()
    elif(op==4):
        id=int(input("Enter tid(Int): "))
        pr=int(input("Enter Priority(Range[1-5]): "))
        dbconnection.prioritize(pr,id)
    elif(op==5):
        id = int(input("Enter tid(Int): "))
        note=str(input("Enter Notes to add: "))
        bm=str(input("Enter Bookmark to add: "))
        dbconnection.addbooknotes(note,bm,id)
    elif(op==6):
        id = int(input("Enter taskid(Int): "))
        dbconnection.searchtasks(id)
    elif(op==7):
        dbconnection.trackcomp()
    else:
        print("Invalid Input.\nTry again...")
        return 0
def takeinput():
    t=PrettyTable(['Select Your Choice '])
    t.add_row(['  1]Add Values           '])
    t.add_row(['  2]Delete Value         '])
    t.add_row(['  3]Display Table        '])
    t.add_row(['  4]Prioritize           '])
    t.add_row(['  5]Add Notes & Bookmarks'])
    t.add_row(['  6]Search Tasks         '])
    t.add_row(['  7]Track Completion     '])
    t.add_row(['  0]Exit/close           '])
    print(t)
    op = int(input("Enter your choice: "))
    return op
