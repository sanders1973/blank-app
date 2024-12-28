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
    

def display_items():
    for main_item, sub_items in st.session_state.to_do_list.items():
        st.markdown(f"- {main_item}")
        
        if st.button(f'Modify Main Item', key=f'modify_{main_item}'):
            modified_main_item = st.text_input('Modify main item', main_item, key=f'modify_input_{main_item}')
            if st.button('Update Main Item', key=f'update_{main_item}'):
                st.session_state.to_do_list[modified_main_item] = st.session_state.to_do_list.pop(main_item)
            

        if st.button(f'Delete Main Item', key=f'delete_{main_item}'):
            del st.session_state.to_do_list[main_item]
        

        for sub_item in sub_items:
            st.markdown(f"\t- {sub_item}")
            
            if st.button(f'Modify Sub Item', key=f'modify_sub_{sub_item}'):
                modified_sub_item = st.text_input('Modify sub item', sub_item, key=f'modify_input_sub_{sub_item}')
                if st.button('Update Sub Item', key=f'update_sub_{sub_item}'):
                    index = st.session_state.to_do_list[main_item].index(sub_item)
                    st.session_state.to_do_list[main_item][index] = modified_sub_item
                

            if st.button(f'Delete Sub Item', key=f'delete_sub_{sub_item}'):
                st.session_state.to_do_list[main_item].remove(sub_item)
            

        new_sub_item = st.text_input('Add a new sub-item for {}'.format(main_item), key=f'new_sub_{main_item}')
        if st.button('Add Sub Item', key=f'add_sub_{main_item}'):
            if new_sub_item:
                st.session_state.to_do_list[main_item].append(new_sub_item)
            

# Display the to-do list with sub-items
display_items()
