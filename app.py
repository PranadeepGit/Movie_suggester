from datetime import time

import streamlit as st
import pickle
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Movie Suggester", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#-------Load assests------

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_CTaizi.json")



with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('Movie Suggester ')
        st.subheader('We always pass on good advice :smile: ')
        st.write('A content-based suggester system using Vector space method and Classification method.')
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
with st.container():
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
            movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path


    def suggest(movie):
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        suggested_movie_names = []
        suggested_movie_posters = []
        for i in distances[1:8]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            suggested_movie_posters.append(fetch_poster(movie_id))
            suggested_movie_names.append(movies.iloc[i[0]].title)

        return suggested_movie_names, suggested_movie_posters


    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Select a movie from the dropdown",
        movie_list
    )
    if st.button('Suggest for me'):
        suggested_movie_names, suggested_movie_posters = suggest(selected_movie)
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.text(suggested_movie_names[0])
            st.image(suggested_movie_posters[0])
        with col2:
            st.text(suggested_movie_names[1])
            st.image(suggested_movie_posters[1])
        with col3:
            st.text(suggested_movie_names[2])
            st.image(suggested_movie_posters[2])
        with col4:
            st.text(suggested_movie_names[3])
            st.image(suggested_movie_posters[3])
        with col5:
            st.text(suggested_movie_names[4])
            st.image(suggested_movie_posters[4])
        with col6:
            st.text(suggested_movie_names[5])
            st.image(suggested_movie_posters[5])
        with col7:
            st.text(suggested_movie_names[6])
            st.image(suggested_movie_posters[6])

st.text("-----------------------------------------------------------------------------------------------")
st.caption('by')
st.write("Pranadeep, Nithish and Tharun.")
st.subheader('IIITV-ICD')
# with st.sidebar:
#     # with st.echo():
#     st.text("APP DESCRIPTION")
#     st.text("It will suggest 5 MOVIES...")

