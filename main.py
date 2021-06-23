from flask import Flask, request, jsonify
from flask_restful import Api
import sqlite3
import datetime
import art,gaming,music,news,sports,showsMovies,science,technology,travel
from apscheduler.schedulers.background import BackgroundScheduler
import databaseTransactions
def sensor():
    if datetime.datetime.now().minute == 18:
        art.art()
        gaming.gaming()
        music.music()
        news.news()
        science.science()
        showsMovies.showsMovies()
        sports.sports()
        technology.technology()
        travel.travel()
        databaseTransactions.apiAdd()


sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=1, id="test",max_instances=6)
sched.start()

app = Flask(__name__)
api = Api(app)




def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("updates.db")
    except sqlite3.error as e:
        print(e)
    return conn







@app.route("/v1/updates", methods=["GET", "POST"])
def updates():

    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM api")
        updates = [
            dict(id=row[0], name=row[1], title=row[2], content=row[3], imageurl=row[4], pageurl=row[5], iconurl=row[6], topic=row[7], subtopic=row[8])
            for row in cursor.fetchall()
        ]
        if updates is not None:
            return jsonify(updates)



if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)