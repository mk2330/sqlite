import sqlite3
con=sqlite3.connect("mkdb.db")
cr=con.cursor()
vName='Grapes'
try:
    query="Delete from ExamResult where SName = '%s'" %(vName)
    cr.execute(query)
    con.commit()

    print(cr.rowcount, "no. of rows affected")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()
    
'''
0 no. of rows affected
'''
