class BooksCollector:

    def __init__(self):
        self.books_rating = {}
        self.favorites = []

    def add_new_book(self, name):
        if not self.books_rating.get(name):
            self.books_rating[name] = 1

    def set_book_rating(self, name, rating):
        if self.books_rating.get(name) and rating in range(1, 11):
            self.books_rating[name] = rating

    def get_book_rating(self, name):
        return self.books_rating.get(name)

    def get_books_with_specific_rating(self, rating):
        books_with_specific_rating = []
        if self.books_rating and rating in range(1, 11):
            for name, book_rating in self.books_rating.items():
                if book_rating == rating:
                    books_with_specific_rating.append(name)

        return books_with_specific_rating

    def get_books_rating(self):
        return self.books_rating

    def add_book_in_favorites(self, name):
        if self.books_rating.get(name):
            if name not in self.favorites:
                self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        return self.favorites
