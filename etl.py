import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from cassandra.cluster import Cluster
from queries import *

def process_song_by_session(file, session):
    
    session.execute(create_table_song_by_session)
    print('Processing song_by_session')
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            session.execute(insert_table_song_by_session, (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
        
def process_artist_by_id(file, session):
    
    session.execute(create_table_artist_by_id)
    print('Processing artist_by_id')
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            session.execute(insert_table_artist_by_id, (int(line[8]), int(line[10]), int(line[3]), line[0], line[9], line[1] +' '+ line[4]))

def process_song_by_user(file, session):
    
    session.execute(create_table_song_by_user)
    print('Processing song_by_user')
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            session.execute(insert_table_song_by_user, (line[1] +' '+ line[4], line[9]))


def process_event_data(file, session):
    process_song_by_session(file, session)
    process_artist_by_id(file, session)
    process_song_by_user(file, session)
    print('Finish')
if __name__ == '__main__':
    
    file = 'event_datafile_new.csv'

    cluster = Cluster(['127.0.0.1'])

    session = cluster.connect()

    session.execute("""CREATE KEYSPACE IF NOT EXISTS udacity WITH REPLICATION = { 
                      'class' : 'SimpleStrategy', 
                      'replication_factor' : 3   }
                    """)

    session.set_keyspace('udacity')

    process_event_data(file, session)