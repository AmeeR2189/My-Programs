import sqlite3
mydb=sqlite3.connect(database="students")
mycur=mydb.cursor()
try:
    sql="""create table data(rollno,name,branch,college,phno.email)"""
    mycur.execute(sql)
except:
    pass
while True:
    ch=int(input("1.insert 2.display 3.exit \n"))
    if ch==1:
        d=tuple(map(str,input().split()))
        ins="insert into data(rollno,name,branch,college,phno,email)values(?,?,?,?,?,?)"
        mycur.execute(ins,d)
    elif ch==2:
        mycur.execute("select * from data")
        data=mycur.fetchall()
        for d in data:
            print(*d)
    else:
        break
    mydb.commit()
