# Import necessary libraries
import pandas as pd
import streamlit as st
import pickle
import requests

# Function to fetch movie poster from an API
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function to recommend similar movies
def recommend(movie):
    # Find the index of the selected movie in the DataFrame
    movie_index = movies[movies['title'] == movie].index[0]
    
    # Get similarity scores between the selected movie and all other movies
    distances = similarity[movie_index]
    
    # Sort movies by similarity in descending order and select the top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc(i[0]).title)
        # Fetch movie poster from the API
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies

# Load movie data and similarity scores from pickled files
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set up the Streamlit app
st.title('Movie Recommender System')

# Create a dropdown select box to choose a movie
selected_movie_name = st.selectbox("Select a movie:", movies['title'].values)

# Create a button for recommendations
if st.button('Recommend'):
    # Get recommended movies and their posters
    names, posters = recommend(selected_movie_name)

    # Display recommended movies and their posters in a grid layout
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
# Import necessary libraries
import pandas as pd
import streamlit as st
import pickle
import requests

# Function to fetch movie poster from an API
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function to recommend similar movies
def recommend(movie):
    # Find the index of the selected movie in the DataFrame
    movie_index = movies[movies['title'] == movie].index[0]
    
    # Get similarity scores between the selected movie and all other movies
    distances = similarity[movie_index]
    
    # Sort movies by similarity in descending order and select the top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc(i[0]).title)
        # Fetch movie poster from the API
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies

# Load movie data and similarity scores from pickled files
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set up the Streamlit app
st.title('Movie Recommender System')

# Create a dropdown select box to choose a movie
selected_movie_name = st.selectbox("Select a movie:", movies['title'].values)

# Create a button for recommendations
if st.button('Recommend'):
    # Get recommended movies and their posters
    names, posters = recommend(selected_movie_name)

    # Display recommended movies and their posters in a grid layout
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
