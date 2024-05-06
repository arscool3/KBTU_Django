import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("blog.db")
    except Error as e:
        print(e)
    return conn

def execute_query(conn, query, args=None):
    try:
        cursor = conn.cursor()
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        conn.commit()
    except Error as e:
        print(e)

def fetch_all(conn, query, args=None):
    try:
        cursor = conn.cursor()
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Error as e:
        print(e)
        return []

def initialize_db():
    conn = create_connection()
    table_creation_queries = [
        """ CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE
            ); """,
        """ CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                owner_id INTEGER NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES users (id)
            ); """,
        """ CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                post_id INTEGER NOT NULL,
                FOREIGN KEY (post_id) REFERENCES posts (id)
            ); """
    ]
    for query in table_creation_queries:
        execute_query(conn, query)
    conn.close()

initialize_db()
