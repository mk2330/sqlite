import sqlite3
con=sqlite3.connect("mkdb.db")
cursor=con.cursor()
try:
    query="Select * from ExamResult"
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
1001	Apple	56	65.5	121.5	60.75	Pass	
1003	Banana	65.5	56	121.5	60.75	Pass	
1004	Orange	45	54.5	99.5	49.75	Pass
'''
