import sqlite3

class Book():
    def __init__(self,name,writer,publisher):
        self.name=name
        self.writer=writer
        self.publisher=publisher
    
    def __str__(self):
        return "Name : {}\nWriter : {}\nPublisher : {}\n".format(self.name,self.writer,self.publisher)

class Library():
    def __init__(self):
        self.connectDatabase()
    
    def connectDatabase(self):
        self.con=sqlite3.connect("library.db")
        self.cursor=self.con.cursor()
        query="Create Table If not exists books (name TEXT,writer TEXT,publisher TEXT)"
        self.cursor.execute(query)
        self.con.commit()
    
    def disconnectDatabase(self):
        self.con.close()
    
    def showBooks(self):
        query="Select * From books"
        self.cursor.execute(query)
        books=self.cursor.fetchall()
        if(len(books)==0):
            print("No book found")
        else:
            for i in books:
                book=Book(i[0],i[1],i[2])
                print(book)
    
    def queryBook(self,name):
        query="Select * From books where name = ?"
        self.cursor.execute(query,(name,))
        books=self.cursor.fetchall()
        if(len(books)==0):
            print("No book found")
        else:
            book=Book(books[0][0],books[0][1],books[0][2])
            print(book)
    
    def addBook(self,book):
        query="Insert into books Values(?,?,?)"
        self.cursor.execute(query,(book.name,book.writer,book.publisher))
        self.con.commit()
    
    def deleteBook(self,name):
        query="Delete From books where name = ?"
        self.cursor.execute(query,(name,))
        self.con.commit()