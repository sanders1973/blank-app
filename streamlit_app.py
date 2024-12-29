import streamlit as st

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Function to add a new task
def add_task():
    if st.session_state['new_task'] and st.session_state['new_description']:
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
def update_task(index, updated_task, updated_description):
    st.session_state['tasks'][index]['task'] = updated_task
    st.session_state['tasks'][index]['description'] = updated_description

st.sidebar.title("Add New Task")
st.sidebar.text_input("Task", key='new_task')
st.sidebar.text_area("Description", key='new_description')
st.sidebar.button("Add Task", on_click=add_task)

st.title("To-Do List")

for i, task in enumerate(st.session_state['tasks']):
    with st.expander(task['task']):
        st.text_area("Edit Task", value=task['task'], key=f'task_{i}')
        st.text_area("Edit Description", value=task['description'], key=f'description_{i}')
        if st.button("Update Task", key=f'update_{i}'):
            update_task(i, st.session_state[f'task_{i}'], st.session_state[f'description_{i}'])
        if st.button("Delete Task", key=f'delete_{i}'):
            delete_task(i)

if st.session_state['tasks']:
    st.success("Tasks updated successfully!")

st.caption("© Your To-Do List App")
