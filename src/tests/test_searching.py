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
    document = document_factory(text=text, language=language)
    _ = document_factory(text="", language=language)

    results = filter_documents(db_session, language, search=search_pattern)

    assert results.count() == 1
    assert results.first() == document


@pytest.mark.parametrize(
    "text, search_pattern",
    [
        ("test", "test"),
        ("Benefity w firmie", "benefit"),
        ("Benefity w firmie", "firma benefity"),
        ("Praca zdalna w firmie", "praca firma"),
        ("Benefity", "benefit"),
        ("Delegacje", "delegacja"),
        ("Praca zdalna", "zdalnie"),
        ("Czytanie jest bardzo ważne. Zgadzasz się?", "czytać zgadzać"),
    ],
)
def test_filter_full_text_search_pl(text, search_pattern, db_session, document_factory):
    language = "pl"
    document = document_factory(text=text, language=language)
    _ = document_factory(text="", language=language)

    results = filter_documents(db_session, language, search=search_pattern)

    assert results.count() == 1
    assert results.first() == document
