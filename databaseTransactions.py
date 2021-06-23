import sqlite3




def contentAdd(name,title,content,imageUrl,pageUrl,iconUrl,topic,subtopic):
    if content!="":
        try:
            con=sqlite3.connect("updates.db")
            cursor=con.cursor()
            data_tuple=(name,title,content,imageUrl,pageUrl,iconUrl,topic,subtopic)
            cursor.execute("CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT,content TEXT, imageurl TEXT, pageurl TEXT, iconurl TEXT, topic TEXT, subtopic TEXT)")
            cursor.execute("INSERT INTO news(name,title,content,imageurl,pageurl,iconurl,topic,subtopic) VALUES (?,?,?,?,?,?,?,?)",data_tuple)

            con.commit()
            cursor.close()
            con.close()
        except:
            print("Database Error!")





def apiAdd():
    try:
        con=sqlite3.connect("updates.db")
        cursor=con.cursor()
        cursor.execute("DROP TABLE IF EXISTS api")
        con.commit()
        cursor.close()
        con.close()
    except:
        print("Database Error!")


    try:
        con=sqlite3.connect("updates.db")
        cursor=con.cursor()
        cursor.execute("CREATE TABLE api AS SELECT * FROM news")
        con.commit()
        cursor.close()
        con.close()
    except:
        print("Database Error!")



    try:
        con=sqlite3.connect("updates.db")
        cursor=con.cursor()
        cursor.execute("DROP TABLE IF EXISTS news")
        con.commit()
        cursor.close()
        con.close()
    except:
        print("Database Error!")




