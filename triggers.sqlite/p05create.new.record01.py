import sqlite3
con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query="Insert into ExamResult (RNo, SName, M1, M2) values (1001, 'Apple', 56, 65.5)"
    cr.execute(query)
    con.commit()

    print(cr.rowcount, "no. of rows affected")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()

'''
1  no. of rows affected
'''
