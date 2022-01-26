import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from db import (
    BaseModel,
    polish_text_search_configuration_command,
    toregconfig_function_command,
)
from models import Document


@pytest.fixture(scope="session")
def model_base():
    return BaseModel


@pytest.yield_fixture(scope="session")
def db_connection(model_base):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/testdb"
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    model_base.metadata.bind = engine
    model_base.metadata.drop_all()
    engine.execute(toregconfig_function_command())
    engine.execute(polish_text_search_configuration_command())
    model_base.metadata.create_all()
    connection = engine.connect()

    yield connection

    model_base.metadata.drop_all()
    engine.dispose()


@pytest.yield_fixture
def db_session(db_connection):
    transaction = db_connection.begin()
    session = sessionmaker(bind=db_connection, class_=Session)
    db_session = session()

    yield db_session

    transaction.rollback()
    db_session.close()


@pytest.fixture
def document_factory(db_session: Session):
    def _document_factory(text: str, language: str):
        document = Document(text=text, language=language)
        db_session.add(document)
        db_session.flush()
        return document

    yield _document_factory
