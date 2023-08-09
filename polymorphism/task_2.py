class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: 'Author') -> 'Book':
        book = Book(name, year, author)
        self.books.append(book)
        return book
    
    def group_by_author(self,author:'Author') :
        return [book for book in self.books if book.author_instance == author]
    
    def __repr__(self):
        return f"Library(name= '{self.name}', books= '{self.books}',authors= '{self.authors}')"
    
    def __str__(self):
        return f"Library {self.name}"



class Book:

    total_number_of_books=0

    def __init__(self,name: str, year: int, author: 'Author'):
        self.name=name
        self.year=year
        self.author_instance=author
        Book.total_number_of_books+=1

    def __repr__(self):
        return f"Book(name= '{self.name}, year= '{self.year}', author= '{self.author_instance}')"
    
    def __str__(self):
        return f"{self.name} is written by {self.author_instance.author_name}"
    
class Author:
    def __init__(self,author_name: str, country: str, birthday: str):
        self.author_name=author_name
        self.country=country
        self.birthday=birthday
        self.author_books=[]

    def __repr__(self):
        return f"Author(name= '{self.author_name}', country= '{self.country}', birthday= '{self.birthday}')"
    
    def __str__(self):
        return f"Hey,my name is {self.author_name} and I am from {self.country}.My birthday is {self.birthday}"
    


author_1=Author("Van Gog","Netherlands","17 april")
author_2=Author("Vans Gorg","Australia","14 may")

library_1=Library("Strange books")

library_1.new_book("Native speaker",1345,repr(author_1))
library_1.new_book("Harry Potter",1991,repr(author_1))
library_1.new_book("Tom and Jerry ",1991,repr(author_2))

print(library_1)