import psycopg2
import streamlit as st
import pandas as pd 
import streamlit.components.v1 as stc
import movies_genres
import movies
import genres
import tags
import users
import ratings
import genome_scores
import genome_tags

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;"> Movie Lens Database Management </h1>
    </div>
    """ 
def connect():
    try:
        conn = psycopg2.connect("dbname = IMDB user=postgres password=vajja")
        cur = conn.cursor()
        return cur, conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
c, conn = connect()

stc.html(HTML_BANNER)
menu = ['Genres', 'Movies', 'Movie'+"'"+'s Genres', 'Tags', 'Ratings', 'Users', 'Genome Scores', 'Genome Tags']
choice = st.sidebar.selectbox("Menu",menu)

if choice == 'Genres':
     genres.read_data(c, conn)

elif choice == 'Movies':
     movies.read_data(c, conn)

elif choice == 'Movie'+"'"+'s Genres':
     movies_genres.read_data(c, conn)

elif choice == 'Tags':
     tags.read_data(c, conn)

elif choice == 'Ratings':
     ratings.read_data(c, conn)

elif choice == 'Users':
     users.read_data(c, conn)

elif choice == 'Genome Scores':
     genome_scores.read_data(c, conn)

elif choice == 'Genome Tags':
     genome_tags.read_data(c, conn)