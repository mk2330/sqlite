import sqlite3
con=sqlite3.connect("mkdb.db")
try:
    query="""
Create table 'tblest'
(
   'eid' integer not null primary key autoincrement,
   'ename' text not null,
   'sal' numeric(10, 2),
   'tax10' numeric(8, 2),
   'tax20' numeric(8, 2),
   'tax30' numeric(8, 2),
   'tottax' numeric(8, 2),
   'np' numeric(10, 2)
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
