import sqlite3
con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query="Insert into tblest (ename,sal)values('x3', 1400000), ('x4', 800000), ('x2', 500000)"
    cr.execute(query)
    con.commit()

    print(cr.rowcount, "no. of rows affected")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()


'''
3 no. of rows affected
'''
