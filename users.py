import streamlit as st
import pandas as pd

def add_data(userid, fname, lname, email, c, conn):
     c.execute('INSERT INTO users VALUES ' + '(' + userid + ", '" + fname + "', '" + lname + "', '" + email + "')")
     print('INSERT INTO users VALUES ' + '(' + userid + ", '" + fname + "', '" + lname + "', '" + email + "')")
    #  conn.commit()

def view_all_data(c):
     c.execute('SELECT * FROM users')
     data = c.fetchall()
     return data

def update_data(task2, task1, c, conn):
     stri = 'UPDATE users SET ' + task1  + ' WHERE ' + task2
     print(stri)
     c.execute(stri)
    #  conn.commit()

def delete_data(task1, c, conn):
     c.execute('DELETE FROM users WHERE ' + task1)
     print('DELETE FROM users WHERE ' + task1)
    #  conn.commit()

def read_data(c, conn):
     with st.expander("View Users"):
          result = view_all_data(c)
          clean_df = pd.DataFrame(result, columns=['userid', 'fname', 'lname', 'email'])
          st.dataframe(clean_df)
     
     tab1, tab2, tab3 = st.tabs(['Insert', 'Update', 'Delete'])

     with tab1:
        st.subheader('Insert Data')
        userid = st.text_input('userid')
        fname = st.text_input('fname')
        lname = st.text_input('lname')
        email = st.text_input('email')
        if st.button('Insert'):
            add_data(userid, fname, lname, email, c, conn)
            st.success('Inserted')

     with tab2: 
        st.subheader('Update Data')
        list_of_tasks = set({'userid', 'fname', 'lname', 'email'})
        selected_task = st.selectbox("Column Name", list_of_tasks)
        if selected_task=='userid':
            task1 = selected_task + " = " + st.text_input(selected_task, key='task1')
        else:
            task1 = selected_task + " = " + "'" + st.text_input(selected_task, key='task1') + "'"
        update_task = st.selectbox("Column to update", list_of_tasks-{selected_task})
        if update_task=='userid':
            task2 = update_task + " = " + st.text_input(update_task, key='task2')
        else:
            task2 = update_task + " = " + "'" + st.text_input(update_task, key='task2') + "'"
        if st.button("Update"):
            update_data(task2,task1, c, conn)
            st.success("Updated")
    
     with tab3:
        st.subheader('Delete Data')
        list_of_tasks = set({'userid', 'fname', 'lname', 'email'})
        selected_task = st.selectbox("Column name",list_of_tasks)
        if selected_task == 'userid':
            task1 = selected_task + " = " + st.text_input(selected_task, key='task')
        else:
            task1 = selected_task + " = " + "'" + st.text_input(selected_task, key='task') + "'"
        if st.button("Delete"):
            delete_data(task1, c, conn)
            st.success("Deleted")