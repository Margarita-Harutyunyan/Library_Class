from student import *

class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = {}
        self.__cards = []

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def addBook(self, book, count = 1):
        if book in self.__books.keys():
            self.__books[book] += count
        else:
            self.__books.update({book : count})
    
    def viewLibrary(self):
        for book in self.__books:
            print('{} : {}'.format(book.getTitle(), self.__books[book]))
        print()

    def createCard(self, studentName, cardLifetime):
        id = hash(studentName)
        self.__cards.append(id)
        print('{}, Your card is valid for {} years'.format(studentName, cardLifetime))

    def takeBook(self, student, bookTitle):
        studentBooks = student.viewBooks()
        if bookTitle in studentBooks:
            print('You cannot take more than one copy of a book!')
            return
        id = hash(student.getName())
        if id not in self.__cards:
            print('Not registered')
            return
        for book in self.__books:
            if bookTitle == book.getTitle():
                if self.__books[book] > 0:
                    student.getBook(book)
                    self.__books[book] -= 1
                    return
                print('Currently unavailable')
                return
        

    def returnBook(self, student, bookTitle):
        id = hash(student.getName())
        if id not in self.__cards:
            print('Not registered')
            return
        for book in self.__books:
            if bookTitle == book.getTitle():  
                self.__books[book] += 1
                student.handBook(book)
