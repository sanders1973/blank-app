import streamlit as st
import pandas as pd

# Initialize session state
if 'to_do_list' not in st.session_state:
    st.session_state.to_do_list = []

def add_item():
    item = st.sidebar.text_input("Add Item")
    description = st.sidebar.text_area("Description")
    if st.sidebar.button("Add"):
        st.session_state.to_do_list.append({"Item": item, "Description": description})
        st.rerun()

def modify_item(idx):
    item = st.sidebar.text_input("Modify Item", value=st.session_state.to_do_list[idx]["Item"])
    description = st.sidebar.text_area("Description", value=st.session_state.to_do_list[idx]["Description"])
    if st.sidebar.button("Save"):
        st.session_state.to_do_list[idx] = {"Item": item, "Description": description}
        st.rerun()

def delete_item(idx):
    if st.sidebar.button("Delete"):
        del st.session_state.to_do_list[idx]
        st.rerun()

# Sidebar for adding items and displaying DataFrame
st.sidebar.header("To-Do List")
add_item()
to_do_df = pd.DataFrame(st.session_state.to_do_list)
if not to_do_df.empty:
    st.sidebar.dataframe(to_do_df)
    selected_idx = st.sidebar.selectbox("Select an item to modify or delete", to_do_df.index)
    modify_item(selected_idx)
    delete_item(selected_idx)
    
    
# Main window for displaying the list in markdown
st.title("My To-Do List")
if not to_do_df.empty:
    for i, row in to_do_df.iterrows():
        st.markdown(f"- **{row['Item']}**: {row['Description']}")
else:
    st.write("No items in the list.")
