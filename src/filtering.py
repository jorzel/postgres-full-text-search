from sqlalchemy import func
from sqlalchemy.orm import Query, Session

from models import Document


def filter_documents(session: Session, language: str, search: str) -> Query:
    filter_args = []
    filter_args.append(Document.language == language)
    if search:
        words = search.split()
        if search[-1] != " ":
            # no whitespace at the end means that word is still typed and not completed
            words[-1] = f"{words[-1]}:*"
        ts_pattern = "&".join(words)
        tsquery = func.to_tsquery(func.toregconfig(language), ts_pattern)
        filter_args.append(Document.tsvector_text.op("@@")(tsquery))
    return session.query(Document).filter(*filter_args)
