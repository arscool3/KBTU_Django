class Config:
    def __init__(self):
        self.secret_key = "super_secret_key"

def get_config():
    return Config()
