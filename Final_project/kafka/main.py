from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pdf_generator.main import get_statgov_data_raw
import uvicorn
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql
import json

from pdf_generator.producer import add_data_to_aggregated_queue

app = FastAPI(title = "e-Gov")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

load_dotenv()

db_config = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
}

def check_in_database(bin: str):
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
            print(result)
    
    return result

@app.get("/process_bin")
async def process_bin(bin: str):
    data  = get_statgov_data_raw(BIN=bin)
    if data is None or data.get('error') is not None or data.get('obj') is None:
        raise HTTPException(status_code=404, detail="Bin not found")

    name = data.get('obj').get('name')
    return {"bin": bin, "name": name}

@app.post("/get_data")
async def process_data(bin: str, user: str):
    database_result = check_in_database(bin)

    if len(database_result) != 0:
        print(database_result)
        user_data = json.loads(user)
        user_data["bin"] = bin
        await add_data_to_aggregated_queue(database_result[0][2], json.dumps(user_data))
        return
    from producer_file import add_data_to_aggregating_queue
    await add_data_to_aggregating_queue(bin, user)


if __name__ == "__main__":

    uvicorn.run(app, host="172.20.10.5", port=1214)

