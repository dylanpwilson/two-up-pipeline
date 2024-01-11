USE football;

-- DROP TABLE matches_scrapped_data;
-- CREATE TABLE matches_scrapped_data (
--     id INT PRIMARY KEY AUTO_INCREMENT,
-- 	match_date VARCHAR(100) NOT NULL,
--     match_time VARCHAR(20) NOT NULL,
--     league VARCHAR(100) NOT NULL,
--     home_team VARCHAR(200) NOT NULL,
--     away_team VARCHAR(200) NOT NULL,
--     final_score VARCHAR(20) NOT NULL,
--     goals VARCHAR(1000)
);

CREATE TABLE matches (
    id INT PRIMARY KEY AUTO_INCREMENT,
	match_date DATETIME,
    country VARCHAR(100),
    league VARCHAR(100),
    season VARCHAR(9),
    round INT,
    home_team VARCHAR(100),
    away_team VARCHAR(100),
    winner VARCHAR(4),
    home_score INT,
    away_score INT,
    CONSTRAINT uc_matches UNIQUE (match_date, home_team, away_team)
);


