import pandas as pd
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')  # Добавьте это перед использованием stopwords

def load_and_clean_data(filepath):
    # Загрузка данных
    data = pd.read_csv('IMDB_top_1000.csv')

    # Оставляем только нужные столбцы
    data = data[['Description', 'Genre']]

    # Берём только первый жанр
    data['Genre'] = data['Genre'].apply(lambda x: x.split(',')[0])

    # Оставляем популярные жанры
    popular_genres = data['Genre'].value_counts().index[:5]
    data = data[data['Genre'].isin(popular_genres)]

    # Предобработка текста
    stop_words = set(stopwords.words('english'))
    data['Description'] = data['Description'].apply(
        lambda x: ' '.join(word for word in x.lower().split() if word.isalnum() and word not in stop_words)
    )

    return data, popular_genres

if __name__ == "__main__":
    print("Модуль data_processing.py работает!")
