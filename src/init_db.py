from sqlalchemy.orm import sessionmaker

from db import (
    engine,
    metadata,
    polish_text_search_configuration_command,
    toregconfig_function_command,
)
from models import Document

metadata.drop_all()
engine.execute(toregconfig_function_command())
engine.execute(polish_text_search_configuration_command())
metadata.create_all()
print("Database initialized")

Session = sessionmaker(bind=engine)

with Session() as session:
    with open("dataset.txt", mode="rt") as textfile:
        for row in textfile.readlines():
            d = Document(
                text=row.replace('"', "").replace(",", " ").capitalize(),
                language="en",
            )
            session.add(d)
    session.commit()
print("Dataset loaded")
