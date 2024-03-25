import sqlite3

con = sqlite3.connect('kütüpDeneme.db')
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()

def addData():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası', 'Arda', 'Everest', 561)")
    con.commit()

def getData():
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri.....")
    for i in liste:
        print(i)

def updateData():
    cursor.execute("UPDATE kitaplık set Yayınevi = 'Arda Polat' where Yayınevi = 'Everest'")
    con.commit()

def deleteData():
    cursor.execute("DELETE FROM kitaplık where Yazar = 'Arda'")
    con.commit()

createTable()

con.close()