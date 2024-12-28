import streamlit as st

# Initialize session state
if 'to_do_list' not in st.session_state:
    st.session_state.to_do_list = {}

# Title of the app
st.title('To-Do List with Sub-Items')

# Input text box to add new items
new_item = st.text_input('Add a new to-do item')

# Add button for main items
if st.button('Add Main Item'):
    if new_item:
        st.session_state.to_do_list[new_item] = []
        

# Display the to-do list with radio buttons to select an item
selected_main_item = st.radio('Select a main item to modify or delete:', list(st.session_state.to_do_list.keys()))

if selected_main_item:
    # Modify main item
    modified_main_item = st.text_input('Modify selected main item', selected_main_item)
    if st.button('Update Main Item'):
        st.session_state.to_do_list[modified_main_item] = st.session_state.to_do_list.pop(selected_main_item)
       
    
