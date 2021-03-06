from flask import Flask, request, jsonify
from flask_restful import Api
import sqlite3
import datetime
import art,gaming,music,news,sports,showsMovies,science,technology,travel
from apscheduler.schedulers.background import BackgroundScheduler
import databaseTransactions



app = Flask(__name__)
api = Api(app)



@app.before_first_request
def sensor():
    if datetime.datetime.now().minute == 1:
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







def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("updates.db")
    except sqlite3.error as e:
        print(e)
    return conn






@app.route("/v1/topics", methods=["GET", "POST"])
def topics():

    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT DISTINCT name,iconurl,topic,subtopic FROM api")
        updates = [
            dict(name=row[0], iconurl=row[1], topic=row[2], subtopic=row[3])
            for row in cursor.fetchall()
        ]
        if updates is not None:
            return jsonify(updates)




@app.route("/", methods=["GET", "POST"])
def mainScreen():

    if request.method == "GET":

        if updates is not None:
            return {"Updates":"/v1/updates","Topics":"/v1/topics"}




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
    app.run(debug=True, threaded=True,use_reloader=False)