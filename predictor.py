import pickle

def predict_genre(description):
    # Загрузка модели и векторизатора
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    # Предсказание
    vectorized_desc = vectorizer.transform([description]).toarray()
    genre = model.predict(vectorized_desc)
    return genre[0]
