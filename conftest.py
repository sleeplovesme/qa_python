import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def add_default_book(collector):
    add_default_book = collector.add_new_book('Гордость и предубеждение и зомби')
    return add_default_book
