import streamlit as st
import pandas as pd
from github import Github
from streamlit_local_storage import LocalStorage


localS = LocalStorage()

# Initialize session state
if 'lists' not in st.session_state:
    st.session_state.lists = {f"List {i+1}": [] for i in range(8)}
if 'current_list' not in st.session_state:
    st.session_state.current_list = 'List 1'
if 'item' not in st.session_state:
    st.session_state.item = ''
if 'description' not in st.session_state:
    st.session_state.description = ''
if 'github_info' not in st.session_state:
    st.session_state.github_info = {"token": "", "username": "", "repo": ""}
if 'github_info_loaded' not in st.session_state:
    st.session_state.github_info_loaded = False

def select_list(list_name):
    st.session_state.current_list = list_name

def add_item():
    st.session_state.lists[st.session_state.current_list].append({"Item": st.session_state.item, "Description": st.session_state.description})
    st.session_state.item = ''
    st.session_state.description = ''
    st.rerun()

def modify_item(selected_item):
    if selected_item:
        idx = st.session_state.lists[st.session_state.current_list].index(selected_item)
        item = st.sidebar.text_input("Modify Item", value=selected_item["Item"], key='modify_item')
        description = st.sidebar.text_area("Description", value=selected_item["Description"], key='modify_description')
        if st.sidebar.button("Save"):
            st.session_state.lists[st.session_state.current_list][idx] = {"Item": item, "Description": description}
            st.rerun()

def delete_item(selected_item):
    if selected_item:
        idx = st.session_state.lists[st.session_state.current_list].index(selected_item)
        if st.sidebar.button("Delete"):
            del st.session_state.lists[st.session_state.current_list][idx]
            st.rerun()

def move_item(selected_item, target_list):
    if selected_item:
        idx = st.session_state.lists[st.session_state.current_list].index(selected_item)
        item = st.session_state.lists[st.session_state.current_list].pop(idx)
        st.session_state.lists[target_list].append(item)
        st.rerun()

def get_github_client():
    return Github(st.session_state.github_info["token"])

def read_from_github():
    g = get_github_client()
    repo = g.get_user().get_repo(st.session_state.github_info["repo"])
    for i in range(8):
        file_path = f"list_{i+1}.txt"
        try:
            file_content = repo.get_contents(file_path)
            content = file_content.decoded_content.decode('utf-8')
            st.session_state.lists[f"List {i+1}"] = [eval(line) for line in content.splitlines()]
        except:
            st.session_state.lists[f"List {i+1}"] = []

def write_to_github():
    g = get_github_client()
    repo = g.get_user().get_repo(st.session_state.github_info["repo"])
    for i in range(8):
        file_path = f"list_{i+1}.txt"
        content = "\n".join([str(item) for item in st.session_state.lists[f"List {i+1}"]])
        try:
            file = repo.get_contents(file_path)
            repo.update_file(file_path, "Update list", content, file.sha)
        except:
            repo.create_file(file_path, "Create list", content)

def save_github_info():
    g = get_github_client()
    repo = g.get_user().get_repo(st.session_state.github_info["repo"])
    file_path = "github_info.txt"
    content = str(st.session_state.github_info)
    localS.setItem("github_info", content)
    try:
        file = repo.get_contents(file_path)
        repo.update_file(file_path, "Update GitHub info", content, file.sha)
    except:
        repo.create_file(file_path, "Create GitHub info", content)

def load_github_info():
    github_info = localS.getItem("github_info")
    if github_info:
        st.session_state.github_info = eval(github_info)
        st.session_state.github_info_loaded = True


# Load GitHub info from browser storage on start
if st.session_state.github_info == "":
    load_github_info()
if st.session_state.github_info_loaded:
    read_from_github()

# Sidebar for list selection and item management
st.sidebar.header("GitHub Actions")
if st.sidebar.button("Load Lists"):
    read_from_github()
if st.sidebar.button("Save Lists"):
    write_to_github()

with st.sidebar.expander("Select a List", expanded=True):
    selected_list = st.radio(
        "Choose your list:",
        list(st.session_state.lists.keys())
    )
    select_list(selected_list)

st.sidebar.header(f"To-Do List: {st.session_state.current_list}")
st.session_state.item = st.sidebar.text_input("Add Item", value=st.session_state.item)
st.session_state.description = st.sidebar.text_area("Description", value=st.session_state.description)
if st.sidebar.button("Add"):
    add_item()
current_list_df = pd.DataFrame(st.session_state.lists[st.session_state.current_list])
if not current_list_df.empty:
    selected_item = st.sidebar.radio(
        "Select an item to modify, delete, or move",
        current_list_df.to_dict('records'),
        format_func=lambda x: f"{x['Item']} - {x['Description']}"
    )
    modify_item(selected_item)
    delete_item(selected_item)
    target_list = st.sidebar.selectbox("Move to:", [list_name for list_name in st.session_state.lists.keys() if list_name != st.session_state.current_list])
    if st.sidebar.button("Move"):
        move_item(selected_item, target_list)
    st.sidebar.dataframe(current_list_df)

# Main window for displaying the lists in tabs and GitHub info
st.title("My To-Do Lists")
tabs = st.tabs(["Lists"] + list(st.session_state.lists.keys()))
with tabs[0]:
    st.header("GitHub Information")
    st.session_state.github_info["token"] = st.text_input("GitHub Token", value=st.session_state.github_info["token"], type="password")
    st.session_state.github_info["username"] = st.text_input("GitHub Username", value=st.session_state.github_info["username"])
    st.session_state.github_info["repo"] = st.text_input("Repository Name", value=st.session_state.github_info["repo"])
    if st.button("Save GitHub Info"):
       # set("github_info", str(st.session_state.github_info))
        save_github_info()
        

for tab, list_name in zip(tabs[1:], st.session_state.lists.keys()):
    with tab:
        current_list_df = pd.DataFrame(st.session_state.lists[list_name])
        if not current_list_df.empty:
            st.header(f"{list_name}")
            for i, row in current_list_df.iterrows():
                description_lines = row['Description'].split('\n')
                st.markdown(f"- **{row['Item']}**:")
                for line in description_lines:
                    st.markdown(f"    - {line}")
        else:
            st.write("No items in the list.")
