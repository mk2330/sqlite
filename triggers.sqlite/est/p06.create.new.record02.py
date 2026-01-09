import sqlite3
ename=(input("Enter Employee Name: "))
esal=int(input("Enter Employee Salary : "))

con=sqlite3.connect("mkdb.db")
cr=con.cursor()
try:
    query="Insert into tblest (ename,sal)values('%s', '%5.2f')"%(ename, esal)
    cr.execute(query)
    con.commit()

    print(cr.rowcount, "no. of rows affected")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()


'''
Output:
Enter Employee Name: x5
Enter Employee Salary : 1200000
1 no. of rows affected
'''
