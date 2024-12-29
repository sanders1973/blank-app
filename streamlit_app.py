import streamlit as st

# Initialize session state if not already done
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

def add_todo_item():
    new_item = st.session_state['new_item']
    if new_item:
        st.session_state.todo_list.append(new_item)
        st.session_state['new_item'] = '' # Clear input box after adding

def delete_item(index):
    del st.session_state.todo_list[index]

def modify_item(index, new_text):
    st.session_state.todo_list[index] = new_text

# Sidebar for entering new items
st.sidebar.header("Add New Item")
st.sidebar.text_input("New to-do item", key='new_item')
st.sidebar.button("Add", on_click=add_todo_item)

# Main page
st.title("To-Do List")

for i, item in enumerate(st.session_state.todo_list):
    col1, col2, col3 = st.columns([6, 1, 1])
    col1.write(item)
    if col2.button("Modify", key=f'modify_{i}'):
        new_text = st.text_input("Modify item", value=item, key=f'input_{i}')
        if st.button("Save", key=f'save_{i}'):
            modify_item(i, new_text)
    if col3.button("Delete", key=f'delete_{i}'):
        delete_item(i)

# Display updated to-do list
st.write(st.session_state.todo_list)
