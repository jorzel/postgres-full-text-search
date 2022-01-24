from sqlalchemy import Column, Index, String, Text, func

from db import BaseModel


class Document(BaseModel):
    text = Column(Text, nullable=False, default="", server_default="")
    language = Column(String, nullable=False, default="en", server_default="en")

    tsvector_text = func.to_tsvector(func.toregconfig(language), text)

    __table_args__ = (
        Index("ix_document_tsvector_text", tsvector_text, postgresql_using="gin"),
    )
