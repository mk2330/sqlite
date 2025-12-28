import sqlite3
vName=str(input("Enter Student name: "))
vM1=float(input("Enter Mark-1: "))
vM2=float(input("Enter Mark-2: "))

con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query="Insert into ExamResult (SName, M1, M2) values ('%s', %5.2f, %5.2f)" %(vName, vM1, vM2)
    cr.execute(query)
    con.commit()

    print(cr.rowcount, "no. of rows affected")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()


'''
Enter Student name: Grapes
Enter Mark-1: 98.0
Enter Mark-2: 20
1 no. of rows affected
'''
