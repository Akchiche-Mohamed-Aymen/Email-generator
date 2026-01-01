from pydantic import BaseModel, Field
class Email(BaseModel):
    subject: str = Field(..., description="Subject line of the email")
    body: str = Field(..., description="Body content of the email")
    