import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.bot_token = os.getenv("BOT_TOKEN")