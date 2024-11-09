import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, rating):
        # Check if book is already in the book_list
        if book_name in self.book_list['book_name'].values:
            print(f"{book_name} is already in the book list.")
        else:
            # Add the new book to the list
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1  # Update the number of books read
    
    def has_read(self, book_name):
        # Check if the book_name is in the book_list
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        # Return the number of books read
        return self.num_books
    
    def fav_books(self):
        # Return books with rating > 3
        return self.book_list[self.book_list['book_rating'] > 3]
