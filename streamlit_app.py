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

    
    # Delete main item and its sub-items
    if st.button('Delete Main Item'):
        del st.session_state.to_do_list[selected_main_item]

    
    # Input text box to add new sub-items
    new_sub_item = st.text_input('Add a new sub-item for {}'.format(selected_main_item))

    # Add button for sub-items
    if st.button('Add Sub Item'):
        if new_sub_item:
            st.session_state.to_do_list[selected_main_item].append(new_sub_item)
    

    # Display the sub-items for the selected main item
    selected_sub_item = st.radio('Select a sub-item to modify or delete:', st.session_state.to_do_list[selected_main_item])

    if selected_sub_item:
        # Modify sub-item
        modified_sub_item = st.text_input('Modify selected sub-item', selected_sub_item)
        if st.button('Update Sub Item'):
            index = st.session_state.to_do_list[selected_main_item].index(selected_sub_item)
            st.session_state.to_do_list[selected_main_item][index] = modified_sub_item
    
        
        # Delete sub-item
        if st.button('Delete Sub Item'):
            st.session_state.to_do_list[selected_main_item].remove(selected_sub_item)
    
