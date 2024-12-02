-- Project Group 14 - Sayid Ali and Gilbert Keithline
-- Date: 11/07/2024
-- Data Manipulation Queries

-- Users

-- Retrieve Users (user_id, user_name, user_email)
SELECT user_id, user_name, user_email, user_password
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


-- Teams


-- Retrieve Teams (team_id, team_name, team_win, team_loss)
SELECT team_id, team_name, team_win, team_loss 
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
-- Will be activated by clicking the team name, which will be an HTML button
SELECT Teams.team_id, Teams.team_name, Players.player_name, 
        Players.point_stat, Players.assist_stat, Players.rebound_stat, 
        Players.block_stat, Players.steal_stat, Players.timePlayed_stat, 
        Players.injury_id, Players_Rosters.roster_id FROM Players
JOIN Teams ON Players.team_id = Teams.team_id
JOIN Players_Rosters ON Players.player_id = Players_Rosters.player_id
WHERE Teams.team_name = :teamNameSelection;

-- Players

-- Retrieve Players (player_id, player_name, stats)
SELECT player_id, player_name, point_stat, assist_stat, rebound_stat, block_stat, steal_stat, timePlayed_stat, team_id, injury_tag 
FROM Players;

-- Sort Players descending by stat
SELECT * FROM Players
ORDER BY Players.:statInput DESC;

-- Search by Player Name
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

-- Rosters

-- Retrieve Rosters (roster_id, roster_name, user_id)
SELECT roster_id, roster_name, user_id 
FROM Rosters;

-- Insert new Roster for a User
INSERT INTO Rosters (roster_name, user_id)
VALUES (:rosterNameInput, :userIDInput);

-- Update a Roster's name
UPDATE Rosters 
SET roster_name = :rosterNameInput, 
    user_id = :userIDInput
WHERE roster_id = :rosterIDInput;

-- Delete a Roster
DELETE FROM Rosters 
WHERE roster_id = :rosterIDInput;

-- Filter Players by Roster
-- Will be activated by clicking the roster name, which will be an HTML button
SELECT Players_Rosters.roster_id, Rosters.roster_name, Players.player_name, 
        Players.point_stat, Players.assist_stat, Players.rebound_stat, 
        Players.block_stat, Players.steal_stat, Players.timePlayed_stat, 
        Players.team_id, Players.injury_id FROM Players
JOIN Players_Rosters ON Players.player_id = Players_Rosters.player_id
JOIN Rosters ON Players_Rosters.roster_id = Rosters.roster_id
WHERE Rosters.roster_name = :rosterNameSelection;


-- Players_Rosters


-- Add Player to a Roster
INSERT INTO Players_Rosters (player_id, roster_id)
VALUES (:playerIDInput, :rosterIDInput);

-- Remove Player from a Roster
DELETE FROM Players_Rosters 
WHERE player_id = :playerIDInput AND roster_id = :rosterIDInput;


-- Injury_Status

-- Retrieve Injury Statuses (injury_id, injury_description)
SELECT injury_tag, injury_description 
FROM Injury_Status;

-- Insert new Injury Status
INSERT INTO Injury_Status (injury_tag, injury_description)
VALUES (:injuryIDInput, :injuryNameInput);

-- Update an Injury Status description
UPDATE Injury_Status 
SET injury_description = :injuryDescriptionInput
WHERE injury_id = :injuryIDInput;

-- Delete an Injury Status
DELETE FROM Injury_Status 
WHERE injury_id = :injuryIDInput;