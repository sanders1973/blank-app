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

# Sidebar for adding items and displaying DataFrame
st.sidebar.header("To-Do List")
add_item()
to_do_df = pd.DataFrame(st.session_state.to_do_list)
if not to_do_df.empty:
    selected_item = st.sidebar.radio(
        "Select an item to modify or delete",
        to_do_df.to_dict('records'),
        format_func=lambda x: f"{x['Item']} - {x['Description']}"
    )
    modify_item(selected_item)
    delete_item(selected_item)
    st.sidebar.dataframe(to_do_df)

# Main window for displaying the list in markdown
st.title("My To-Do List")
if not to_do_df.empty:
    for i, row in to_do_df.iterrows():
        st.markdown(f"- **{row['Item']}**: {row['Description']}")
else:
    st.write("No items in the list.")
