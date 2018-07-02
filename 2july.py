import sqlite3
conn =sqlite3.connect('test.db')
print("opened database successfully")
"""
conn.execute('''create table companies
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL)''')
print("table created successfully")
conn.close()

conn.execute("INSERT INTO COMPANIES(ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'PAUL',32,'california',2000.00)")

conn.execute("INSERT INTO COMPANIES(ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'allen',21,'india',2022.00)")


cursor =conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY from COMPANIES")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("SALARY=",row[4]),"\n"

print("operation  succesfull")
conn.close()

conn.execute("UPDATE COMPANIES set SALARY=25000 where ID=1")
conn.commit()

print("total no. rows updated=",conn.total_changes)
conn.close()
"""

"""
conn.execute("DELETE from COMPANIES where ID=2")
conn.commit()
print("total number of rows deleted",conn.total_changes)
"""





