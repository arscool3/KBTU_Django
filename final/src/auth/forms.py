from fastapi import Form
from fastapi.security import OAuth2PasswordRequestForm

class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    def __init__(
        self,
        email: str = Form(...),
        password: str = Form(...),
        scope: str = Form(""),
        client_id: str = Form(None),
        client_secret: str = Form(None)
    ):
        super().__init__(username=email, password=password, scope=scope, client_id=client_id, client_secret=client_secret)
        self.email = email