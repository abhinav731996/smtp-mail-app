from pydantic import BaseModel
from pydantic import EmailStr


class EmailRequest(BaseModel):

    email: EmailStr

    subject: str

    message: str