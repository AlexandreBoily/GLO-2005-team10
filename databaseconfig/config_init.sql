CREATE DATABASE IF NOT EXISTS EsportsWiki;
USE EsportsWiki;

CREATE TABLE IF NOT EXISTS GAMES(
    id smallint auto_increment,
    game_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS LEAGUES(
    shorthand CHAR(10),
    name VARCHAR(50) NOT NULL,
    max_no_teams SMALLINT NOT NULL,
    description TEXT,
    region VARCHAR(50) DEFAULT 'Global',
    prize_pool DECIMAL(15,2) DEFAULT 0,
    online BOOLEAN DEFAULT 0,
    game_id smallint REFERENCES GAMES(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    rules_id smallint REFERENCES RULES(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL,
    PRIMARY KEY (shorthand)
);

CREATE TABLE IF NOT EXISTS RULES(
    id smallint AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL ,
    description TEXT,
    no_teams_per_match SMALLINT NOT NULL ,
    no_players_per_teams SMALLINT NOT NULL,
    game_id SMALLINT NOT NULL REFERENCES GAMES(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE ,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS TEAMS(
    id SMALLINT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    organization_id smallint REFERENCES ORGANIZATION(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ORGANIZATION(
    id smallint AUTO_INCREMENT,
    name VARCHAR(50),
    logo VARCHAR(200),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS PLAYERS(
    id SMALLINT AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    alias VARCHAR(50) NOT NULL ,
    nationality SMALLINT REFERENCES settingsNationalities(NationalityID)
        ON UPDATE CASCADE
        ON DELETE CASCADE ,
    team_id smallint,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS TEAMS_LEAGUES(
    team_id SMALLINT NOT NULL REFERENCES TEAMS(id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    league_id VARCHAR(50) NOT NULL REFERENCES LEAGUES(shorthand)
        ON UPDATE CASCADE
        ON DELETE NO ACTION ,
    result SMALLINT
);

CREATE TABLE IF NOT EXISTS PLAYERS_TEAMS(
    player_id SMALLINT NOT NULL REFERENCES PLAYERS(id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    team_id SMALLINT NOT NULL REFERENCES TEAMS(id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    start DATE,
    end DATE
);

#Nationality table creation taken from https://www.rmtweb.co.uk/sql-nationalities-table-sql-format
CREATE TABLE settingsNationalities(
`NationalityID` int(11) NOT NULL AUTO_INCREMENT,
`Nationality` varchar(200) DEFAULT NULL,
PRIMARY KEY (`NationalityID`)
);
INSERT INTO settingsNationalities VALUES (1,'Afghan'),(2,'Albanian'),(3,'Algerian'),(4,'American'),(5,'Andorran'),(6,'Angolan'),(7,'Antiguans'),(8,'Argentinean'),(9,'Armenian'),(10,'Australian'),(11,'Austrian'),(12,'Azerbaijani'),(13,'Bahamian'),(14,'Bahraini'),(15,'Bangladeshi'),(16,'Barbadian'),(17,'Barbudans'),(18,'Batswana'),(19,'Belarusian'),(20,'Belgian'),(21,'Belizean'),(22,'Beninese'),(23,'Bhutanese'),(24,'Bolivian'),(25,'Bosnian'),(26,'Brazilian'),(27,'British'),(28,'Bruneian'),(29,'Bulgarian'),(30,'Burkinabe'),(31,'Burmese'),(32,'Burundian'),(33,'Cambodian'),(34,'Cameroonian'),(35,'Canadian'),(36,'Cape Verdean'),(37,'Central African'),(38,'Chadian'),(39,'Chilean'),(40,'Chinese'),(41,'Colombian'),(42,'Comoran'),(43,'Congolese'),(44,'Congolese'),(45,'Costa Rican'),(46,'Croatian'),(47,'Cuban'),(48,'Cypriot'),(49,'Czech'),(50,'Danish'),(51,'Djibouti'),(52,'Dominican'),(53,'Dominican'),(54,'Dutch'),(55,'Dutchman'),(56,'Dutchwoman'),(57,'East Timorese'),(58,'Ecuadorean'),(59,'Egyptian'),(60,'Emirian'),(61,'Equatorial Guinean'),(62,'Eritrean'),(63,'Estonian'),(64,'Ethiopian'),(65,'Fijian'),(66,'Filipino'),(67,'Finnish'),(68,'French'),(69,'Gabonese'),(70,'Gambian'),(71,'Georgian'),(72,'German'),(73,'Ghanaian'),(74,'Greek'),(75,'Grenadian'),(76,'Guatemalan'),(77,'Guinea-Bissauan'),(78,'Guinean'),(79,'Guyanese'),(80,'Haitian'),(81,'Herzegovinian'),(82,'Honduran'),(83,'Hungarian'),(84,'I-Kiribati'),(85,'Icelander'),(86,'Indian'),(87,'Indonesian'),(88,'Iranian'),(89,'Iraqi'),(90,'Irish'),(91,'Irish'),(92,'Israeli'),(93,'Italian'),(94,'Ivorian'),(95,'Jamaican'),(96,'Japanese'),(97,'Jordanian'),(98,'Kazakhstani'),(99,'Kenyan'),(100,'Kittian and Nevisian'),(101,'Kuwaiti'),(102,'Kyrgyz'),(103,'Laotian'),(104,'Latvian'),(105,'Lebanese'),(106,'Liberian'),(107,'Libyan'),(108,'Liechtensteiner'),(109,'Lithuanian'),(110,'Luxembourger'),(111,'Macedonian'),(112,'Malagasy'),(113,'Malawian'),(114,'Malaysian'),(115,'Maldivan'),(116,'Malian'),(117,'Maltese'),(118,'Marshallese'),(119,'Mauritanian'),(120,'Mauritian'),(121,'Mexican'),(122,'Micronesian'),(123,'Moldovan'),(124,'Monacan'),(125,'Mongolian'),(126,'Moroccan'),(127,'Mosotho'),(128,'Motswana'),(129,'Mozambican'),(130,'Namibian'),(131,'Nauruan'),(132,'Nepalese'),(133,'Netherlander'),(134,'New Zealander'),(135,'Ni-Vanuatu'),(136,'Nicaraguan'),(137,'Nigerian'),(138,'Nigerien'),(139,'North Korean'),(140,'Northern Irish'),(141,'Norwegian'),(142,'Omani'),(143,'Pakistani'),(144,'Palauan'),(145,'Panamanian'),(146,'Papua New Guinean'),(147,'Paraguayan'),(148,'Peruvian'),(149,'Polish'),(150,'Portuguese'),(151,'Qatari'),(152,'Romanian'),(153,'Russian'),(154,'Rwandan'),(155,'Saint Lucian'),(156,'Salvadoran'),(157,'Samoan'),(158,'San Marinese'),(159,'Sao Tomean'),(160,'Saudi'),(161,'Scottish'),(162,'Senegalese'),(163,'Serbian'),(164,'Seychellois'),(165,'Sierra Leonean'),(166,'Singaporean'),(167,'Slovakian'),(168,'Slovenian'),(169,'Solomon Islander'),(170,'Somali'),(171,'South African'),(172,'South Korean'),(173,'Spanish'),(174,'Sri Lankan'),(175,'Sudanese'),(176,'Surinamer'),(177,'Swazi'),(178,'Swedish'),(179,'Swiss'),(180,'Syrian'),(181,'Taiwanese'),(182,'Tajik'),(183,'Tanzanian'),(184,'Thai'),(185,'Togolese'),(186,'Tongan'),(187,'Trinidadian or Tobagonian'),(188,'Tunisian'),(189,'Turkish'),(190,'Tuvaluan'),(191,'Ugandan'),(192,'Ukrainian'),(193,'Uruguayan'),(194,'Uzbekistani'),(195,'Venezuelan'),(196,'Vietnamese'),(197,'Welsh'),(198,'Yemenite'),(199,'Zambian'),(200,'Zimbabwean');


DELIMITER //

CREATE TRIGGER generate_default_teams_result
BEFORE INSERT
   ON TEAMS_LEAGUES FOR EACH ROW

BEGIN

    declare n int;
    if NEW.result is null then
        select count(team_id) into n from TEAMS_LEAGUES where new.league_id = league_id;
        set new.result = n + 1;
    end if;

END //

DELIMITER ;

LOAD DATA INFILE '/var/lib/mysql-files/games_data.csv' INTO TABLE GAMES
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (game_name);

LOAD DATA INFILE '/var/lib/mysql-files/leagues_data.csv' INTO TABLE LEAGUES
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql-files/players_data.csv' INTO TABLE PLAYERS
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (first_name,last_name,alias,nationality,team_id);

LOAD DATA INFILE '/var/lib/mysql-files/rules_data.csv' INTO TABLE RULES
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (name,description,no_teams_per_match,no_players_per_teams,game_id);

LOAD DATA INFILE '/var/lib/mysql-files/organization_data.csv' INTO TABLE ORGANIZATION
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (name,logo);

LOAD DATA INFILE '/var/lib/mysql-files/teams_data.csv' INTO TABLE TEAMS
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (name,organization_id);

LOAD DATA INFILE '/var/lib/mysql-files/players_team_data.csv' INTO TABLE PLAYERS_TEAMS
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql-files/teams_league_data.csv' INTO TABLE TEAMS_LEAGUES
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;


