from fastapi import FastAPI, HTTPException
import database

app = FastAPI()

@app.post("/users/")
def create_user(username: str, email: str):
    conn = database.create_connection()
    query = "INSERT INTO users (username, email) VALUES (?, ?)"
    database.execute_query(conn, query, (username, email))
    conn.close()
    return {"username": username, "email": email}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    conn = database.create_connection()
    query = "SELECT * FROM users WHERE id = ?"
    user = database.fetch_all(conn, query, (user_id,))
    conn.close()
    if user:
        return user[0]
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/posts/")
def create_post(title: str, content: str, owner_id: int):
    conn = database.create_connection()
    query = "INSERT INTO posts (title, content, owner_id) VALUES (?, ?, ?)"
    database.execute_query(conn, query, (title, content, owner_id))
    conn.close()
    return {"title": title, "content": content, "owner_id": owner_id}

@app.get("/posts/{post_id}")
def read_post(post_id: int):
    conn = database.create_connection()
    query = "SELECT * FROM posts WHERE id = ?"
    post = database.fetch_all(conn, query, (post_id,))
    conn.close()
    if post:
        return post[0]
    raise HTTPException(status_code=404, detail="Post not found")
