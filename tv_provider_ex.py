import sqlite3
import timeit
import csv
import os
#import pytest

def create_table(conn, cursor):
    cursor.execute('''
        CREATE TABLE channels (
        _id INTEGER PRIMARY KEY AUTOINCREMENT,
        package_name TEXT NOT NULL,
        input_id TEXT NOT NULL,
        type TEXT NOT NULL DEFAULT 'TYPE_OTHER',
        service_type TEXT NOT NULL DEFAULT 'SERVICE_TYPE_AUDIO_VIDEO',
        original_network_id INTEGER NOT NULL DEFAULT 0,
        transport_stream_id INTEGER NOT NULL DEFAULT 0,
        service_id INTEGER NOT NULL DEFAULT 0,
        display_number TEXT,
        display_name TEXT,
        network_affiliation TEXT,
        description TEXT,
        video_format TEXT,
        browsable INTEGER NOT NULL DEFAULT 0,
        searchable INTEGER NOT NULL DEFAULT 1,
        selectable INTEGER,
        locked INTEGER NOT NULL DEFAULT 0,
        app_link_icon_uri TEXT,
        app_link_poster_art_uri TEXT,
        app_link_text TEXT,
        app_link_color INTEGER,
        app_link_intent_uri TEXT,
        internal_provider_data BLOB,
        internal_provider_flag1 INTEGER,
        internal_provider_flag2 INTEGER,
        internal_provider_flag3 INTEGER,
        internal_provider_flag4 INTEGER,
        logo BLOB,
        version_number INTEGER,
        channel_genre TEXT,cam_channel INTEGER,
        UNIQUE(_id,package_name));
        ''')
    conn.commit()

def read_dummy():
    matrix = []
    f = open('D:/github/tv_provider_ex/tv_db.csv', 'r')
    csvReader = csv.reader(f)
    for row in csvReader:
        matrix.append(row)
    return matrix

def insert_records(conn, cursor, records):
    for row in records[1:]:
        cursor.execute('''
            INSERT INTO channels ('package_name', 'input_id', 'type',
                'service_type', 'original_network_id', 'transport_stream_id',
                'service_id', 'display_number', 'display_name')
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            ''', (row[1], row[2], row[3], row[4], row[5],
            row[6], row[7], row[8], row[9]))
    conn.commit()

def display_records(cursor):
    cursor.execute('''
        SELECT * FROM channels;
        ''')
    print(cursor.fetchall())

# open database
conn = sqlite3.connect('D:/github/tv_provider_ex/work_tv.db')
cursor = conn.cursor()

# initialize table
cursor.execute('''
    DROP TABLE channels;
    ''')
conn.commit()

# create table
create_table(conn, cursor)

# read dummy
dummy = read_dummy()

# insert data
insert_records(conn, cursor, dummy)

# display records
display_records(cursor)

conn.close()
