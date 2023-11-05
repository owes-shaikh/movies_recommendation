# Movies Recommendation Sytem

The provided Python code uses the Streamlit framework to create a movie recommender system. Here's an explanation of how the code works:

1. Import Libraries:
   - `pandas` is imported for data manipulation.
   - `streamlit` is imported for creating a web-based user interface.
   - `pickle` is used for reading pickled data.
   - `requests` is used for making HTTP requests.

2. `fetch_poster(movie_id)` Function:
   - This function takes a movie ID as input and uses it to make an API request to retrieve the poster image of the movie from 'themoviedb.org.'
   - The movie poster URL is constructed and returned.

3. `recommend(movie)` Function:
   - This function recommends similar movies based on the selected movie's title.
   - It finds the index of the selected movie in the DataFrame, calculates the cosine similarity between the selected movie and all other movies, and returns the top 5 recommended movies.
   - It also fetches poster images for the recommended movies using the `fetch_poster` function.

4. Load Data:
   - Movie data and similarity scores are loaded from pickled files using the `pickle.load` method.

5. Streamlit User Interface:
   - The Streamlit app's title is set to "Movie Recommender System."
   - A dropdown select box allows the user to choose a movie from the list of available movies.

6. Recommendations:
   - When the "Recommend" button is clicked, the selected movie is used as input for the `recommend` function to retrieve recommended movies and their poster images.
   - The recommended movies and their posters are displayed in a grid layout using `st.beta_columns`.

This code creates a simple movie recommender system using Streamlit, allowing users to select a movie and receive recommendations for similar movies along with their poster images. The movie data and similarity scores are precomputed and loaded from pickled files for efficiency.
