import sqlite3
con=sqlite3.connect("mkdb.db")
try:
    query="""
Create table 'examresult'
(
   'RNo' integer not null primary key autoincrement,
   'SName' text not null,
   'M1' numeric check(M1 >= 0 and M1 <= 100),
   'M2' numeric check(M2 >= 0 and M2 <= 100),
   'Total' numeric,
   'Average' numeric,
   'Result' text not null default 'Fail' check(Result == 'Pass' or Result == 'Fail')
);
    """
    con.execute(query)
    con.commit()

    print("Successfully created new table")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()

'''
Successfully created new table
'''
