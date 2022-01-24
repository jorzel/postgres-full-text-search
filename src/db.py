import logging
import re

from sqlalchemy import Column, Integer, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import configure_mappers

logger = logging.getLogger(__name__)

pattern = re.compile(r"(?<!^)(?=[A-Z])")


def toregconfig_function_command():
    return """
         CREATE OR REPLACE FUNCTION toregconfig(text)
         RETURNS regconfig AS 'select (
            case
            when $1=''fr'' then ''french''
            when $1=''es'' then ''spanish''
            when $1=''pl'' then ''polish''
            when $1=''ru'' then ''russian''
            else ''simple''
            end
        )::regconfig;' LANGUAGE SQL IMMUTABLE
        RETURNS NULL ON NULL INPUT;
    """


def camel_case_to_underscore(name: str) -> str:
    return pattern.sub("_", name).lower()


class Base:
    """
    Abstract model providing basic fields and tablename
    """

    @declared_attr
    def __tablename__(cls):
        return camel_case_to_underscore(cls.__name__).lower()

    id = Column(Integer, primary_key=True, autoincrement=True)


SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/testdb"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)
BaseModel = declarative_base(cls=Base, metadata=metadata)


from models import Document  # noqa

configure_mappers()