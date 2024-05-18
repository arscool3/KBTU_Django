import uuid
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta

load_dotenv()

db_config = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
}
def make_database_record(data, file_path):
    with psycopg2.connect(**db_config) as conn:

        with conn.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO pdf (id, bin, file_path, begin_date, end_date)
                VALUES ({}, {}, {}, {}, {})
            """).format(
                sql.Literal(str(uuid.uuid4())),
                sql.Literal(data['bin']),
                sql.Literal(file_path),
                sql.Literal(datetime.now()),
                sql.Literal(datetime.now() + timedelta(days=1))
            )

            cursor.execute(insert_query)

def check_in_database(bin: str) -> bool:
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT * 
                FROM pdf 
                WHERE bin = {} 
                AND (NOW() - BEGIN_DATE) <= INTERVAL '1 day'
            """).format(sql.Literal(bin))
            cursor.execute(select_query)
            result = cursor.fetchall()
    
    return len(result) > 0