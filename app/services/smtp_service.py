import smtplib

from email.mime.text import MIMEText

from app.config.settings import settings

from app.utils.exceptions import (
    SMTPConfigurationError,
    EmailSendingError
)


def send_email(
    email: str,
    subject: str,
    message: str
):

    if not settings.SMTP_SERVER:
        raise SMTPConfigurationError(
            "SMTP server is missing."
        )

    if not settings.SMTP_USER:
        raise SMTPConfigurationError(
            "SMTP username is missing."
        )

    if not settings.SMTP_PASSWORD:
        raise SMTPConfigurationError(
            "SMTP password is missing."
        )

    try:

        msg = MIMEText(message, "html")

        msg["Subject"] = subject

        msg["From"] = settings.SMTP_USER

        msg["To"] = email

        with smtplib.SMTP(
            settings.SMTP_SERVER,
            settings.SMTP_PORT
        ) as server:

            server.starttls()

            server.login(
                settings.SMTP_USER,
                settings.SMTP_PASSWORD
            )

            server.send_message(msg)

        return True

    except smtplib.SMTPAuthenticationError:

        raise EmailSendingError(
            "Invalid SMTP username or password."
        )

    except Exception as e:

        raise EmailSendingError(str(e))