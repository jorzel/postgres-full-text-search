import pytest


@pytest.fixture
def db_session():
    return None


@pytest.fixture
def document_factory(db_session):
    def _document_factory(text, language):
        return None

    yield _document_factory


def filter_documents(session, language, search):
    return []


@pytest.mark.parametrize(
    "text, search_pattern",
    [
        ("benefit", "benefits"),
        ("benefits", "benefit"),
        ("work", "working"),
        ("working hours", "work hour"),
        ("checking type", "check types"),
    ],
)
def test_filter_full_text_search_en(text, search_pattern, db_session, document_factory):
    language = "en"
    document = document_factory(text=text, language="en")

    results = filter_documents(db_session, language, search=search_pattern)

    assert results.count() == 1
    assert results.first() == document
