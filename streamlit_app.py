import streamlit as st
import pandas as pd

# Initialize session state
if 'lists' not in st.session_state:
    st.session_state.lists = {f"List {i+1}": [] for i in range(8)}
if 'current_list' not in st.session_state:
    st.session_state.current_list = 'List 1'
if 'item' not in st.session_state:
    st.session_state.item = ''
if 'description' not in st.session_state:
    st.session_state.description = ''

def select_list(list_name):
    st.session_state.current_list = list_name


def add_item():
    if st.sidebar.button("Add"):
        st.session_state.lists[st.session_state.current_list].append({"Item": st.session_state.item, "Description": st.session_state.description})
        
        st.session_state.description = ''
        st.session_state.item = ''
        st.rerun()

def modify_item(selected_item):
    if selected_item:
        idx = st.session_state.lists[st.session_state.current_list].index(selected_item)
        item = st.sidebar.text_input("Modify Item", value=selected_item["Item"], key='modify_item')
        description = st.sidebar.text_area("Description", value=selected_item["Description"], key='modify_description')
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
with st.sidebar.expander("Select a List", expanded=True):
    selected_list = st.radio(
        "Choose your list:",
        list(st.session_state.lists.keys())
    )
    select_list(selected_list)

st.sidebar.header(f"To-Do List: {st.session_state.current_list}")
st.session_state.item = st.sidebar.text_input("Add Item", value=st.session_state.item)
#st.session_state.description = st.sidebar.text_area("Description", value=st.session_state.description)
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
  

# Main window for displaying the selected list in markdown
st.title(f"My To-Do List: {st.session_state.current_list}")
if not current_list_df.empty:
    for i, row in current_list_df.iterrows():
        st.markdown(f"- **{row['Item']}**: {row['Description']}")
else:
    st.write("No items in the list.")
