#create a class representing a book
#add attributes and methods

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False

    def display_info(self):
        print(f"'{self.title}' by {self.author} ({self.year})")

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"You checked out '{self.title}'.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' wasn't checked out.")

#add an inheritance layer to explore polymorphism
class PrintedBook(Book):
    def __init__(self, title, author, year, weight_grams):
        super().__init__(title, author, year)
        self.weight_grams = weight_grams

    def display_info(self):
        super().display_info()
        print(f"Format: Printed | Weight: {self.weight_grams}g")

class EBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def display_info(self):
        super().display_info()
        print(f"Format: EBook | File size: {self.file_size_mb}MB")

#create instances
ebook = EBook("Digital Fortress", "Dan Brown", 1998, 2.5)
printed = PrintedBook("The Hobbit", "J.R.R. Tolkien", 1937, 300)

#polymorphism in action
books = [ebook, printed]

for book in books:
    book.display_info()
    book.check_out()
    book.return_book()
    print()
