class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

        def borrow(self):
            if self.available:
                self.available = False
                print(f"el libro {self.title} ha sido prestado")
            else:
                print(f"el libro {self.title} no está disponible")

                def return_book(self):
                    self.available = True
                    print(f"el libro {self.title} ha sido devuelto")

class user:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)            
        else:
            print(f"el libro {book.title} no está disponible")
            
    def return_book(self, title):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"el libro {book.title} no está en la lista de prestado")
class Library:
    def __init__(self):
        self.books = []
        self.user = []
    def add_book(self, book):
        self.books.append(book)
        print(f"el libro {book.title} ha sido agregado")

    def register_user(self, user):
        self.user.append(user)
        print(f"el usuario {user.name} ha sido registrado")
    
    def show_available_books(self):
        print("libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author} ")

book1 = book("el principito", "Antoine de saint exupery")
book2 = book("1984", "George orwell")

user1 = user("Bianca", "001")
user2 = user("Marc", "002")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)
library.register_user(user2)

library.show_available_books()
user1.borrow_book(book1)

library.show_available_books()

user1.return_book(book1)

library.show_available_books()
