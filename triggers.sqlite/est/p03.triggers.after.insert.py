import sqlite3
con=sqlite3.connect("mkdb.db")
try:
    query="""

Create trigger est_TrgIns after insert on tblest
Begin
    Update tblest set tax10=iif(new.sal > 500000, 250000, iif(new.sal > 250000, new.sal, 0)) * 10.0 / 100 where eid=new.eid;
    Update tblest set tax20=iif(new.sal > 1000000, 500000, iif(new.sal > 500000, new.sal, 0)) * 20.0 / 100 where eid=new.eid;
    Update tblest set tax30=iif(new.sal > 1000000, 0) * 30.0 / 100 where eid=new.eid;
    Update tblest set tottax=tax10 + tax20 + tax30 where eid=new.eid;
    Update tblest set np=new.sal - tottax where eid=new.eid;

End;
    """
    con.execute(query)
    con.commit()

    print("Successfully created before insert trigger")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()

'''
Successfully created before insert trigger
'''
