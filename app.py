import os
from flask import (
    Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/get_meetings")
def get_meetings():
    meetings = list(mongo.db.meetings.find())
    return render_template("meetings.html", meetings=meetings)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    meetings = list(mongo.db.meetings.find({"$text": {"$search": query}}))
    return render_template("meetings.html", meetings=meetings)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
                # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_meeting", methods=["GET", "POST"])
def add_meeting():
    if request.method == "POST":
        is_complete = "on" if request.form.get("is_complete") else "off"
        meeting = {
            "group_name": request.form.get("group_name"),
            "meeting_name": request.form.get("meeting_name"),
            "meeting_agenda": request.form.get("meeting_agenda"),
            "meeting_date": request.form.get("meeting_date"),
            "meeting_actions": request.form.get("meeting_actions"),
            "is_complete": is_complete,
            "created_by": session["user"]
        }
        mongo.db.meetings.insert_one(meeting)
        flash("Meeting Successfully Added")
        return redirect(url_for("get_meetings"))

    groups = mongo.db.groups.find().sort("group_name", 1)
    return render_template("add_meeting.html", groups=groups)


@app.route("/edit_meeting/<meeting_id>", methods=["GET", "POST"])
def edit_meeting(meeting_id):
    if request.method == "POST":
        is_complete = "on" if request.form.get("is_complete") else "off"
        submit = {
            "group_name": request.form.get("group_name"),
            "meeting_name": request.form.get("meeting_name"),
            "meeting_agenda": request.form.get("meeting_agenda"),
            "meeting_date": request.form.get("meeting_date"),
            "meeting_actions": request.form.get("meeting_actions"),
            "is_complete": is_complete,
            "created_by": session["user"]
        }
        mongo.db.meetings.update({"_id": ObjectId(meeting_id)}, submit)
        flash("Meeting Successfully Updated")
        
    meeting = mongo.db.meetings.find_one({"_id": ObjectId(meeting_id)})
    groups = mongo.db.groups.find().sort("group_name", 1)
    return render_template("edit_meeting.html", meeting=meeting, groups=groups)


@app.route("/delete_meeting/<meeting_id>")
def delete_meeting(meeting_id):
    mongo.db.meetings.remove({"_id": ObjectId(meeting_id)})
    flash("Meeting Successfully Deleted")
    return redirect(url_for("get_meetings"))


@app.route("/get_groups")
def get_groups():
    groups = mongo.db.groups.find().sort("group_name")
    return render_template("groups.html", groups=groups)


@app.route("/add_group", methods=["GET", "POST"])
def add_group():
    if request.method == "POST":
        group = {
            "group_name": request.form.get("group_name")
        }        
        mongo.db.groups.insert_one(group)
        flash("New Group Added")
        return redirect(url_for("get_groups"))

    return render_template("add_group.html")


@app.route("/edit_group/<group_id>", methods=["GET", "POST"])
def edit_group(group_id):
    if request.method == "POST":
        submit = {
            "group_name": request.form.get("group_name")
        }
        mongo.db.groups.update({"_id": ObjectId(group_id)}, submit)
        flash("Group Successfully Updated")
        return redirect(url_for("get_groups"))

    group = mongo.db.groups.find_one({"_id": ObjectId(group_id)})
    return render_template("edit_group.html", group=group)


@app.route("/delete_group/<group_id>")
def delete_group(group_id):
    mongo.db.groups.remove({"_id": ObjectId(group_id)})
    flash("Group Successfully Deleted")
    return redirect(url_for("get_groups"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
