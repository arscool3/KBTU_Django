from fastapi import HTTPException

def get_current_user():
    user = "admin"  # Simulated user fetching logic
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
