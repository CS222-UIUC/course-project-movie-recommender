import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import sklearn as sk
import numpy as np
import pandas as pd
import tensorflow as ts
import matplotlib.pyplot as plt
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")
df.head()

print(df.shape)

df.info()
df.isnull().sum()  # check null values

df.duplicated().sum()
vcounts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
vaverages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
avg = vaverages.mean()
avg
df = df.drop(["production_companies", "popularity", "budget", "revenue", "status", "recommendations",
             "runtime", "vote_average", "backdrop_path", 'tagline'], axis=1)  # 'poster_path'], axis=1)
df.drop_duplicates(inplace=True)
df.title.duplicated().sum()
# checking for release data with same movie title
df[["title", "release_date"]].duplicated().sum()
df.drop_duplicates(subset=["title", "release_date"], inplace=True)
df = df[df.vote_count >= 350].reset_index()
df.isnull().sum()
df.fillna("", inplace=True)  # replace the null values with ''
# We do have an option filling all the nulls with 0, but since they will have string values, I thought that na -> "" will be necessary
df
index = df[(df.genres == "") & (df.overview == "")].index
df.drop(index, inplace=True)
df.shape
df.head()
df.info()
df.genres = df.genres.apply(lambda x: " ".join(x.split("-")))
df.keywords = df.keywords.apply(lambda x: " ".join(x.split("-")))
df.credits = df.credits.apply(
    lambda x: " ".join(x.replace(" ", "").split("-")[:5]))
df["tags"] = df.overview + " " + df.genres + " " + \
    df.credits + " " + df.keywords + " " + df.original_language
df['tags']
df_new = df[["id", "title", "tags", 'poster_path']]
df_new
df_new.tags = df_new.tags.apply(lambda x: x.lower())
df_new
df_new.tags
df_new.tags[0]
df_new.head()
prts = PorterStemmer()


def stem(text):
    y = []
    for i in text.split():
        y.append(prts.stem(i))

    return " ".join(y)


df_new["tags"] = df_new["tags"].apply(stem)
countvec = CountVectorizer(stop_words="english", max_features=5000)
countvec
vect = countvec.fit_transform(df_new["tags"]).toarray()
vect
countvec.get_feature_names_out()
sim = cosine_similarity(vect)
sim
sim.shape

# function to give recommenddation based on similar movie


def recommend(movies):
    movie_index = df_new[df_new.title == movies].index[0]
    distances = sim[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]

    arr = []
    for i in movies_list:
        print(df_new.iloc[i[0]].title)
        arr.append(df_new.iloc[i[0]].title)
    return arr


# recommend("Batman") testing function

# start of UI


root = tk.Tk()
root.title("Movie Recommender")
root.geometry('1200x700')

# background
bg_gradient = tk.Canvas(root, width=1200, height=700)
bg_gradient.pack()
bg_gradient.create_rectangle(0, 0, 1200, 350, fill='#62a8c7', width=0)
bg_gradient.create_rectangle(0, 350, 1200, 700, fill='#c7d4e0', width=0)

# center square that buttons go into
main_frame = tk.Frame(root, bg='#f2f2f2', width=600, height=500)
main_frame.place(relx=0.5, rely=0.5, anchor='center')

# Title
title = Label(main_frame, text="Personalized Movie Recommender",
              bg="#f2f2f2", font=('Helvetica', 30))
title.pack(pady=30)

# Generate command (recommend movies)


def generate_recommendations():
    generate_btn.destroy()  # destroy the generate button
    genre_lbl.destroy()  # destroy the genre label
    lbl2 = Label(main_frame, text="Movies Recommended for you",
                 bg="#f2f2f2", font=('Helvetica', 20))
    lbl2.pack(pady=30)
    movies_to_display = recommend(movie_input)
    for movie in movies_to_display:
        movie_lbl = Label(main_frame, text=movie,
                          bg="#f2f2f2", font=('Helvetica', 15))
        movie_lbl.pack(pady=5)
    # Display recommended movies
    # comedy_movies = ['The Shawshank Redemption', 'The Godfather',
    #                  'The Dark Knight', 'The Godfather: Part II', '12 Angry Men']
    # romance_movies = ['The Notebook', 'Titanic',
    #                   'The Fault in Our Stars', 'The Vow', 'A Walk to Remember']
    # horror_movies = ['The Exorcist', 'The Shining',
    #                  'Get Out', 'Hereditary', 'Psycho']
    # drama_movies = ['The Shawshank Redemption',
    #                 'The Godfather', 'Forrest Gump', 'The Godfather: Part II']
    # action_movies = ['The Dark Knight', 'Avengers: Endgame',
    #                  'Inception', 'The Matrix', 'Die Hard']
    # if (genre_input == "Comedy"):
    #     for movie in comedy_movies:
    #         movie_lbl = Label(main_frame, text=movie,
    #                           bg="#f2f2f2", font=('Helvetica', 15))
    #         movie_lbl.pack(pady=5)
    # elif (genre_input == "Action"):
    #     for movie in action_movies:
    #         movie_lbl = Label(main_frame, text=movie,
    #                           bg="#f2f2f2", font=('Helvetica', 15))
    #         movie_lbl.pack(pady=5)
    # elif (genre_input == "Romance"):
    #     for movie in romance_movies:
    #         movie_lbl = Label(main_frame, text=movie,
    #                           bg="#f2f2f2", font=('Helvetica', 15))
    #         movie_lbl.pack(pady=5)
    # elif (genre_input == "Drama"):
    #     for movie in drama_movies:
    #         movie_lbl = Label(main_frame, text=movie,
    #                           bg="#f2f2f2", font=('Helvetica', 15))
    #         movie_lbl.pack(pady=5)
    # elif (genre_input == "Horror"):
    #     for movie in horror_movies:
    #         movie_lbl = Label(main_frame, text=movie,
    #                           bg="#f2f2f2", font=('Helvetica', 15))
    #         movie_lbl.pack(pady=5)

    # Will take user input when Begin button is clicked


def question1():
    global movie_input
    movie_input = simpledialog.askstring(
        "Similar movie", "What is a similar movie you want to watch?", parent=main_frame)

    # Ask additional questions
    # length_input = simpledialog.askstring(
    #     "length", "How long of a movie are you in the mood for? Something shorter or longer??", parent=main_frame)
    # mood_input = simpledialog.askstring(
    #     "mood", "What color descirbes your mood right now", parent=main_frame)
    # time_period_input = simpledialog.askstring(
    #     "Time Period", "What is your favorite time period for movies?", parent=main_frame)

    # Display additional question answers
    movie_lbl = tk.Label(main_frame, text="Your similar movie preference is " + movie_input,
                         bg="#f2f2f2", font=('Helvetica', 15))
    movie_lbl.pack(pady=10)
    # length_lbl = tk.Label(main_frame, text="You prefer to watch a " + length_input + " movie",
    #                       bg="#f2f2f2", font=('Helvetica', 15))
    # length_lbl.pack(pady=10)

    # mood_lbl = tk.Label(main_frame, text="Your current mood color is " + mood_input,
    #                     bg="#f2f2f2", font=('Helvetica', 15))
    # mood_lbl.pack(pady=10)

    # time_period_lbl = tk.Label(main_frame, text="Your favorite time period for movies is " + time_period_input,
    #                            bg="#f2f2f2", font=('Helvetica', 15))
    # time_period_lbl.pack(pady=10)

    quest1_button.destroy()

    # Generate button
    global generate_btn
    generate_btn = Button(main_frame, text="Generate Recommendations", fg="white",
                          bg="#62a8c7", command=generate_recommendations,
                          width=25, height=2, font=('Helvetica', 12))
    generate_btn.pack(pady=30)


genre_lbl = tk.Label(main_frame, text="", bg="#f2f2f2",
                     font=('Helvetica', 15))
genre_lbl.pack(pady=30)

# background color
root.configure(bg='#f2f2f2')

# user input when begin is pressed
quest1_button = Button(main_frame, text="Begin", fg="white", bg="#62a8c7",
                       command=question1, width=15, height=2, font=('Helvetica', 12))
quest1_button.pack(pady=30)

root.mainloop()
