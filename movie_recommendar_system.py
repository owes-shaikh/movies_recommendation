#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')


# In[3]:


movies.head()


# In[4]:


credits.head()


# In[5]:


credits.head(1)['cast'].values


# In[6]:


movies.merge(credits,on='title')


# In[7]:


movies = movies.merge(credits,on='title')


# In[8]:


movies


# In[9]:


movies.head()


# In[10]:


movies.info()


# In[11]:


# genres, id, keywords, title, overview, popularity, cast, crew

movies[['id','title','overview','genres','keywords','cast','crew']].head()


# In[12]:


movies = movies[['id','title','overview','genres','keywords','cast','crew']]


# In[13]:


movies.head()


# In[14]:


movies.isnull().sum()


# In[15]:


movies.duplicated().sum()


# In[16]:


movies.iloc[0].genres


# In[17]:


def convert(obj):
    L = []
    for i in obj:
        L.append(i['name'])
    return L

        


# In[ ]:





# In[18]:


convert('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


# In[19]:


import ast
ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


# In[20]:


def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

        


# In[21]:


convert('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


# In[22]:


movies['genres'].apply(convert)


# In[23]:


movies['genres'] = movies['genres'].apply(convert)


# In[24]:


movies.head()


# In[25]:


movies['keywords'].apply(convert)


# In[26]:


movies['keywords'] = movies['keywords'].apply(convert)


# In[27]:


movies.head()


# In[28]:


movies.iloc[0].cast


# In[29]:


def cast(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L


# In[30]:


movies['cast'].apply(cast)


# In[31]:


movies['cast'] = movies['cast'].apply(cast)


# In[32]:


movies.head()


# In[33]:


def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L
        


# In[ ]:





# In[34]:


movies['crew'].apply(fetch_director)


# In[35]:


movies['crew'] = movies['crew'].apply(fetch_director)


# In[36]:


movies.head()


# In[37]:


movies['overview'][0]


# In[38]:


movies.apply(pd.to_numeric, errors="ignore").applymap(lambda x: isinstance(x, float), na_action='ignore').any()


# In[39]:


movies['overview'].apply(lambda x:x.split())


# In[40]:


movies['overview'] = movies['overview'].fillna('')
movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[41]:


movies['overview']


# In[42]:


movies.head()


# In[43]:


movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ","") for i in x]) 
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ","") for i in x])


# In[44]:


movies.head()


# In[45]:


movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'] 


# In[46]:


movies.head()


# In[47]:


new_df = movies[['id','title','tags']]


# In[48]:


new_df.head()


# In[49]:


new_df['tags'] = new_df['tags'].apply(lambda x :" ".join(x))


# In[50]:


new_df.head()


# In[51]:


new_df['tags'][0]


# In[52]:


new_df['tags'] = new_df['tags'].apply(lambda x :x.lower())


# In[53]:


new_df['tags'][0]


# In[54]:


pip install -U scikit-learn


# In[55]:


pip install --upgrade scikit-learn


# In[56]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[57]:


vectors = cv.fit_transform(new_df['tags']).toarray()

vectors


# In[58]:


cv.get_feature_names_out()


# In[59]:


a = cv.get_feature_names_out()

vertical_list = [[x] for x in a]

vertical_list


# we will use steming to reduce similar words and assign a single root word

# In[60]:


import nltk


# In[61]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


# In[65]:


def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))
        
    return " ".join(y)


# In[66]:


new_df['tags'].apply(stem)


# In[67]:


new_df['tags'] = new_df['tags'].apply(stem)


# In[68]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[69]:


vectors = cv.fit_transform(new_df['tags']).toarray()

vectors


# In[70]:


cv.get_feature_names_out()


# In[71]:


a = cv.get_feature_names_out()

vertical_list = [[x] for x in a]

vertical_list


# In[73]:


from sklearn.metrics.pairwise import cosine_similarity


# In[76]:


similarity = cosine_similarity(vectors)


# In[80]:


similarity[0]


# In[82]:


similarity[1]


# In[84]:


new_df


# In[86]:


new_df['title'] == 'Avatar'


# In[87]:


new_df[new_df['title'] == 'Avatar']


# In[90]:


new_df[new_df['title'] == 'Avatar'].index[0]


# In[ ]:





# In[93]:


sorted(similarity[0],reverse = True)


# In[95]:


sorted(list(enumerate(similarity[0])))


# In[96]:


sorted(list(enumerate(similarity[0])),reverse = True)


# In[98]:


sorted(list(enumerate(similarity[0])),reverse = True,key = lambda x: x[1])[1:6]


# In[102]:


def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x: x[1])[1:6]
    
    for i in movies_list:
        print(new_df.iloc[i[0]].title)
    return


# In[103]:


recommend('Avatar')


# In[104]:


import pickle 


# In[105]:


pickle.dump(new_df,open('movies.pkl','wb'))


# In[106]:


new_df


# In[107]:


new_df.to_dict()


# In[108]:


pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))


# In[109]:


pickle.dump(similarity,open('similarity.pkl','wb'))


# In[ ]:




