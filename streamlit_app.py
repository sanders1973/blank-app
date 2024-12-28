import streamlit as st

# Initialize session state
if 'to_do_list' not in st.session_state:
    st.session_state.to_do_list = []

# Title of the app
st.title('To-Do List')

# Input text box to add new items
new_item = st.text_input('Add a new to-do item')

# Add button
if st.button('Add'):
    if new_item:
        st.session_state.to_do_list.append(new_item)
       

# Display the to-do list with radio buttons to select an item
selected_item = st.radio('Select an item to modify or delete:', st.session_state.to_do_list)

if selected_item:
    # Modify item
    modified_item = st.text_input('Modify selected item', selected_item)
    if st.button('Update'):
        index = st.session_state.to_do_list.index(selected_item)
        st.session_state.to_do_list[index] = modified_item
        
    
    # Delete item
    if st.button('Delete'):
        st.session_state.to_do_list.remove(selected_item)
       

