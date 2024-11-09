import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`
        lover = BookLover("Alice", "alice@example.com", "Fantasy")
        lover.add_book("Jane Eyre", 4)
        self.assertIn("Jane Eyre", lover.book_list['book_name'].values)
    
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once
        lover = BookLover("Bob", "bob@example.com", "Sci-Fi")
        lover.add_book("Fight Club", 5)
        lover.add_book("Fight Club", 5)
        self.assertEqual(len(lover.book_list[lover.book_list['book_name'] == "Fight Club"]), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`
        lover = BookLover("Carol", "carol@example.com", "Mystery")
        lover.add_book("The Divine Comedy", 4)
        self.assertTrue(lover.has_read("The Divine Comedy"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        lover = BookLover("Dave", "dave@example.com", "History")
        self.assertFalse(lover.has_read("How to lie with Data"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected
        lover = BookLover("Eve", "eve@example.com", "Romance")
        lover.add_book("How to influence friends", 5)
        lover.add_book("The Popol Vuh", 5)
        lover.add_book("Atomic Habits", 3)
        self.assertEqual(lover.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3
        lover = BookLover("Frank", "frank@example.com", "Adventure")
        lover.add_book("The 5AM Club", 4)
        lover.add_book("Step Up Step Back", 2)
        lover.add_book("Measure What Matters", 5)
        favorite_books = lover.fav_books()
        self.assertTrue(all(favorite_books['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)
