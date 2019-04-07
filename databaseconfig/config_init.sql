CREATE DATABASE IF NOT EXISTS EsportsWiki;
USE EsportsWiki;

CREATE TABLE IF NOT EXISTS GAMES(
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS LEAGUES(
    name VARCHAR(50),
    shorthand CHAR(5) NOT NULL,
    max_no_teams SMALLINT,
    description TEXT,
    region VARCHAR(50),
    prize_pool DECIMAL(15,2),
    online BOOLEAN,
    game_name VARCHAR(50),
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

#GAMES
INSERT INTO GAMES (name) VALUES ("Dota 2");
INSERT INTO GAMES (name) VALUES ("Overwatch");
INSERT INTO GAMES (name) VALUES ("PUBG");
INSERT INTO GAMES (name) VALUES ("Brood War");
INSERT INTO GAMES (name) VALUES ("Heroes");
INSERT INTO GAMES (name) VALUES ("Counter-Strike");
INSERT INTO GAMES (name) VALUES ("Rocket League");
INSERT INTO GAMES (name) VALUES ("League of Legends");
INSERT INTO GAMES (name) VALUES ("Warcraft III");
INSERT INTO GAMES (name) VALUES ("Artifact");
INSERT INTO GAMES (name) VALUES ("Starcraft II");
INSERT INTO GAMES (name) VALUES ("Rainbow Six");
INSERT INTO GAMES (name) VALUES ("Smash");
INSERT INTO GAMES (name) VALUES ("Hearthstone");
INSERT INTO GAMES (name) VALUES ("Fortnite");
INSERT INTO GAMES (name) VALUES ("World of Warcraft");
INSERT INTO GAMES (name) VALUES ("Arena of Valor");
INSERT INTO GAMES (name) VALUES ("Quake");
INSERT INTO GAMES (name) VALUES ("Team Fortress");
INSERT INTO GAMES (name) VALUES ("CLash Royale");

#LEAGUES - DOTA 2
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("OGA Dota PIT Minor 2019", "Dota Pit", 8,
        "The OGA Dota PIT Minor 2019 is the seventh tournament by One Game Agency. Eight teams will fight for a $300,000 USD prize pool as well as qualification points for The International 2019",
        300000, false, "Dota 2");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("Cobx Masters 2019", "Cobx Masters", 6,
        "Cobx Masters 2019 Phase II is a six team international LAN tournament held at the Bombay Exhibition Centre, Mumbai, India in April 2019. Two international invites are joined by two qualifiers from India and two qualifiers from Southeast Asia to compete for a total prize pool of ₹ 7,000,000 INR (~$100,000 USD)",
        100000, false, "Dota 2");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("MDL Disneyland Paris Major", "Mars Dota 2 League", 16,
        "MDL will be hosting their first tournament outside of China ever, and what a venue to pick for this occasion: together with the Disneyland Paris Event Group, MDL presents the MDL Disneyland Paris Major, the fourth Major of the 2018-19 Dota Pro Circuit",
        1000000, false, "Dota 2");

#LEAGUES - OVERWATCH
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("Overwatch League - 2019", "OWL", 20,
        "The Overwatch League (OWL) is a professional esports league for the video game Overwatch, produced by its developer Blizzard Entertainment. The Overwatch League follows the model of other traditional North American professional sporting leagues by using a set of permanent, city-based teams backed by separate ownership groups.",
        5000000, false, "Overwatch");

#LEAGUES - PUBG
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("PUBG Europe League", "PUBG Europe League", 16,
        "PUBG Europe League is a PUBG professional league in Europe. The league represents Europe''s portion of 2019 Official competitive season held by PUBG Corporation. The 2019 competitive season will culminated at the PUBG Global Championship 2019.",
        225000, false, "PUBG");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("FACEIT Global Summit: PUBG Classic", "FACEIT Global Summit", 24,
        "The FACEIT Global Summit: PUBG Classic is the first Global Event of the 2019 circuit. Represents best teams from every region in Phase 1.",
        400000, false, "PUBG");

#LEAGUES - BROOD WAR
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("2019 Korea StarCraft League", "Korea StarCraft League", 16,
        "The 2019 Korea StarCraft League Season 3, or KSL Season 3, is an offline tournament, organized by Blizzard.",
        71719, false, "Brood War");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("Afreeca Starleague Season 7", "Afreeca Starleague", 24,
        "The Afreeca Starleague Season 7 or AfreecaTV Starcraft League Season 7, is an offline tournament broadcasted live on Afreeca, organized by Kongdoo and Afreeca. Qualifiers will begin at Seoul on the 2019-01-05.",
        100000, false, "Brood War");

#LEAGUES - HEROES
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("Agon League Season 3", "Agon League", 18,
        "Group Stage: two groups of 8 teams, round-robin, best-of-2 matches.",
        357.06, true, "Heroes");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("Heroes Lounge Division S Season 1 Europe", "Heroes Lounge Division S", 8,
        "The prize pool of Heroes Lounge Division S is fully crowdfunded on Matcherino with the money being split equally between the EU and NA leagues.",
        8067.50, true, "Heroes");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("Gold Series Heroes League 2019", "Gold Series Heroes League", 8,
        "Each player of the teams that won the Qualifier but not earned any prize money will receive 3,750 Gems on their Battle.Net account.",
        82250, true, "Heroes");

#LEAGUES - COUNTER-STRIKE
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("StarSeries & i-League CS:GO Season 7", "StarSeries", 16,
        "The StarSeries & i-League returns for its 7th Counter-Strike: Global Offensive Season. The tournament features an increased prize pool of $500,000 USD.",
        500000, false, "Counter-Strike");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("BLAST Pro Series: Miami 2019", "BLAST Pro Series", 6,
        "The BLAST Pro Standoff is a prize bonus showmatch, with five 1v1 aim duels.",
        250000, false, "Counter-Strike");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("Intel Extreme Masters Season XIV - Sydney", "Intel Extreme Masters", 16,
        "Two double-elimination format (GSL) Groups",
        250000, false, "Counter-Strike");

#LEAGUES - ROCKET LEAGUE
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("RLCS Season 7", "RLCS", 12,
        "RLCS Season 7 is the first RLCS season in 2019. This season marks the start of a partnership between Psyonix and ELEAGUE featuring ''wide-ranging'' content including a multi-part feature series on the RLCS on TBS Television.",
        529500, false, "Rocket League");

#LEAGUES - LEAGUE OF LEGENDS
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("LCS Spring 2019", "LCS", 10,
        "1st place team from Group Stage will select their opponent from Quarterfinals",
        200000, false, "League of Legends");
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("LEC Spring 2019", "LEC", 10,
        "Starting in 2019, teams that participate in the EU LCS will be there as permanent partners of the league.",
        200000, false, "League of Legends");

#LEAGUES - WARCRAFT III
INSERT INTO LEAGUES (name, shorthand, max_no_teams, description, prize_pool, online, game_name)
VALUES ("mTw Legendary Cup", "mTw Legendary Cup", 8,
        "The mTw Legendary Cup is a major tournament organized by team mTw and sponsored by Thermaltake that will take place in Berlin (Germany).",
        5331, false, "Warcraft III");