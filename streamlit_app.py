import streamlit as st

# Title of the app
st.title("Select an Item from the List")

# List of text items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Dropdown menu for selecting an item
selected_item = st.selectbox("Choose an item:", items)

# Display the selected item
st.write(f"You selected: {selected_item}")
