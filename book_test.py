import unittest
from book import Book

class BookTest(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedzim", "Sapkowski", 1997)
    def test_get_info(self):
        text_correct = 'Tytuł: Wiedzim Author: Sapkowski Rok: 1997'
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)

    def test_change_title(self):
        self.book.change_title("Miecz przeznaczenia")
        #text_correct = 'Tytuł: Wiedzim Author: Sapkowski Rok: 1997'
        #text_result = self.book.change_title()
        #self.assertEqual(text_correct, text_result)
        text_correct = "Miecz przeznaczenia"
        text_result = self.book.title
        self.assertEqual(text_correct, text_result)

    def test_change_author(self):
        self.book.change_author("Tolkien")
        self.assertEqual("Tolkien", self.book.author)

    def test_change_year(self):
        self.book.change_year(2024)
        self.assertEqual(2024, self.book.year)


    if __name__ == '__main__':
        unittest.main()