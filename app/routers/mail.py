from fastapi import APIRouter

from fastapi.responses import JSONResponse

from app.models.email_model import EmailRequest

from app.services.smtp_service import send_email

from app.utils.exceptions import (
    SMTPConfigurationError,
    EmailSendingError
)

router = APIRouter()


@router.post("/send-email")
def send_mail(
    request: EmailRequest
):

    try:

        send_email(
            request.email,
            request.subject,
            request.message
        )

        return JSONResponse(

            status_code=200,

            content={

                "success": True,

                "message": "Email sent successfully."
            }
        )

    except SMTPConfigurationError as e:

        return JSONResponse(

            status_code=400,

            content={

                "success": False,

                "message": str(e)
            }
        )

    except EmailSendingError as e:

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "message": str(e)
            }
        )

    except Exception as e:

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "message": f"Unexpected error: {str(e)}"
            }
        )