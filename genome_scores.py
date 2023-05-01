import streamlit as st
import pandas as pd

def add_data(movieid, tagid, relevance, c, conn):
     c.execute('INSERT INTO genome_scores VALUES ' + '(' + movieid + ", " + tagid + ", " + relevance + ")")
     print('INSERT INTO genome_scores VALUES ' + '(' + movieid + ", " + tagid + ", " + relevance + ")")
    #  conn.commit()

def view_all_data(c):
     c.execute('SELECT * FROM genome_scores WHERE movieid<10')
     data = c.fetchall()
     return data

def update_data(task2, task1, c, conn):
     stri = 'UPDATE genome_scores SET ' + task1  + ' WHERE ' + task2
     print(stri)
     c.execute(stri)
    #  conn.commit()

def delete_data(task1, c, conn):
     c.execute('DELETE FROM genome_scores WHERE ' + task1)
     print('DELETE FROM genome_scores WHERE ' + task1)
    #  conn.commit()

def read_data(c, conn):
     with st.expander("View Genome Scores"):
          result = view_all_data(c)
          clean_df = pd.DataFrame(result, columns=['movieid', 'tagid', 'relevance'])
          st.dataframe(clean_df)
     
     tab1, tab2, tab3, tab4 = st.tabs(['Insert', 'Update', 'Delete', 'Query'])

     with tab1:
        st.subheader('Insert Data')
        movieid = st.text_input('movieid')
        tagid = st.text_input('tagid')
        relevance = st.text_input('relevance')
        if st.button('Insert'):
            add_data(movieid, tagid, relevance, c, conn)
            st.success('Inserted')

     with tab2: 
        st.subheader('Update Data')
        list_of_tasks = set({'movieid', 'tagid', 'relevance'})
        selected_task = st.selectbox("Column Name", list_of_tasks)
        if selected_task=='movieid' or selected_task=='tagid' or selected_task=='relevance':
            task1 = selected_task + " = " + st.text_input(selected_task, key='task1')
        else:
            task1 = selected_task + " = " + "'" + st.text_input(selected_task, key='task1') + "'"
        update_task = st.selectbox("Column to update", list_of_tasks-{selected_task})
        if update_task=='movieid' or update_task=='tagid' or update_task=='relevance':
            task2 = update_task + " = " + st.text_input(update_task, key='task2')
        else:
            task2 = update_task + " = " + "'" + st.text_input(update_task, key='task2') + "'"
        if st.button("Update"):
            update_data(task2,task1, c, conn)
            st.success("Updated")
    
     with tab3:
        st.subheader('Delete Data')
        list_of_tasks = set({'movieid', 'tagid', 'relevance'})
        selected_task = st.selectbox("Column name",list_of_tasks)
        if selected_task == 'movieid' or selected_task=='tagid' or selected_task=='relevance':
            task1 = selected_task + " = " + st.text_input(selected_task, key='task')
        else:
            task1 = selected_task + " = " + "'" + st.text_input(selected_task, key='task') + "'"
        if st.button("Delete"):
            delete_data(task1, c, conn)
            st.success("Deleted")
     
     with tab4:
         st.subheader('Query')
         query = st.text_area('Query')
         if st.button("Execute"):
             with st.expander('View Table'):
                c.execute(query)
                if query.startswith('select'):
                    data = c.fetchall()
                else:
                    data = view_all_data(c)
                clean_df = pd.DataFrame(data, columns=['movieid', 'tagid', 'relevance'])
                st.dataframe(clean_df)