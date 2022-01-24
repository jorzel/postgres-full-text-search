from sqlalchemy import func
from sqlalchemy.orm import Query, Session

from models import Document


def filter_documents(session: Session, language: str, search: str) -> Query:
    filter_args = []
    filter_args.append(Document.language == language)
    ts_pattern = "&".join(search.split())
    tsquery = func.to_tsquery(func.toregconfig(language), ts_pattern)
    filter_args.append(Document.tsvector_text.op("@@")(tsquery))
    return session.query(Document).filter(*filter_args)
