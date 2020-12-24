# CQL Queries for DROP and CREATE song_by_session table
drop_table_song_by_session = """DROP TABLE IF EXISTS song_by_session"""
create_table_song_by_session = """CREATE TABLE IF NOT EXISTS song_by_session (
                                    sessionId int, 
                                    itemInSession int,
                                    artist text,
                                    song text,
                                    length float,
                                    PRIMARY KEY ((sessionId, itemInSession))
                               )"""
query1 = "INSERT INTO song_by_session(sessionId, itemInSession, artist, song, length) "
insert_table_song_by_session = query1 + "VALUES (%s, %s, %s, %s, %s)"
        
# CQL Queries for DROP and CREATE artist_by_id table
drop_table_artist_by_id = """DROP TABLE IF EXISTS artist_by_id"""
create_table_artist_by_id = """CREATE TABLE IF NOT EXISTS artist_by_id (
                                sessionId int,
                                userId int,
                                itemInSession int,
                                artist text,
                                song text,
                                user text,
                                PRIMARY KEY ((sessionid, userId), itemInSession)
                            )"""
query2 = "INSERT INTO artist_by_id(sessionId, userId, itemInSession, artist, song, user) "
insert_table_artist_by_id = query2 + "VALUES (%s, %s, %s, %s, %s, %s)"
            
# CQL Queries for DROP and CREATE song_by_session table
drop_table_song_by_user = """DROP TABLE IF EXISTS song_by_user"""
create_table_song_by_user = """CREATE TABLE IF NOT EXISTS song_by_user (
                                username text,
                                song text,
                                PRIMARY KEY (song, username)
                            )"""
query3 = "INSERT INTO song_by_user(username, song) "
insert_table_song_by_user = query3 + "VALUES (%s, %s)"
            