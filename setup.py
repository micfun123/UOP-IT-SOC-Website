import sqlite3
import os

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    description TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL,
    class_of INTEGER NOT NULL,
    level TEXT NOT NULL,
    bio TEXT NOT NULL,
    image TEXT NOT NULL,
    role TEXT,
    github TEXT,
    linkedin TEXT,
    twitter TEXT,
    website TEXT,
    mastodon TEXT    
)
''')