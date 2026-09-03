from dotenv import load_dotenv

import os

load_dotenv()


class Settings:

    SMTP_SERVER = os.getenv("SMTP_SERVER")

    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

    SMTP_USER = os.getenv("SMTP_USER")

    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


settings = Settings()