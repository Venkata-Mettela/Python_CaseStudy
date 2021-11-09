from dao.dbconnection import getdbconnection
def create_task(task):
    mydb = getdbconnection()
    mycursor =mydb.cursor()
    sql ="INSERT INTO task (tname,tdesc,tstatus,tpriority,tnotes,tbm,townid,tcrid,crton,modon) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (task.tname,task.tdesc,task.tstatus,task.tpriority,task.tnotes,task.tbm,task.townid,task.tcrid,task.crton,task.modon)
    mycursor.execute(sql,val)
    mydb.commit
    mydb.close()