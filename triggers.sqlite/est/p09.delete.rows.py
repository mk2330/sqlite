import sqlite3
con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query=" delete from tblest where eid=1003"
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
