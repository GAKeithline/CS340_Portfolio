# Project Group 14 - Sayid Ali and Gilbert Keithline
# Date: 11/19/2024
# Project Part 4 DRAFT- Enable CRUD functionality for one entity table

# Citation for: CSS style sheet implementation
# Date: 11/19/2024
# Copied from: Stack Overflow
# Source URL: https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python

# Citation for: Flask app.py construction
# Date: 11/17/2024
# Adapted from: OSU CS340 - Flask Starter App
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_keithlig"
app.config["MYSQL_PASSWORD"] = "2334"
app.config["MYSQL_DB"] = "cs340_keithlig"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
# Routes 

@app.route('/')
# Set landing page
def home():
    return redirect("/index")

@app.route('/index')
# Render the Home page
def index():
    return render_template('index.j2')

@app.route("/users", methods=["POST", "GET"])
# 'Display' Users table and enable 'Create' functionality
def users():
    # Render the table (Display)
    if request.method == 'GET':
        query = "SELECT user_id as ID, user_name as Name, user_email as 'Email Address', user_password as Password FROM Users;"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        user_data = cursor.fetchall()

        return render_template('users.j2', user_data = user_data)
    
    # Add a new user (Create)
    if request.method == 'POST':
        if request.form.get("addUser"):
            name = request.form["user_name"]
            email = request.form["user_email"]
            pword = request.form["user_password"]

            query = "INSERT INTO Users (user_name, user_email, user_password) VALUES (%s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (name, email, pword))
            mysql.connection.commit()
        
        return redirect("/users")

@app.route("/removeUser/<int:id>")
# 'Remove' a table item
def removeUser(id):
    # Deletes a User (Remove)
    query = "DELETE FROM Users WHERE user_id = '%s';"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/users")

@app.route("/editUser/<int:id>", methods=["POST", "GET"])
# Enables 'Update' funtionality for User items
def editUser(id):
    # Renders the update template
    if request.method == "GET":
        query = 'SELECT * FROM Users WHERE user_id =%s' % (id)
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        user_data = cursor.fetchall()

        return render_template("editUser.j2", user_data=user_data)
    
    # Allows database user to change row information based on user_id selection (Update)
    if request.method == "POST":
        if request.form.get("editUser"):
                id = request.form["user_id"]
                name = request.form["user_name"]
                email = request.form["user_email"]
                pword = request.form["user_password"]

                query = "UPDATE Users SET Users.user_name = %s, Users.user_email = %s, Users.user_password = %s WHERE Users.user_id = %s"
                cursor = mysql.connection.cursor()
                cursor.execute(query, (name, email, pword, id))
                mysql.connection.commit()
                
        return redirect("/users")
    

@app.route("/teams", methods=["POST", "GET"])
# 'Display' Teams table and enable 'Create' functionality
def teams():
    # Render the table (Display)
    if request.method == 'GET':
        query = 'SELECT team_id as ID, team_name as "Team Name", team_win as Wins, team_loss as Losses FROM Teams;'
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        team_data = cursor.fetchall()

        return render_template('teams.j2', team_data = team_data)
    
    # Add a new Team (Create)
    if request.method == 'POST':
        if request.form.get("addTeam"):
            name = request.form["team_name"]
            win = request.form["team_win"]
            loss = request.form["team_loss"]

            query = 'INSERT INTO Teams (team_name, team_win, team_loss) VALUES (%s, %s, %s);'
            cursor = mysql.connection.cursor()
            cursor.execute(query, (name, win, loss))
            mysql.connection.commit()
        
        return redirect("/teams")
    
@app.route("/removeTeam/<int:id>")
# 'Remove' a table item
def removeTeam(id):
    # Deletes a Team (Remove)
    query = "DELETE FROM Teams WHERE team_id = '%s';"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/teams")

@app.route("/editTeam/<int:id>", methods=["POST", "GET"])
# Enables 'Update' funtionality for Team items
def editTeam(id):
    # Renders the update template
    if request.method == "GET":
        query = 'SELECT * FROM Teams WHERE team_id =%s' % (id)
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        team_data = cursor.fetchall()

        return render_template("editTeam.j2", team_data=team_data)
    
    # Allows database user to change row information based on user_id selection (Update)
    if request.method == "POST":
        if request.form.get("editTeam"):
                id = request.form["team_id"]
                name = request.form["team_name"]
                win = request.form["team_win"]
                loss = request.form["team_loss"]

                query = "UPDATE Teams SET team_name = %s, team_win = %s, team_loss = %s WHERE team_id = %s"
                cursor = mysql.connection.cursor()
                cursor.execute(query, (name, win, loss, id))
                mysql.connection.commit()
                
        return redirect("/teams")


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 53530)) 
    
    app.run(port=port, debug=True) 


