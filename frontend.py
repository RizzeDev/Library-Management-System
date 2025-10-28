import streamlit as st
import backend as bk 

st.set_page_config(page_title="Library Management System 📚", layout="wide")

st.title("📚 Library Management System")
st.caption("A simple Python + MySQL project to manage books, members, and records.")


if st.sidebar.button("ℹ️ About Project"):
    st.sidebar.info("""
    **Library Management System (CBSE Project 2025–26)**

    **Programming Used**
    - Python (Logic and Backend)
    - MySQL (Database)
    - Streamlit (User Interface)

    **Developed By**
    - Ritesh Pathak (Programmer)
    - Pavitr Pandey (File Management)
    - Viraj Garosa (File Management)

    **Guide:** Ms. Deepshikha
    
    **Class & Subject:**  XII____(Computer Science - 083)

    **School:** Amity International School, Mayur Vihar Phase 1, Delhi-110091
    """)

# Sidebar Navigation
menu = st.sidebar.radio("Menu", [
    "Add Book",
    "Add Member",
    "Issue Book",
    "Return Book",
    "View All Books",
    "View All Members"
])


# Add Book Section
if menu == "Add Book":
    st.subheader("➕ Add New Book")
    name = st.text_input("Enter Book Name")
    genre = st.text_input("Enter Book Genre")
    price = st.number_input("Enter Price (₹)", min_value=0)
    if st.button("Save Book"):
        if name and genre:
            message = bk.add_book(name, genre, price)
            st.success(message)
        else:
            st.warning("Please fill all the details properly!")


# Add Member Section
elif menu == "Add Member":
    st.subheader("👤 Add New Member")
    name = st.text_input("Enter Member Name")
    age = st.number_input("Enter Member Age", min_value=5, max_value=120)
    active = st.selectbox("Membership Active?", ["Y", "N"])
    if st.button("Save Member"):
        if name:
            message = bk.add_member(name, age, active)
            st.success(message)
        else:
            st.warning("Member name cannot be blank!")


# Issue Book Section
elif menu == "Issue Book":
    st.subheader("🔖 Issue a Book")
    member_id = st.text_input("Enter Member ID")
    book_id = st.text_input("Enter Book ID")
    if st.button("Issue Book"):
        if member_id and book_id:
            message = bk.issue_book(member_id, book_id)
            st.info(message)
        else:
            st.warning("Please enter both Member ID and Book ID!")


# Return Book Section
elif menu == "Return Book":
    st.subheader("↩️ Return a Book")
    member_id = st.text_input("Enter Member ID")
    book_id = st.text_input("Enter Book ID")
    if st.button("Return Book"):
        if member_id and book_id:
            message = bk.return_book(member_id, book_id)
            st.success(message)
        else:
            st.warning("Please enter both Member ID and Book ID!")


# View Books Section
elif menu == "View All Books":
    st.subheader("📖 All Books in the Library")
    books = bk.get_all_books()
    if books:
        for book in books:
            st.write(f"ID: {book[0]} | Name: {book[1]} | Genre: {book[2]} | Price: ₹{book[3]}")
    else:
        st.warning("No books found in the database.")


# View Members Section
elif menu == "View All Members":
    st.subheader("👥 All Library Members")
    members = bk.get_all_members()
    if members:
        for i, m in enumerate(members, 1):
            st.write(f"{i}. Name: {m[1]} | ID: {m[0]} | Age: {m[2]} | Active: {m[3]}")
    else:
        st.warning("No members found in the library records.")

