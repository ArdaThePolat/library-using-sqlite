from library import *

print("""
Welcome to the library application

Operations;
1. Show books
2. Query book
3. Add book
4. Delete book
5. Exit
""")

library=Library()

while True:
    myinput = input("Please select an operation : ")
    if(myinput == "5"):
        print("Exiting from the system...")
        break
    elif(myinput == "1"):
        library.showBooks()
    elif(myinput == "2"):
        library.queryBook(input("Please enter the name of the book : "))
    elif(myinput == "3"):
        library.addBook(Book(input("Name : "),input("Writer : "),input("Publisher : ")))
        print("Book added successfully.")
    elif(myinput == "4"):
        library.deleteBook(input("Please enter the name of the book : "))
        print("Book deleted successfully.")
    else:
        print("Invalid operation")
