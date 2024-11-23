import data_processing
print(data_processing.load_and_clean_data)  # Проверяем доступность функции

from model_training import train_model
from predictor import predict_genre

import os



print("Текущая рабочая директория:", os.getcwd())  # Показывает текущую директорию
print("Файлы в папке:", os.listdir())  # Показывает файлы в текущей директории



if __name__ == "__main__":
    # Загрузка и очистка данных
    data, popular_genres = data_processing.load_and_clean_data('imdb_top_1000.csv')

    # Обучение модели
    model, vectorizer, X_test, y_test = train_model(data)
    print("Модель обучена!")

    # Пример предсказания
    description = "A young wizard discovers his magical heritage and faces a dark enemy."
    genre = predict_genre(description)
    print(f"Описание: {description}")
    print(f"Предсказанный жанр: {genre}")
