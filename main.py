class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]

# Приклад використання
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Кількість книг у бібліотеці:", len(library))

print("Перша книга у бібліотеці:", library[0])
print("Друга книга у бібліотеці:", library[1])
print("Третя книга у бібліотеці:", library[2])

