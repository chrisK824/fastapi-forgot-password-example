import os
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
import logging
import ssl

logger = logging.getLogger("uvicorn")
ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()
SENDER_GMAIL = os.environ["SENDER_GMAIL"]
SENDER_GMAIL_PASSWORD = os.environ["SENDER_GMAIL_PASSWORD"]
dirname = os.path.dirname(__file__)
templates_folder = os.path.join(dirname, '../templates')


conf = ConnectionConfig(
    MAIL_USERNAME = SENDER_GMAIL,
    MAIL_PASSWORD = SENDER_GMAIL_PASSWORD,
    MAIL_FROM = SENDER_GMAIL,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="FastAPI forgot password example",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = False,
    TEMPLATE_FOLDER = templates_folder,
)

async def send_registration_notification(password, recipient_email):
    template_body = {
        "email": recipient_email,
        "password": password
    }

    try:
        message = MessageSchema(
            subject="FastAPI forgot password application registration",
            recipients=[recipient_email],
            template_body=template_body,
            subtype=MessageType.html
        )
        fm = FastMail(conf)
        await fm.send_message(message, template_name="registration_notification.html")
    except Exception as e:
        logger.error(f"Something went wrong in registration email notification")
        logger.error(str(e))


async def send_reset_password_mail(recipient_email, user, url, expire_in_minutes):
    template_body = {
        "user": user,
        "url": url,
        "expire_in_minutes": expire_in_minutes
    }
    try:
        message = MessageSchema(
            subject="FastAPI forgot password application reset password",
            recipients=[recipient_email],
            template_body=template_body,
            subtype=MessageType.html
        )
        fm = FastMail(conf)
        await fm.send_message(message, template_name="reset_password_email.html")
    except Exception as e:
        logger.error(f"Something went wrong in reset password email")
        logger.error(str(e))
