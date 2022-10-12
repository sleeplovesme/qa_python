class TestBooksCollector:
    def test_init_empty_dict(self, collector):
        # Проверка books_rating в конструкторе.
        assert collector.books_rating == {}

    def test_init_empty_list(self, collector):
        # Проверка favorites в конструкторе.
        assert collector.favorites == []

    def test_add_new_book_add_two_books_true(self, collector, add_default_book):
        # Проверка добавления книг.
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_exist_book_false(self, collector, add_default_book):
        # Нельзя добавить одну и ту же книгу дважды.
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_book_is_not_in_list_false(self, collector):
        # Нельзя выставить рейтинг книге, которой нет в списке.
        collector.set_book_rating('Гордость и предубеждение и зомби', 8)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') is None

    def test_set_book_rating_rate_less_1_false(self, collector, add_default_book):
        # Нельзя выставить рейтинг меньше 1.
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_set_book_rating_rate_more_10_false(self, collector, add_default_book):
        # Нельзя выставить рейтинг больше 10.
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_set_book_rating_book_not_in_list_false(self, collector):
        # У не добавленной книги нет рейтинга.
        assert collector.get_book_rating('Гордость и предубеждение и зомби') is None

    def test_add_book_in_favorites_add_one_book_true(self, collector, add_default_book):
        # Добавление книги в избранное.
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_not_in_books_rating_false(self, collector):
        # Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_delete_book_true(self, collector, add_default_book):
        # Проверка удаления книги из избранного.
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_with_specific_rating_get_books_with_rating_equals_5_true(self, collector, add_default_book):
        # Проверка вывода списка книг с определенным рейтингом.
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Питон для чайников')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 6)
        collector.set_book_rating('Питон для чайников', 5)
        assert len(collector.get_books_with_specific_rating(5)) == 2
