-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create Database
CREATE DATABASE tournament;

-- Connect to Database
\c tournament

-- Drop old Tables if exists
DROP TABLE IF EXISTS match;
DROP TABLE IF EXISTS player;

-- Create player Table if not exists
CREATE TABLE IF NOT EXISTS player(
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create match Table if not exists
CREATE TABLE IF NOT EXISTS match(
	id SERIAL PRIMARY KEY,
	player_1 int references player,
	player_2 int references player,
	the_winner int references player DEFAULT NULL,
	round_no int DEFAULT 1,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(player_1, player_2, round_no)
);
