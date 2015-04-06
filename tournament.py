#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    con = connect()
    cmd = con.cursor()
    cmd.execute("DELETE FROM match;")
    con.commit()
    con.close()


def deletePlayers():
    """Remove all the player records from the database."""
    con = connect()
    cmd = con.cursor()
    cmd.execute("DELETE FROM player;")
    con.commit()
    con.close()


def countPlayers():
    """Returns the number of players currently registered."""
    con = connect()
    cmd = con.cursor()
    cmd.execute("SELECT count(*) as number FROM player;")
    record = cmd.fetchall()
    con.close()
    return record[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    con = connect()
    cmd = con.cursor()
    cmd.execute("INSERT INTO player(name) VALUES(%s);", (name, ))
    con.commit()
    con.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    con = connect()
    cmd = con.cursor()
    cmd.execute("""SELECT   id,
                            name,
                            (select count(*) from match where the_winner = player.id) as wins,
                            (select count(*) from match where player.id = player_1 or player.id = player_2) as matches
                    FROM player
                    ORDER BY wins DESC, created_at;
                """)

    record = cmd.fetchall()
    con.close()
    return record


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    con = connect()
    cmd = con.cursor()
    cmd.execute("INSERT INTO match(player_1, player_2, the_winner) VALUES(%s, %s, %s);", (loser, winner, winner, ))
    con.commit()
    con.close()
 
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    con = connect()
    cmd = con.cursor()
    cmd.execute("""SELECT id, name
                    FROM player 
                    WHERE id in (
                        SELECT the_winner
                        FROM match
                    )

                    UNION ALL

                    SELECT id, name FROM player
                    WHERE id not in(
                        SELECT the_winner FROM match
                    );
                """)

    record = cmd.fetchall()
    con.close()
    result = []
    for row in chunks(record, 2):
        result.append(row[0] + row[1])

    return result
