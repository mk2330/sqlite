import sqlite3
con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query=" Update tblest set sal=1300000 where eid=1004"
    cr.execute(query)
    con.commit()

    print(cr.rowcount, "no. of rows affected")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()

'''
1 no. of rows affected
'''
