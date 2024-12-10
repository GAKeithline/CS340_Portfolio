-- Project Group 14 - Sayid Ali and Gilbert Keithline 
-- Date: 10/29/2024
-- Source URL: https://canvas.oregonstate.edu/courses/1976520/pages/activity-1-creating-a-customer-object-table?module_item_id=24719034

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Players_Rosters;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Rosters;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS Injury_Status;


-- ========================
-- TABLE CREATION
-- ========================

-- Create Injury_Status Table
CREATE OR REPLACE TABLE Injury_Status (
    injury_id int NOT NULL AUTO_INCREMENT,
    injury_tag varchar(5) NOT NULL UNIQUE,
    injury_description varchar(145),
    PRIMARY KEY (injury_id)

);

-- Create Users Table
CREATE OR REPLACE TABLE Users (
    user_id int NOT NULL AUTO_INCREMENT,
    user_name varchar(145) NOT NULL,
    user_email varchar(145) NOT NULL,
    user_password varchar(145) NOT NULL,
    PRIMARY KEY (user_id),
    UNIQUE(user_email)
);

-- Create Teams Table
CREATE OR REPLACE TABLE Teams (
    team_id int NOT NULL AUTO_INCREMENT,
    team_name varchar(45) NOT NULL,
    team_win int,
    team_loss int,
    PRIMARY KEY (team_id)
);

-- Create Rosters Table
CREATE OR REPLACE TABLE Rosters (
    roster_id int NOT NULL AUTO_INCREMENT,
    roster_name varchar(255) NOT NULL,
    user_id int,
    PRIMARY KEY (roster_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- Create Players Table
CREATE OR REPLACE TABLE Players (
    player_id int NOT NULL AUTO_INCREMENT,
    player_name varchar(45) NOT NULL,
    point_stat int DEFAULT NULL,
    assist_stat int DEFAULT NULL,
    rebound_stat int DEFAULT NULL,
    block_stat int DEFAULT NULL,
    steal_stat int DEFAULT NULL,
    timePlayed_stat int DEFAULT NULL,
    team_id int,
    injury_id varchar(10),
    PRIMARY KEY (player_id),
    FOREIGN KEY (team_id) REFERENCES Teams(team_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL,
    FOREIGN KEY (injury_id) REFERENCES Injury_Status(injury_tag)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- Create Players_Rosters Table
CREATE OR REPLACE TABLE Players_Rosters (
    playerRoster_id int NOT NULL AUTO_INCREMENT,
    player_id int,
    roster_id int,
    PRIMARY KEY (playerRoster_id),
    FOREIGN KEY (player_id) REFERENCES Players(player_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (roster_id) REFERENCES Rosters(roster_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- =====================================================
-- Insert example data into tables
-- =====================================================

-- Insert data into Injury_Status Table
INSERT INTO Injury_Status (injury_tag, injury_description) VALUES
('NULL', 'Player is healthy.'),
('QUES', 'Questionable: Player is day to day. Likely to play, but may sit out.'),
('DOUBT', 'Doubtful: Player is unlikely to play, possibly could.'),
('OUT', 'Out: Player is not playing this week.'),
('IR', 'Injured Reserve: Player is dealing with a major injury and will miss significant time.');


-- Insert data into Users Table
INSERT INTO Users (user_name, user_email, user_password) VALUES
('Alex Keithline', 'keithlig@oregonstate.edu', '123456'),
('Sayid Ali', 'als@oregonstate.edu', '654321'),
('Some Dude', 'some.dude@gmail.com', '123321'),
('Some Lady', 'some.lady@msn.com', '321123'),
('Sonic the Hedgehog', 'gottaGoFast@speed.org', 'zoomzoom');

-- Insert data into Teams Table
INSERT INTO Teams (team_id, team_name, team_win, team_loss) VALUES
(11, 'Milwaukee Bucks', 12, 11),
(12, 'Los Angeles Lakers', 33, 11),
(13, 'Minnesota Timberwolves', 12, 11),
(14, 'Cleveland Cavaliers', 21, 4),
(15, 'Portland Trail Blazers', 8, 16);

-- Insert data into Rosters Table
INSERT INTO Rosters (roster_id, roster_name, user_id) VALUES
(8, 'Globetrotters', 2),
(9, 'Moonwalkers', 4),
(10, 'Astrosteppers', 1),
(11, 'Galaxyjoggers', 5);

-- Insert data into Players Table
INSERT INTO Players (player_id, player_name, point_stat, assist_stat, rebound_stat, block_stat, steal_stat, timePlayed_stat, team_id, injury_id) VALUES
(1, 'Lebron James', 23, 9, 8, 1, 1, 35, 12, NULL),
(2, 'Anthony Edwards', 27, 4, 6, 1, 1, 36, 13, 'QUES'),
(3, 'Khris Middleton', 11, 6, 3, 1, 1, 22, 11, 'QUES'),
(4, 'Dean Wade', 6, 2, 5, NULL, 1, 22, 14, NULL),
(5, 'Anthony Davis', 28, 4, 11, 2, 1, 36, 12, 'NULL'),
(6, 'Rudy Gobert', 11, 2, 11, 2, 1, 34, 13, 'NULL'),
(7, 'Giannis Antetokounmpo', 33, 6, 12, 1, 1, 35, 11, 'DOUBT'),
(8, 'Georges Niang', 8, 1, 4, NULL, NULL, 21, 14, 'NULL'),
(9, 'Scoot Henderson', 12, 5, 3, 0, 1, 26, 15, 'NULL'),
(10, 'Robert Williams III', 10, 1, 6, 2, 1, 19, 15, 'OUT');

-- Insert data into Players_Rosters Table
INSERT INTO Players_Rosters (playerRoster_id, roster_id, player_id) VALUES
(1, 10, 7),
(2, 10, 10),
(3, 10, 6),
(4, 9, 3),
(5, 9, 9),
(6, 8, 1),
(7, 11, 2),
(8, 8, 4);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;