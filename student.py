from book import *

class Student:
    def __init__(self, name):
        self.__name = name
        self.__books = []
    
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def getBook(self, book):
        self.__books.append(book)
    
    def handBook(self, book):
        index = self.__books.index(book)
        self.__books.pop(index)
    
    def viewBooks(self):
        bookList = []
        for book in self.__books:
            bookList.append(book.getTitle())
        return bookList
