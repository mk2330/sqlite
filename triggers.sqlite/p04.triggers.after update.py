import sqlite3
con=sqlite3.connect("mkdb.db")
try:
    query="""
Create trigger ExamResult_TrgUpd after update on ExamResult
Begin
    Update ExamResult set Total=(new.M1 + new.M2), Average=(new.M1 + new.M2) / 2 where RNo=new.RNo;
    Update ExamResult set Result='Fail' where RNo=new.RNo;
    Update ExamResult set Result='Pass' where (new.M1 > 34.4 and new.M2 > 34.4) and RNo=new.RNo;
End;
    """
    con.execute(query)
    con.commit()

    print("Successfully created before update trigger")
except Exception as ex:
    con.rollback()
    print("Err:", ex)
con.close()

'''
Successfully created before update trigger
'''
