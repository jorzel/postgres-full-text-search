from models import Document


def filter_documents(session, language, search):
    return session.query(Document)
