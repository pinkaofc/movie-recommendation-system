import pickle
import streamlit as st
import pandas as pd
import requests
import json


def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c1d7f6f22794bf149d28dd3821b96293&language=en-US'
    response = requests.get(url)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


# --- Recommendation function ---
def recommend(movie, n=5):
    idx = movies.index[movies['title'].str.casefold() == movie.casefold()]
    if len(idx) == 0:
        return [], []

    movie_index = int(idx[0])
    distances = similarity[movie_index]
    movie_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)

    # Skip the same movie and take top n
    top = [(i, s) for i, s in movie_list if i != movie_index][:n]

    recommended_movies = []
    recommended_movies_posters = []
    for i, score in top:
        movie_id = movies.iloc[i].movie_id   # ensure your movie.pkl has a "movie_id" column
        recommended_movies.append(movies.iloc[i].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# --- Load data ---
movie_dict = pickle.load(open('movie.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Streamlit UI ---
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    'Choose a movie you like:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)  # 5 recommended movies
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
