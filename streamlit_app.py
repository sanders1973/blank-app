import streamlit as st

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Function to add a new task
def add_task():
    if st.session_state['new_task']:
        st.session_state['tasks'].append({
            'task': st.session_state['new_task'],
            'description': st.session_state['new_description']
        })
        st.session_state['new_task'] = ""
        st.session_state['new_description'] = ""

# Function to delete a task
def delete_task(index):
    st.session_state['tasks'].pop(index)

# Function to update a task
def update_task(index):
    st.session_state['tasks'][index]['task'] = st.session_state[f'task_{index}']
    st.session_state['tasks'][index]['description'] = st.session_state[f'description_{index}']

st.title("To-Do List Application")

st.text_input("New Task", key='new_task')
st.text_area("Description", key='new_description')
st.button("Add Task", on_click=add_task)

for i, task in enumerate(st.session_state['tasks']):
    with st.expander(task['task'], expanded=True):
        st.text_input("Edit Task", value=task['task'], key=f'task_{i}', on_change=update_task, args=(i,))
        st.text_area("Edit Description", value=task['description'], key=f'description_{i}', on_change=update_task, args=(i,))
        st.button("Delete Task", key=f'delete_{i}', on_click=delete_task, args=(i,))

if st.session_state['tasks']:
    st.success("Tasks updated successfully!")

st.caption("© Your To-Do List App")

