USE football;

CREATE TABLE matches_scrapped_data (
	match_date VARCHAR(100),
    match_time TIME,
    country VARCHAR(100),
    league VARCHAR(100),
    home_team VARCHAR(200),
    away_team VARCHAR(200),
    final_score VARCHAR(20),
    goals VARCHAR(1000)
);