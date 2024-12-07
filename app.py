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
    
@app.route("/injuryStatus", methods=["POST", "GET"])
# 'Display' Users table and enable 'Create' functionality
def injury():
    # Render the table (Display)
    if request.method == 'GET':
        query = "SELECT injury_id as ID, injury_tag as Tag, injury_description as 'Status Description' FROM Injury_Status;"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        injury_data = cursor.fetchall()

        return render_template('injuryStatus.j2', injury_data = injury_data)
    
    # Add a new user (Create)
    if request.method == 'POST':
        if request.form.get("addInjury"):
            tag = request.form["injury_tag"]
            desc = request.form["injury_description"]

            query = "INSERT INTO Injury_Status (injury_tag, injury_description) VALUES (%s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (tag, desc))
            mysql.connection.commit()
        
        return redirect("/injuryStatus")
    
@app.route("/removeInjury/<int:id>")
# 'Remove' a table item
def removeInjury(id):
    # Deletes a User (Remove)
    query = "DELETE FROM Injury_Status WHERE injury_id = '%s';"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/injuryStatus")

@app.route("/editInjury/<int:id>", methods=["POST", "GET"])
# Enables 'Update' funtionality for User items
def editInjury(id):
    # Renders the update template
    if request.method == "GET":
        query = 'SELECT * FROM Injury_Status WHERE injury_id =%s' % (id)
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        injury_data = cursor.fetchall()

        return render_template("editInjury.j2", injury_data=injury_data)
    
    # Allows database user to change row information based on user_id selection (Update)
    if request.method == "POST":
        if request.form.get("editInjury"):
                id = request.form["injury_id"]
                tag = request.form["injury_tag"]
                desc = request.form["injury_description"]

                query = "UPDATE Injury_Status SET Injury_Status.injury_tag = %s, Injury_Status.injury_description = %s WHERE Injury_Status.injury_id = %s"
                cursor = mysql.connection.cursor()
                cursor.execute(query, (tag, desc, id))
                mysql.connection.commit()
                
        return redirect("/injuryStatus")
    

@app.route("/players", methods=["POST", "GET"])
# 'Display' Users table and enable 'Create' functionality
def players():
    # Render the table (Display)
    if request.method == 'GET':
        query = "SELECT player_id as ID, player_name as 'Player Name', point_stat as Points, assist_stat as Assists, rebound_stat as Rebounds, block_stat as Blocks, steal_stat as Steals, timePlayed_stat as Minutes, team_id as Team, injury_id as 'Injury Status' FROM Players;"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        player_data = cursor.fetchall()

        query2 = "SELECT team_id FROM Teams;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        team_data = cur.fetchall()

        query3 = "SELECT injury_tag FROM Injury_Status;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        injury_data = cur.fetchall()

        query4 = 'SELECT roster_id FROM Rosters;'
        cur = mysql.connection.cursor()
        cur.execute(query4)
        roster_data = cur.fetchall()

        return render_template('players.j2', player_data = player_data, team_data = team_data, injury_data = injury_data, roster_data = roster_data)
    
    # Add a new user (Create)
    if request.method == 'POST':
        if request.form.get("addPlayer"):
            name = request.form["player_name"]
            points = request.form["player_points"]
            assists = request.form["player_assists"]
            rebounds = request.form["player_rebounds"]
            blocks = request.form["player_blocks"]
            steals = request.form["player_steals"]
            minutes = request.form["player_minutes"]
            team = request.form["player_team"]
            injury = request.form["player_injury"]

            query = "INSERT INTO Players (player_name, point_stat, assist_stat, rebound_stat, block_stat, steal_stat, timePlayed_stat, team_id, injury_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (name, points, assists, rebounds, blocks, steals, minutes, team, injury))
            mysql.connection.commit()
        
        return redirect("/players")
    
@app.route("/removePlayer/<int:id>")
# 'Remove' a table item
def removePlayer(id):
    # Deletes a User (Remove)
    query = "DELETE FROM Players WHERE player_id = '%s';"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/players")


@app.route("/editPlayer/<int:id>", methods=["POST", "GET"])
# Enables 'Update' funtionality for User items
def editPlayer(id):
    # Renders the update template
    if request.method == "GET":
        query = 'SELECT * FROM Players WHERE player_id =%s' % (id)
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        player_data = cursor.fetchall()

        query2 = "SELECT team_id FROM Teams"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        team_data = cur.fetchall()

        query3 = "SELECT injury_tag FROM Injury_Status"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        injury_data = cur.fetchall()

        query4 = 'SELECT roster_id FROM Rosters;'
        cur = mysql.connection.cursor()
        cur.execute(query4)
        roster_data = cur.fetchall()

        return render_template("editPlayer.j2", player_data=player_data, team_data=team_data, injury_data=injury_data, roster_data=roster_data)
    
    # Allows database user to change row information based on user_id selection (Update)
    if request.method == "POST":
        if request.form.get("editPlayer"):
            id = request.form["player_id"]
            name = request.form["player_name"]
            points = request.form["player_points"]
            assists = request.form["player_assists"]
            rebounds = request.form["player_rebounds"]
            blocks = request.form["player_blocks"]
            steals = request.form["player_steals"]
            minutes = request.form["player_minutes"]
            team = request.form["player_team"]
            injury = request.form["player_injury"]

            query = "UPDATE Players SET player_name = %s, point_stat = %s, assist_stat = %s, rebound_stat = %s, block_stat = %s, steal_stat = %s, timePlayed_stat = %s, team_id = %s, injury_id = %s WHERE player_id = %s;"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (name, points, assists, rebounds, blocks, steals, minutes, team, injury, id))
            mysql.connection.commit()
                
        return redirect("/players")
    
@app.route("/rosters", methods=["POST", "GET"])
# 'Display' Users table and enable 'Create' functionality
def rosters():
    # Render the table (Display)
    if request.method == 'GET':
        query = "SELECT roster_id as ID, roster_name as 'Roster Name', user_id as User FROM Rosters;"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        roster_data = cursor.fetchall()

        query2 = "SELECT user_id FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        user_data = cur.fetchall()

        return render_template('rosters.j2', roster_data = roster_data, user_data = user_data)
    
    # Add a new user (Create)
    if request.method == 'POST':
        if request.form.get("addRoster"):
            name = request.form["roster_name"]
            user = request.form["roster_user"]

            query = "INSERT INTO Rosters (roster_name, user_id) VALUES (%s, %s);"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (name, user))
            mysql.connection.commit()
        
        return redirect("/rosters")
    
@app.route("/removeRoster/<int:id>")
# 'Remove' a table item
def removeRoster(id):
    # Deletes a User (Remove)
    query = "DELETE FROM Rosters WHERE roster_id = '%s';"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/rosters")

@app.route("/editRoster/<int:id>", methods=["POST", "GET"])
# Enables 'Update' funtionality for User items
def editRoster(id):
    # Renders the update template
    if request.method == "GET":
        query = 'SELECT * FROM Rosters WHERE roster_id =%s' % (id)
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        roster_data = cursor.fetchall()

        query2 = "SELECT user_id FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        user_data = cur.fetchall()

        return render_template("editRoster.j2", roster_data=roster_data, user_data=user_data)
    
    # Allows database user to change row information based on user_id selection (Update)
    if request.method == "POST":
        if request.form.get("editRoster"):
            id = request.form["roster_id"]
            name = request.form["roster_name"]
            user = request.form["roster_user"]

            query = "UPDATE Rosters SET roster_name = %s, user_id = %s WHERE roster_id = %s;"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (name, user, id))
            mysql.connection.commit()
                
        return redirect("/rosters")
    
@app.route("/playersRosters", methods=["POST", "GET"])
# 'Display' Users table and enable 'Create' functionality
def relations():
    # Render the table (Display)
    if request.method == 'GET':
        query = "SELECT playerRoster_id as ID, player_id as 'Player ID', roster_id as 'Roster ID' FROM Players_Rosters;"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        pr_data = cursor.fetchall()

        query2 = "SELECT player_id FROM Players"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        player_data = cur.fetchall()

        query3 = "SELECT roster_id FROM Rosters"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        roster_data = cur.fetchall()

        return render_template('playersRosters.j2', pr_data = pr_data, player_data = player_data, roster_data = roster_data)
    
    # Add a new user (Create)
    if request.method == 'POST':
        if request.form.get("addRelation"):
            player = request.form["player"]
            roster = request.form["roster"]

            query = "INSERT INTO Players_Rosters (player_id, roster_id) VALUES (%s, %s);"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (player, roster))
            mysql.connection.commit()
        
        return redirect("/playersRosters")
    
@app.route("/removeRelation/<int:id>")
# 'Remove' a table item
def removeRelation(id):
    # Deletes a User (Remove)
    query = "DELETE FROM Players_Rosters WHERE playerRoster_id = '%s';"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/playersRosters")

@app.route("/editRelation/<int:id>", methods=["POST", "GET"])
# Enables 'Update' funtionality for User items
def editRelation(id):
    # Renders the update template
    if request.method == "GET":
        query = 'SELECT * FROM Players_Rosters WHERE playerRoster_id =%s' % (id)
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        relation_data = cursor.fetchall()

        query2 = "SELECT player_id FROM Players"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        player_data = cur.fetchall()

        query3 = "SELECT roster_id FROM Rosters"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        roster_data = cur.fetchall()

        return render_template("editPlayerRoster.j2", relation_data = relation_data, player_data = player_data, roster_data=roster_data)
    
    # Allows database user to change row information based on user_id selection (Update)
    if request.method == "POST":
        if request.form.get("editRelation"):
            id = request.form["pr_id"]
            player = request.form["player"]
            roster = request.form["roster"]

            query = "UPDATE Players_Rosters SET player_id = %s, roster_id = %s WHERE playerRoster_id = %s;"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (player, roster, id))
            mysql.connection.commit()
                
        return redirect("/playersRosters")
    
@app.route("/viewRoster/<int:id>")
# 'Remove' a table item
def viewRoster(id):
    # Deletes a User (Remove)
    query = "SELECT Players_Rosters.roster_id as ID, Rosters.roster_name as 'Roster Name', Players.player_name as Player, Players.team_id as Team FROM Players JOIN Players_Rosters ON Players.player_id = Players_Rosters.player_id JOIN Rosters ON Players_Rosters.roster_id = Rosters.roster_id WHERE Rosters.roster_id = %s;" % (id)
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    roster_data = cursor.fetchall()

    return render_template("viewRoster.j2", roster_data = roster_data)

@app.route("/viewTeam/<int:id>")  # BEING DEVELOPED
# 'Remove' a table item
def viewTeam(id):
    # Deletes a User (Remove)
    query = "SELECT Teams.team_id as ID, Teams.team_name as 'Team Name', Players.player_name as Player FROM Players JOIN Teams ON Players.team_id = Teams.team_id WHERE Teams.team_id = %s;" % (id)
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    team_data = cursor.fetchall()

    return render_template("viewTeam.j2", team_data = team_data)


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 53530)) 
    
    app.run(port=port, debug=True) 


