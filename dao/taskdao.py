from dbconnections import getdbconnection
def create_task(task):
    mydb=getdbconnection()
    mycursor=mydb.cursor()
    sql="insert into task(tname,tdesc,tstatus,tpriority,tnotes,tbm,townid,tcrid,crton,modon)VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(task.taskname,task.tdesc,task.tstatus,task.tprority,task.tnotes,task.tbm,task.townid,task.tcrid,task.crton,task.modon)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()
