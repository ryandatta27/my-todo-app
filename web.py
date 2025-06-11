import streamlit as st
import functions

# # Load existing todos
todos = functions.get_todos()

# Debugging: Print the contents of todos to verify
# st.write("Debugging: Contents of todos.txt")
# st.write(todos)

# Function to add a new todo
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    # st.session_state["new_todo"] = ""  # ✅ Safe to reset here

# App UI
st.title("Bonus Web App")
st.subheader("Welcome to the Bonus Web App")
st.write("This is a simple web app to demonstrate the bonus functionality.")

# Display todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()

# Input for new todo
st.text_input("Add a new todo", placeholder="Enter a new todo", key="new_todo")

# Add and Delete buttons
st.button("Add", on_click=add_todo, key="add_button")

# Debugging: Print the session state to verify
# st.write("Debugging: st.session_state")
# st.write(st.session_state)
