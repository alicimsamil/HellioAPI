import sqlite3




def contentAdd(name,title,content,imageUrl,pageUrl,iconUrl):
    try:
        con=sqlite3.connect("updates.db")
        cursor=con.cursor()
        data_tuple=(name,title,content,imageUrl,pageUrl,iconUrl)
        cursor.execute("CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT, content TEXT, imageurl TEXT, pageurl TEXT, iconurl TEXT)")
        cursor.execute("INSERT INTO news(name,title,content,imageurl,pageurl,iconurl) VALUES (?,?,?,?,?,?)",data_tuple)

        con.commit()
        cursor.close()
        con.close()
    except:
        print("Database Error!")
