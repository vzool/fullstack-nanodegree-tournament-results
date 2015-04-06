## Full-Stack Nanodegree Tournament Results

This is a python tournament functions working with a Database as a Back-End.

## File Structure

I organized the project with considerations based on trustful functionality.

```
	tournament.py		(Query functions)
	tournament.sql		(Database Tournament Database SQL)
	tournament_test.py	(Test Functions)
```
## Database Structure

```

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql tournament 
psql (9.3.6)
Type "help" for help.

tournament=> \d player
                                     Table "public.player"
   Column   |            Type             |                      Modifiers                      
------------+-----------------------------+-----------------------------------------------------
 id         | integer                     | not null default nextval('player_id_seq'::regclass)
 name       | text                        | not null
 created_at | timestamp without time zone | default now()
Indexes:
    "player_pkey" PRIMARY KEY, btree (id)
    "player_name_key" UNIQUE CONSTRAINT, btree (name)
Referenced by:
    TABLE "match" CONSTRAINT "match_player_1_fkey" FOREIGN KEY (player_1) REFERENCES player(id)
    TABLE "match" CONSTRAINT "match_player_2_fkey" FOREIGN KEY (player_2) REFERENCES player(id)
    TABLE "match" CONSTRAINT "match_the_winner_fkey" FOREIGN KEY (the_winner) REFERENCES player(id)

tournament=> \d match
                                     Table "public.match"
   Column   |            Type             |                     Modifiers                      
------------+-----------------------------+----------------------------------------------------
 id         | integer                     | not null default nextval('match_id_seq'::regclass)
 player_1   | integer                     | 
 player_2   | integer                     | 
 the_winner | integer                     | 
 round_no   | integer                     | default 1
 created_at | timestamp without time zone | default now()
Indexes:
    "match_pkey" PRIMARY KEY, btree (id)
    "match_player_1_player_2_round_no_key" UNIQUE CONSTRAINT, btree (player_1, player_2, round_no)
Foreign-key constraints:
    "match_player_1_fkey" FOREIGN KEY (player_1) REFERENCES player(id)
    "match_player_2_fkey" FOREIGN KEY (player_2) REFERENCES player(id)
    "match_the_winner_fkey" FOREIGN KEY (the_winner) REFERENCES player(id)



```

## Instructions

To Test those functions you will need to type the following:

### First import the SQL file into psql

```
$ psql -f tournament.sql
```

### Finally do this
```
$ python tournament_test.py
```

## Requirements

- You will need a Python 2.x language installed in your system.
- PostgreSQL 9.3+


## Licence

It's Completely Free. But, Do whatever you like to do on your own full responsibility;

This licence is known with [MIT License](http://vzool.mit-license.org/) in professional networks.
