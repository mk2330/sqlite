import sqlite3
con=sqlite3.connect("mkdb.db")
cursor=con.cursor()
try:
    query="Select * from tblest"
    cursor=con.execute(query)
    rows=cursor.fetchall()
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            print(rows[r][c], end="\t")
        else:
            print()
except Exception as ex:
    print("Err:", ex)
con.close()

'''
output:
1001	x5	1600000	25000	100000	0	125000	1475000	
1002	x5	1200000	25000	100000	0	125000	1075000	
1004	x4	1300000	25000	100000	0	125000	1175000	
1005	x2	500000	50000	0	None	None	None
'''
