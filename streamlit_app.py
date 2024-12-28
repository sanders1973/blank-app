import streamlit as st

# Function to display and handle to-do lists
def display_todo_list(title, items, other_lists):
    st.subheader(title)
    new_item = st.text_input(f"Add item to {title}")
    if new_item:
        items.append({"task": new_item, "subtasks": []})

    for index, item in enumerate(items):
        if st.button(f"Remove {item['task']}", key=f"{title}_remove_{index}"):
            del items[index]
        for other_list in other_lists:
            if st.button(f"Move to {other_list['title']}", key=f"{title}_move_{index}_to_{other_list['title']}"):
                other_list['items'].append(item)
                del items[index]
                break

        subtask_input = st.text_input(f"Add sub-item to {item['task']}", key=f"{title}_subtask_{index}")
        if subtask_input:
            item["subtasks"].append(subtask_input)
        st.write(f"- {item['task']}")
        for subtask in item["subtasks"]:
            st.write(f"  - {subtask}")

# Initialize the lists
todo_lists = [
    {"title": "To Do 1", "items": []},
    {"title": "To Do 2", "items": []},
    {"title": "To Do 3", "items": []},
    {"title": "To Do 4", "items": []},
]

# Layout setup in 2x2 grid
col1, col2 = st.columns(2)
with col1:
    display_todo_list(todo_lists[0]["title"], todo_lists[0]["items"], todo_lists[1:])
    display_todo_list(todo_lists[2]["title"], todo_lists[2]["items"], todo_lists[3:])

with col2:
    display_todo_list(todo_lists[1]["title"], todo_lists[1]["items"], todo_lists[0:1] + todo_lists[2:])
    display_todo_list(todo_lists[3]["title"], todo_lists[3]["items"], todo_lists[0:3])
