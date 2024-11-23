from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

def train_model(data):
    # Векторизация текста
    vectorizer = CountVectorizer(max_features=5000)
    X = vectorizer.fit_transform(data['Description']).toarray()
    y = data['Genre']

    # Разделение на обучение и тест
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Обучение модели
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Сохранение модели и векторизатора
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

    return model, vectorizer, X_test, y_test