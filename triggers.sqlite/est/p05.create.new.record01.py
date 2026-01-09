import sqlite3
con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query="Insert into tblest(eid, ename, sal) values(1001, 'x5', 1600000)"
    cr.execute(query)
    con.commit()


    print(cr.rowcount, "no.of rows affected")
except Exception as e:
    con.rollback()
    print("Err.:",e)
con.close()
