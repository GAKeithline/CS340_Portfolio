-- Project Group 14 - Sayid Ali and Gilbert Keithline
-- Date: 11/07/2024
-- Data Manipulation Queries


-- =====================
-- USERS
-- =====================

-- Retrieve Users (user_id, user_name, user_email)
SELECT user_id as ID, user_name as Name, user_email as 'Email Address', user_password as Password
FROM Users;

-- Insert new User
INSERT INTO Users (user_name, user_email, user_password)
VALUES (:userNameInput, :emailInput, :passwordInput);

-- Update a User's information
UPDATE Users
SET user_name = :userNameInput, 
    user_email = :emailInput, 
    user_password = :passwordInput
WHERE user_id = :userIDInput;

-- Delete a User
DELETE FROM Users 
WHERE user_id = :userIDInput;


-- =====================
-- TEAMS
-- =====================

-- Retrieve Teams (team_id, team_name, team_win, team_loss)
SELECT team_id as ID, team_name as 'Team Name', team_win as Wins, team_loss as Losses
FROM Teams;

-- Insert new Team
INSERT INTO Teams (team_name, team_win, team_loss)
VALUES (:teamNameInput, :winInput, :lossInput);

-- Update a Team's record
UPDATE Teams
SET team_name = :teamNameInput, 
    team_win = :winInput, 
    team_loss = :lossInput
WHERE team_id = :teamIDInput;

-- Delete a Team
DELETE FROM Teams 
WHERE team_id = :teamIDInput;

-- Filter players by team
-- Will be activated by clicking the 'View Team' button in the Teams table
SELECT Teams.team_id as ID, Teams.team_name as 'Team Name', Players.player_name as Player, 
FROM Players
JOIN Teams ON Players.team_id = Teams.team_id
WHERE Teams.team_id = :teamIDSelection;


-- =====================
-- Players
-- =====================

-- Retrieve Players (player_id, player_name, stats)
SELECT player_id as ID, player_name as 'Player Name', point_stat as Points, assist_stat as Assists, 
        rebound_stat as Rebounds, block_stat as Blocks, steal_stat as Steals, timePlayed_stat as Minutes, team_id as Team, injury_tag as 'Injury Status'
FROM Players;

-- Sort Players descending by stat
-- Ultimately not implemented. But would be pretty easy to write in by making the table heads into href links
SELECT * FROM Players
ORDER BY Players.:statInput DESC;

-- Search by Player Name
-- Ultimately not implemented.
SELECT * FROM Players
WHERE Players.player_name = :playerNameInput;

-- Insert new Player into a Team
INSERT INTO Players (player_name, point_stat, assist_stat, rebound_stat, block_stat, steal_stat, timePlayed_stat, team_id, injury_id)
VALUES (:playerNameInput, :pointsInput, :assistsInput, :reboundsInput, :blocksInput, :stealsInput, :timePlayedInput, :teamIDInput, :injuryIDInput);

-- Update Player's stats
UPDATE Players
SET player_name = :playerNameInput, 
    point_stat = :pointsInput, 
    assist_stat = :assistsInput, 
    rebound_stat = :reboundsInput, 
    block_stat = :blocksInput, 
    steal_stat = :stealsInput, 
    timePlayed_stat = :timePlayedInput, 
    team_id = :teamIDInput, 
    injury_id = :injuryIDInput
WHERE player_id = :playerIDInput;

-- Delete a Player
DELETE FROM Players 
WHERE player_id = :playerIDInput;


-- =====================
-- ROSTERS
-- =====================

-- Retrieve Rosters (roster_id, roster_name, user_id)
SELECT roster_id as ID, roster_name as 'Roster Name', user_id as User
FROM Rosters;

-- Insert new Roster for a User
INSERT INTO Rosters (roster_name, user_id)
VALUES (:rosterNameInput, :userIDInput);

-- Update a Roster's information
UPDATE Rosters 
SET roster_name = :rosterNameInput, 
    user_id = :userIDInput
WHERE roster_id = :rosterIDInput;

-- Delete a Roster
DELETE FROM Rosters 
WHERE roster_id = :rosterIDInput;

-- Filter Players by Roster
-- Will be activated by clicking the 'View Roster' button in the Rosters table.
SELECT Players_Rosters.roster_id as ID, Rosters.roster_name as 'Roster name', Players.player_name as Player, 
FROM Players
JOIN Players_Rosters ON Players.player_id = Players_Rosters.player_id
JOIN Rosters ON Players_Rosters.roster_id = Rosters.roster_id
WHERE Rosters.roster_name = :rosterNameSelection;


-- =====================
-- Players_Rosters
-- =====================

-- Display intersection table
SELECT playerRoster_id as ID, player_id as 'Player ID', roster_id as 'Roster ID' 
FROM Players_Rosters;

-- Add Player to a Roster
INSERT INTO Players_Rosters (player_id, roster_id)
VALUES (:playerIDInput, :rosterIDInput);

-- Remove Player from a Roster
DELETE FROM Players_Rosters 
WHERE playerRoster_id = :playerRosterIDInput;


-- =====================
-- Injury_Status
-- =====================

-- Retrieve Injury Statuses (injury_id, injury_tag, injury_description)
SELECT injury_id as ID, injury_tag as Tag, injury_description as 'Status Description' 
FROM Injury_Status;

-- Insert new Injury Status
INSERT INTO Injury_Status (injury_tag, injury_description)
VALUES (:injuryTagInput, :injuryDescriptionInput);

-- Update an Injury Status description
UPDATE Injury_Status 
SET injury_tag = :injuryTagInput, injury_description = :injuryDescriptionInput
WHERE injury_id = :injuryIDInput;

-- Delete an Injury Status
DELETE FROM Injury_Status 
WHERE injury_id = :injuryIDInput;