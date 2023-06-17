import streamlit as st
import function
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    print(todo)
    function.write_todos(todos)

todos = function.get_todos()

st.title("My To-do App")
st.subheader('This is my to-do app.')
st.write('Please write down what you plan to do today.')
for index, choice in enumerate(todos):
    checkbox = st.checkbox(choice,key= choice)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[choice]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

