import pytest

from filtering import filter_documents


@pytest.mark.parametrize(
    "text, search_pattern",
    [
        ("benefit", "benefits"),
        ("benefits", "benefit"),
        ("work", "working"),
        ("working hours", "work hour"),
        ("checking type", "check types"),
        ("Best person at the world", "best world"),
        ("I like swimming and fishing. I have finished a book about it", "swim finish"),
    ],
)
def test_filter_full_text_search_en(text, search_pattern, db_session, document_factory):
    language = "en"
    document = document_factory(text=text, language="en")
    _ = document_factory(text="", language=language)

    results = filter_documents(db_session, language, search=search_pattern)

    assert results.count() == 1
    assert results.first() == document
