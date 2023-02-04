#An example of using the library 
from library import *

lib = Library('PicsArtLib')

b1 = Book('Dive Into Systems', 814)
b2 = Book('Practical Binary Analysis', 460)
b3 = Book('OOAD with Applications', 717)
b4 = Book('Learning Python', 1213)
b5 = Book('Effective Python', 469)
b6 = Book('Compilers: Principles, Techniques, and Tools', 1040)

lib.addBook(b1, 1)
lib.addBook(b2, 2)
lib.addBook(b3, 5)
lib.addBook(b4, 3)
lib.addBook(b5, 10)
lib.addBook(b6, 2)

lib.viewLibrary()

student1 = Student('Molly')
student2 = Student('Melanie')

lib.createCard('Molly', 2)
lib.createCard('Melanie', 3)

lib.takeBook(student1, 'Dive Into Systems')
lib.takeBook(student1, 'Practical Binary Analysis')
print('{} currently owns the following books:'.format(student1.getName()))
print(student1.viewBooks())

lib.takeBook(student2, 'Dive Into Systems')
lib.takeBook(student2, 'OOAD with Applications')
print('{} currently owns the following books:'.format(student2.getName()))
print(student2.viewBooks())

lib.returnBook(student1, 'Dive Into Systems')
print("{}'s currently available books: ".format(lib.getName()))
lib.viewLibrary()
