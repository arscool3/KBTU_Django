from fastapi import Header, HTTPException

def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token

def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
    return token

class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
