import streamlit as st

# Function to initialize session state for to-do lists
def init_state():
    if 'todo1' not in st.session_state:
        st.session_state.todo1 = []
    if 'todo2' not in st.session_state:
        st.session_state.todo2 = []
    if 'todo3' not in st.session_state:
        st.session_state.todo3 = []
    if 'todo4' not in st.session_state:
        st.session_state.todo4 = []

# Function to add a new item
def add_item(list_name, item, sub_items):
    st.session_state[list_name].append({'item': item, 'sub_items': sub_items})

# Function to delete an item
def delete_item(list_name, index):
    st.session_state[list_name].pop(index)

# Function to move an item between lists
def move_item(from_list, to_list, index):
    item = st.session_state[from_list].pop(index)
    st.session_state[to_list].append(item)

# Initialize state
init_state()

st.title('To-Do List Application')

# Layout of to-do lists
col1, col2 = st.columns(2)

with col1:
    st.header('To-Do List 1')
    for idx, todo in enumerate(st.session_state.todo1):
        st.write(f"{todo['item']} - Sub-items: {', '.join(todo['sub_items'])}")
        if st.button(f'Delete 1-{idx}', key=f'delete1-{idx}'):
            delete_item('todo1', idx)
        for jdx, list_name in enumerate(['todo2', 'todo3', 'todo4']):
            if st.button(f'Move to {list_name[-1]}', key=f'move1-{idx}-{jdx}'):
                move_item('todo1', list_name, idx)
    new_item = st.text_input('New item for List 1', key='new_item1')
    new_sub_items = st.text_input('Sub-items for List 1 (comma separated)', key='new_sub_items1').split(',')
    if st.button('Add to List 1'):
        add_item('todo1', new_item, new_sub_items)

    st.header('To-Do List 3')
    for idx, todo in enumerate(st.session_state.todo3):
        st.write(f"{todo['item']} - Sub-items: {', '.join(todo['sub_items'])}")
        if st.button(f'Delete 3-{idx}', key=f'delete3-{idx}'):
            delete_item('todo3', idx)
        for jdx, list_name in enumerate(['todo1', 'todo2', 'todo4']):
            if st.button(f'Move to {list_name[-1]}', key=f'move3-{idx}-{jdx}'):
                move_item('todo3', list_name, idx)
    new_item = st.text_input('New item for List 3', key='new_item3')
    new_sub_items = st.text_input('Sub-items for List 3 (comma separated)', key='new_sub_items3').split(',')
    if st.button('Add to List 3'):
        add_item('todo3', new_item, new_sub_items)

with col2:
    st.header('To-Do List 2')
    for idx, todo in enumerate(st.session_state.todo2):
        st.write(f"{todo['item']} - Sub-items: {', '.join(todo['sub_items'])}")
        if st.button(f'Delete 2-{idx}', key=f'delete2-{idx}'):
            delete_item('todo2', idx)
        for jdx, list_name in enumerate(['todo1', 'todo3', 'todo4']):
            if st.button(f'Move to {list_name[-1]}', key=f'move2-{idx}-{jdx}'):
                move_item('todo2', list_name, idx)
    new_item = st.text_input('New item for List 2', key='new_item2')
    new_sub_items = st.text_input('Sub-items for List 2 (comma separated)', key='new_sub_items2').split(',')
    if st.button('Add to List 2'):
        add_item('todo2', new_item, new_sub_items)

    st.header('To-Do List 4')
    for idx, todo in enumerate(st.session_state.todo4):
        st.write(f"{todo['item']} - Sub-items: {', '.join(todo['sub_items'])}")
        if st.button(f'Delete 4-{idx}', key=f'delete4-{idx}'):
            delete_item('todo4', idx)
        for jdx, list_name in enumerate(['todo1', 'todo2', 'todo3']):
            if st.button(f'Move to {list_name[-1]}', key=f'move4-{idx}-{jdx}'):
                move_item('todo4', list_name, idx)
    new_item = st.text_input('New item for List 4', key='new_item4')
    new_sub_items = st.text_input('Sub-items for List 4 (comma separated)', key='new_sub_items4').split(',')
    if st.button('Add to List 4'):
        add_item('todo4', new_item, new_sub_items)

st.sidebar.title('Instructions')
st.sidebar.write('''
- Add new items by typing in the text boxes and clicking the "Add" button for each list.
- Delete items by clicking the "Delete" button next to each item.
- Move items between lists using the "Move" buttons.
- Sub-items will be moved or deleted along with their parent item.
''')

if __name__ == "__main__":
    main()
