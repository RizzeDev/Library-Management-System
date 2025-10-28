import random
import pymysql

db = pymysql.connect(host="localhost", user="root", password="root17")  
MyCur = db.cursor()

def create():
    try:
        MyCur.execute("CREATE DATABASE IF NOT EXISTS Library")
        MyCur.execute("USE Library")
        MyCur.execute("""
            CREATE TABLE IF NOT EXISTS books(
                bid VARCHAR(6) PRIMARY KEY,
                Name VARCHAR(255) NOT NULL,
                Genre VARCHAR(255),
                Price INT(10) NOT NULL
            )
        """)
        MyCur.execute("""
            CREATE TABLE IF NOT EXISTS members(
                mid VARCHAR(6) PRIMARY KEY,
                Name VARCHAR(255) NOT NULL,
                Age INT(3) NOT NULL,
                Membership_Active VARCHAR(1) NOT NULL
            )
        """)
        MyCur.execute("""
            CREATE TABLE IF NOT EXISTS issuedbooks(
                mid VARCHAR(6),
                bid VARCHAR(6)
            )
        """)
        db.commit()
    except Exception as e:
        print("Database setup error:", e)



def midgenerate():
    return chr(random.randint(65, 90)) + str(random.randint(100, 999))

def bidgenerate():
    return ''.join([chr(random.randint(65, 90)) for _ in range(random.randint(3, 5))])



#CORE FUNCTIONS:

def add_book(name, genre, price):
    try:
        bid = bidgenerate()
        MyCur.execute("INSERT INTO books VALUES(%s, %s, %s, %s)", (bid, name, genre, price))
        db.commit()
        return f"✅ Book added successfully! Book ID: {bid}"
    except Exception as e:
        return f"❌ Error adding book: {e}"

def add_member(name, age, memstatus):
    try:
        mid = midgenerate()
        MyCur.execute("INSERT INTO members VALUES(%s, %s, %s, %s)", (mid, name, age, memstatus))
        db.commit()
        return f"✅ Member added successfully! Member ID: {mid}"
    except Exception as e:
        return f"❌ Error adding member: {e}"

def issue_book(mid, bid):
    try:
        MyCur.execute("INSERT INTO issuedbooks VALUES(%s, %s)", (mid, bid))
        db.commit()
        return "✅ Book issued successfully!"
    except Exception as e:
        return f"❌ Error issuing book: {e}"

def return_book(mid, bid):
    try:
        MyCur.execute("DELETE FROM issuedbooks WHERE mid=%s AND bid=%s", (mid, bid))
        db.commit()
        return "✅ Book returned successfully!"
    except Exception as e:
        return f"❌ Error returning book: {e}"

def get_all_books():
    MyCur.execute("SELECT * FROM books")
    return MyCur.fetchall()

def get_all_members():
    MyCur.execute("SELECT * FROM members")
    return MyCur.fetchall()


create()

