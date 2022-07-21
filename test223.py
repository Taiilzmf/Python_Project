## Imports sqlite3
import sqlite3
##adds filelist and its contents
fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
#connects sqlite to a new database
conn = sqlite3.connect ('test.db')
#gives us a way to control the database and creates the table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_testCol TEXT) ")
    #cycles through the list to find all .txt files in list then prints them
    for x in fileList:
        if x.endswith(".txt"):
            cur.execute("INSERT INTO tbl_fileList(col_testCol) VALUES (?)", \
                        (x,))
            print(x)
    #commits connection
    conn.commit()
    #closes the connection
conn.close()
