from sqlalchemy import Column, String, Text

from db import BaseModel


class Document(BaseModel):
    text = Column(Text, nullable=False, default="", server_default="")
    language = Column(String, nullable=False, default="en", server_default="en")
