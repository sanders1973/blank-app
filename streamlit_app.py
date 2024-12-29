import streamlit as st
import pandas as pd

# Initialize session state
if 'to_do_list' not in st.session_state:
    st.session_state.to_do_list = []

def add_item():
    item = st.sidebar.text_input("Add Item")
    description = st.sidebar.text_area("Description")
    if st.sidebar.button("Add"):
        st.session_state.to_do_list.append({"Item": item, "Description": description})
        st.rerun()

def modify_item(selected_item):
    if selected_item:
        idx = st.session_state.to_do_list.index(selected_item)
        item = st.sidebar.text_input("Modify Item", value=selected_item["Item"])
        description = st.sidebar.text_area("Description", value=selected_item["Description"])
        if st.sidebar.button("Save"):
            st.session_state.to_do_list[idx] = {"Item": item, "Description": description}
            st.rerun()

def delete_item(selected_item):
    if selected_item:
        idx = st.session_state.to_do_list.index(selected_item)
        if st.sidebar.button("Delete"):
            del st.session_state.to_do_list[idx]
            st.rerun()

# Sidebar for adding items and selecting items to modify or delete
st.sidebar.header("To-Do List")
add_item()
if st.session_state.to_do_list:
    selected_item = st.sidebar.radio(
        "Select an item to modify or delete",
        st.session_state.to_do_list,
        format_func=lambda x: f"{x['Item']} - {x['Description']}"
    )
    modify_item(selected_item)
    delete_item(selected_item)

# Main window for displaying the list in markdown
st.title("My To-Do List")
if st.session_state.to_do_list:
    for item in st.session_state.to_do_list:
        st.markdown(f"- **{item['Item']}**: {item['Description']}")
else:
    st.write("No items in the list.")
