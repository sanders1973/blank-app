import streamlit as st

# Initialize session state to keep track of to-do list items
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

st.title('To-Do List App')

# Function to add new item
def add_item():
    item = st.text_input('Enter a new to-do item:', key='new_item')
    if st.button('Add Item'):
        if item:
            st.session_state.todo_list.append(item)
           

# Display existing to-do items with radio buttons
def display_items():
    for index, item in enumerate(st.session_state.todo_list):
        st.radio('', [item], key=f'item_{index}')

add_item()
display_items()

# Function to select an item for modification or deletion
selected_item = st.radio('Select an item to modify or delete:', st.session_state.todo_list, key='modify_delete')
if selected_item:
    if st.button('Modify'):
        new_value = st.text_input('Enter the new value:', value=selected_item)
        if st.button('Update Item'):
            item_index = st.session_state.todo_list.index(selected_item)
            st.session_state.todo_list[item_index] = new_value
           
    if st.button('Delete'):
        st.session_state.todo_list.remove(selected_item)
       
