#QUESTION 1

import sqlite3
conn =sqlite3.connect('dbms.db')
print("opened database successfully")

conn.execute("""CREATE TABLE BOOK
           (BOOK_ID INT PRIMARY KEY NOT NULL,
           TITLE_ID TEXT NOT NULL,
           LOCATION CHAR (30),
           GENRE CHAR (20))""")
print("table created successfully")
conn.close()


conn.execute('''create table TITLE
           (TITLE_ID INT PRIMARY KEY NOT NULL,
           ISBN_ID INT NOT NULL,
           PUBLISHER_ID INT NOT NULL ,
           PUBLICATION_YEAR INT NOT NULL)''')
print("table created successfully")
conn.close()


conn.execute('''create table PUBLISHERS
(PUBLISHERS_ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
STREET_ADDRESS CHAR(50),
SUIT_NUMBER INT NOT NULL,
ZIP_CODE_ID INT NOT NULL)''')
print("table created successfully")
conn.close()


conn.execute('''create table zip_code
(ZIP_CODE_ID INT PRIMARY KEY NOT NULL,
CITY_ID TEXT NOT NULL,
STATE CHAR(50),
ZIP_CODE INT NOT NULL)''')
print("table created successfully")
conn.close()


conn.execute('''create table authors_titles
(AUTHOR_TITLE_ID INT PRIMARY KEY NOT NULL,
AUTHOR_ID TEXT NOT NULL,
TITLE_ID NOT NULL)''')
print("table created successfully")
conn.close()



conn.execute('''create table authors
(AUTHOR_ID INT PRIMARY KEY NOT NULL,
FIRST_NAME TEXT NOT NULL,
MIDDLE_NAME TEXT NOT NULL,
LAST_NAME TEXT NOT NULL)''')
print("table created successfully")
conn.close()

#QUESTON 2


conn.execute("INSERT INTO BOOK(BOOK_ID,TITLE_ID,LOCATION,GENRE) VALUES(1,11,'INDIA','BIOGRAPHY')")
conn.execute("INSERT INTO TITLE(TITLE_ID,ISBN_ID,PUBLISHER_ID,PUBLICATION_YEAR) VALUES(2,121432,12,1997)")
conn.execute("INSERT INTO PUBLISHERS(PUBLISHERS_ID,NAME,STREET_ADDRESS,SUIT_NUMBER,ZIP_CODE_ID) VALUES(111,'JOHN','310A ALGERIA',110,93)")
conn.execute("INSERT INTO AUTHORS_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID) VALUES(222,'RICK',121)")
conn.execute("INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME) VALUES(333,'ROBIN','SINGH','SHARMA')")



#QUESTION 3
a=conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE FROM BOOK")
for b in a:
    print("BOOK ID:",b[0])
    print("TITLE ID:", b[1])
    print("LOCATION ID:", b[2])
    print("GENRE ID:", b[3])
conn.execute("UPDATE BOOK SET LOCATION ='AMERICA' WHERE BOOK_ID=1")

a=conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE FROM BOOK")
for b in a:
    print("BOOK ID:",b[0])
    print("TITLE ID:", b[1])
    print("LOCATION ID:", b[2])
    print("GENRE ID:", b[3])

conn.close()


