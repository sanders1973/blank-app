import streamlit as st
import pandas as pd

# Initialize session state
if 'lists' not in st.session_state:
    st.session_state.lists = {f"List {i+1}": [] for i in range(8)}
if 'current_list' not in st.session_state:
    st.session_state.current_list = 'List 1'

def select_list(list_name):
    st.session_state.current_list = list_name

def add_item():
    item = st.sidebar.text_input("Add Item")
    description = st.sidebar.text_area("Description")
    if st.sidebar.button("Add"):
        st.session_state.lists[st.session_state.current_list].append({"Item": item, "Description": description})
        st.rerun()

def modify_item(selected_item):
    if selected_item:
        idx = st.session_state.lists[st.session_state.current_list].index(selected_item)
        item = st.sidebar.text_input("Modify Item", value=selected_item["Item"])
        description = st.sidebar.text_area("Description", value=selected_item["Description"])
        if st.sidebar.button("Save"):
            st.session_state.lists[st.session_state.current_list][idx] = {"Item": item, "Description": description}
            st.rerun()

def delete_item(selected_item):
    if selected_item:
        idx = st.session_state.lists[st.session_state.current_list].index(selected_item)
        if st.sidebar.button("Delete"):
            del st.session_state.lists[st.session_state.current_list][idx]
            st.rerun()

# Sidebar for list selection and item management
st.sidebar.header("Select a List")
for list_name in st.session_state.lists.keys():
    if st.sidebar.button(list_name):
        select_list(list_name)

st.sidebar.header(f"To-Do List: {st.session_state.current_list}")
add_item()
current_list_df = pd.DataFrame(st.session_state.lists[st.session_state.current_list])
if not current_list_df.empty:
    selected_item = st.sidebar.radio(
        "Select an item to modify or delete",
        current_list_df.to_dict('records'),
        format_func=lambda x: f"{x['Item']} - {x['Description']}"
    )
    modify_item(selected_item)
    delete_item(selected_item)
    st.sidebar.dataframe(current_list_df)

# Main window for displaying the selected list in markdown
st.title(f"My To-Do List: {st.session_state.current_list}")
if not current_list_df.empty:
    for i, row in current_list_df.iterrows():
        st.markdown(f"- **{row['Item']}**: {row['Description']}")
else:
    st.write("No items in the list.")
