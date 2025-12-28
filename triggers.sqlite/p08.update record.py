import sqlite3
con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query="Update ExamResult set M2=34.5 where RNo=1002"
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
