import random
import pymysql

# --- DATABASE CONNECTION ---
def connect_to_db():
    try:
        db = pymysql.connect(
            host="mysql-1234.railway.app",  # change to real host
            user="myuser",
            password="mypassword",
            database="library"
        )
        print("✅ Database connection successful!")
        return db
    except pymysql.err.OperationalError as e:
        print(f"❌ Database connection failed: {e}")
        return None

db = connect_to_db()
MyCur = db.cursor() if db else None


# --- DATABASE SETUP ---
def create():
    if not db:
        print("⚠️ Skipping database setup — connection not available.")
        return

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
        print("📚 Tables ready to use!")
    except Exception as e:
        print("❌ Database setup error:", e)


# --- ID GENERATORS ---
def midgenerate():
    return chr(random.randint(65, 90)) + str(random.randint(100, 999))

def bidgenerate():
    return ''.join([chr(random.randint(65, 90)) for _ in range(random.randint(3, 5))])


# --- CORE FUNCTIONS ---
def add_book(name, genre, price):
    if not db:
        return "⚠️ Cannot add book — database not connected."
    try:
        bid = bidgenerate()
        MyCur.execute("INSERT INTO books VALUES(%s, %s, %s, %s)", (bid, name, genre, price))
        db.commit()
        return f"✅ Book added successfully! ID: {bid}"
    except Exception as e:
        return f"❌ Error adding book: {e}"

def add_member(name, age, memstatus):
    if not db:
        return "⚠️ Cannot add member — database not connected."
    try:
        mid = midgenerate()
        MyCur.execute("INSERT INTO members VALUES(%s, %s, %s, %s)", (mid, name, age, memstatus))
        db.commit()
        return f"✅ Member added successfully! ID: {mid}"
    except Exception as e:
        return f"❌ Error adding member: {e}"

def issue_book(mid, bid):
    if not db:
        return "⚠️ Cannot issue book — database not connected."
    try:
        MyCur.execute("INSERT INTO issuedbooks VALUES(%s, %s)", (mid, bid))
        db.commit()
        return "✅ Book issued successfully!"
    except Exception as e:
        return f"❌ Error issuing book: {e}"

def return_book(mid, bid):
    if not db:
        return "⚠️ Cannot return book — database not connected."
    try:
        MyCur.execute("DELETE FROM issuedbooks WHERE mid=%s AND bid=%s", (mid, bid))
        db.commit()
        return "✅ Book returned successfully!"
    except Exception as e:
        return f"❌ Error returning book: {e}"

def get_all_books():
    if not db:
        return []
    try:
        MyCur.execute("SELECT * FROM books")
        return MyCur.fetchall()
    except Exception as e:
        print("Error fetching books:", e)
        return []

def get_all_members():
    if not db:
        return []
    try:
        MyCur.execute("SELECT * FROM members")
        return MyCur.fetchall()
    except Exception as e:
        print("Error fetching members:", e)
        return []


create()




