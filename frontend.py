import streamlit as st
import backend as bk

st.set_page_config(page_title="Library Management System", page_icon="📚", layout="wide")

st.title("📚 Library Management System")
st.caption("Developed by Pratyush Upreti & Dhwani Verma | CBSE Project 2025")

# Sidebar navigation
choice = st.sidebar.radio("Navigate", [
    "Add Book", "Add Member", "Issue Book", "Return Book",
    "Search Book", "Search Member",
    "View All Books", "View All Members", "View Issued Books"
])

# PAGE LOGIC 

if choice == "Add Book":
    st.subheader("➕ Add New Book")
    name = st.text_input("Book Name")
    genre = st.text_input("Genre")
    price = st.number_input("Price (₹)", min_value=0, step=10)
    if st.button("Add Book"):
        if name and genre and price:
            bid = bk.add_book(name, genre, int(price))
            st.success(f"✅ Book '{name}' added successfully! Book ID: {bid}")
        else:
            st.warning("⚠️ Please fill all fields before submitting.")

elif choice == "Add Member":
    st.subheader("🧍 Add New Member")
    name = st.text_input("Member Name")
    age = st.number_input("Age", min_value=5, max_value=100, step=1)
    memstatus = st.selectbox("Membership Active?", ["Y", "N"])
    if st.button("Add Member"):
        if name and age:
            mid = bk.add_member(name, int(age), memstatus)
            st.success(f"✅ Member '{name}' added successfully! Member ID: {mid}")
        else:
            st.warning("⚠️ Please fill all fields.")

elif choice == "Issue Book":
    st.subheader("📖 Issue a Book")
    mid = st.text_input("Member ID")
    bid = st.text_input("Book ID")
    if st.button("Issue Book"):
        if mid and bid:
            bk.issue_book(mid, bid)
            st.success("✅ Book issued successfully!")
        else:
            st.warning("⚠️ Please enter both Member ID and Book ID.")

elif choice == "Return Book":
    st.subheader("🔁 Return a Book")
    mid = st.text_input("Member ID")
    bid = st.text_input("Book ID")
    if st.button("Return Book"):
        if mid and bid:
            bk.return_book(mid, bid)
            st.success("✅ Book returned successfully!")
        else:
            st.warning("⚠️ Please enter both Member ID and Book ID.")

elif choice == "Search Book":
    st.subheader("🔍 Search Book by ID")
    bid = st.text_input("Enter Book ID")
    if st.button("Search"):
        data = bk.search_book(bid)
        if data:
            st.write("### 📘 Book Details:")
            for row in data:
                st.write(f"**Book ID:** {row[0]}")
                st.write(f"**Name:** {row[1]}")
                st.write(f"**Genre:** {row[2]}")
                st.write(f"**Price:** ₹{row[3]}")
        else:
            st.warning("❌ No book found with that ID.")

elif choice == "Search Member":
    st.subheader("🔍 Search Member by ID")
    mid = st.text_input("Enter Member ID")
    if st.button("Search"):
        data = bk.search_member(mid)
        if data:
            st.write("### 👤 Member Details:")
            for row in data:
                st.write(f"**Member ID:** {row[0]}")
                st.write(f"**Name:** {row[1]}")
                st.write(f"**Age:** {row[2]}")
                st.write(f"**Membership Active:** {row[3]}")
        else:
            st.warning("❌ No member found with that ID.")

elif choice == "View All Books":
    st.subheader("📚 All Books in Library")
    data = bk.all_books()
    if data:
        for i, row in enumerate(data, 1):
            st.write(f"**{i}. {row[1]}** | ID: {row[0]} | Genre: {row[2]} | ₹{row[3]}")
    else:
        st.warning("❌ No books found in library.")

elif choice == "View All Members":
    st.subheader("👥 All Members in Library")
    data = bk.all_members()
    if data:
        for i, row in enumerate(data, 1):
            st.write(f"**{i}. {row[1]}** | ID: {row[0]} | Age: {row[2]} | Active: {row[3]}")
    else:
        st.warning("❌ No members found in library.")

elif choice == "View Issued Books":
    st.subheader("📦 Issued Books")
    data = bk.all_issued()
    if data:
        for i, row in enumerate(data, 1):
            st.write(f"**{i}. Member ID:** {row[0]} | **Book ID:** {row[1]}")
    else:
        st.warning("❌ No books currently issued.")
