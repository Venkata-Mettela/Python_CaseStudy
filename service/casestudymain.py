from dao.taskdao import create_task
from service.task import *
t = Task(tname="name1", tdesc="description", tstatus="status", tpriority=2, tnotes="notes", tbm="bookmark", townid=5, tcrid=7, crton="2021-10-30", modon="2021-11-2")
create_task(t)
