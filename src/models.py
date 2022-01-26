from sqlalchemy import Column, Index, String, Text, func

from db import BaseModel


class Document(BaseModel):
    text = Column(Text, nullable=False, default="", server_default="")
    language = Column(String, nullable=False, default="en", server_default="en")

    tsvector_text = func.to_tsvector(func.toregconfig(language), text)

    __table_args__ = (
        Index(
            "ix_pl_document_tsvector_text",
            func.to_tsvector("polish", text),
            postgresql_using="gin",
            postgresql_where=(language == "pl"),
        ),
        Index(
            "ix_en_document_tsvector_text",
            func.to_tsvector("english", text),
            postgresql_using="gin",
            postgresql_where=(language == "en"),
        ),
    )

    def __str__(self):
        return f"Document(text={self.text}, language={self.language}"

    __repr__ = __str__
