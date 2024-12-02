import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Anime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    text = text.lower().strip()
    tokens = word_tokenize(text)
    tokens = [
        word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)


def get_recommendations(user_input):
    user_input_processed = preprocess_text(user_input)
    animes = Anime.objects.all()

    anime_data = []
    for anime in animes:
        title = anime.title
        synopsis = anime.synopsis or ""
        background = anime.background or ""
        genres = " ".join(anime.genres) if anime.genres else ""
        image = anime.image.url if hasattr(
            anime.image, 'url') else anime.image or ""

        anime_data.append({
            'id': anime.id,
            'image': image,
            'youtube_url': anime.youtube_url or "",
            'title': title,
            'genres': anime.genres,
            'type': anime.type or "",
            'episodes': anime.episodes or 0,
            'status': anime.status or "",
            'rating': anime.rating or "",
            'score': anime.score or 0,
            'synopsis': synopsis,
            'background': background,
            'year': anime.year or 0,
            'combined_features': preprocess_text(synopsis) + " " + preprocess_text(background) + " " + preprocess_text(genres)
        })

    anime_df = pd.DataFrame(anime_data)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(anime_df['combined_features'])
    user_input_vec = vectorizer.transform([user_input_processed])
    cosine_sim = cosine_similarity(user_input_vec, tfidf_matrix)
    similar_anime_idx = cosine_sim.argsort()[0][-10:][::-1]

    recommended_animes = [
        {
            'id': anime_df.iloc[idx]['id'],
            'image': anime_df.iloc[idx]['image'],
            'youtube_url': anime_df.iloc[idx]['youtube_url'],
            'title': anime_df.iloc[idx]['title'],
            'genres': anime_df.iloc[idx]['genres'],
            'type': anime_df.iloc[idx]['type'],
            'episodes': anime_df.iloc[idx]['episodes'],
            'status': anime_df.iloc[idx]['status'],
            'rating': anime_df.iloc[idx]['rating'],
            'score': anime_df.iloc[idx]['score'],
            'synopsis': anime_df.iloc[idx]['synopsis'],
            'background': anime_df.iloc[idx]['background'],
            'year': anime_df.iloc[idx]['year'],
        }
        for idx in similar_anime_idx
    ]

    return recommended_animes
