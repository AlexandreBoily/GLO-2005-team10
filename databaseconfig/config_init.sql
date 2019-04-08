CREATE DATABASE IF NOT EXISTS EsportsWiki;
USE EsportsWiki;

CREATE TABLE IF NOT EXISTS GAMES(
    id smallint NOT NULL,
    game_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS LEAGUES(
    shorthand CHAR(10) NOT NULL,
    name VARCHAR(50),
    max_no_teams SMALLINT,
    description TEXT,
    region VARCHAR(50),
    prize_pool DECIMAL(15,2),
    online BOOLEAN,
    game_id VARCHAR(50),
    PRIMARY KEY (shorthand)
);

CREATE TABLE IF NOT EXISTS RULES(
    name VARCHAR(50) NOT NULL ,
    description TEXT,
    no_teams_per_match SMALLINT NOT NULL ,
    no_players_per_teams SMALLINT NOT NULL,
    league_id VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS TEAMS(
    name VARCHAR(50) NOT NULL ,
    solo BOOLEAN NOT NULL,
    id SMALLINT NOT NULL,
    league_id VARCHAR(50) NOT NULL ,
    organization_name VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ORGANIZATION(
    name VARCHAR(50) NOT NULL,
    logo VARCHAR(200),
    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS PLAYERS(
    id SMALLINT NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    alias VARCHAR(50) NOT NULL ,
    nationality SMALLINT,
    team_id smallint,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS TEAMS_LEAGUES(
    team_id SMALLINT NOT NULL,
    league_id VARCHAR(50) NOT NULL
);

LOAD DATA INFILE '/var/lib/mysql-files/games_data.txt' INTO TABLE GAMES
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql-files/leagues_data.txt' INTO TABLE LEAGUES
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql-files/players_data.csv' INTO TABLE PLAYERS
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;

DELIMITER //

CREATE TRIGGER teams_before_insert
BEFORE INSERT
   ON TEAMS FOR EACH ROW

BEGIN

   DECLARE n smallint;
   DECLARE na varchar(50);

   SELECT no_players_per_teams into n from RULES where league_id = NEW.league_id;

   if n = 1 then
       SET NEW.solo = true;
   else
       SET  NEW.solo = false;
   end if;

   if NEW.solo then
       SELECT alias into na from PLAYERS where team_id = NEW.id;
   else
       SELECT name into na from ORGANIZATION where name = NEW.organization_name;
   end if;

   SET NEW.name = na;

END //

DELIMITER ;
