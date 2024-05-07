from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBearer

app = FastAPI()


def get_query_token(token: str):
    if token != "KBTU_Django":
        raise HTTPException(status_code=400, detail="No auth token")
    return token


class TokenChecker:
    def __init__(self, token: str = Depends(get_query_token)):
        self.token = token

    def check_token(self):
        if self.token != "KBTU_FastAPI":
            raise HTTPException(status_code=400, detail="Invalid token")
        return self.token


basic_auth = HTTPBasic()
oauth2_scheme = HTTPBearer()


@app.get("/token/")
async def get_token(basic_auth_credentials: HTTPBasic = Depends(basic_auth),
                    oauth2_token: str = Depends(oauth2_scheme),
                    token_checker: TokenChecker = Depends()):
    return {"detail": "Token successfully validated"}
