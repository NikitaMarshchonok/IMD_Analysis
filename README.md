IMD Analysis Project
Description
This project predicts the genre of movies based on their textual descriptions. It uses Natural Language Processing (NLP) and Machine Learning to classify genres. 
The project demonstrates skills in data processing, text pre-processing, model building, and result visualization.

Features:
  Load and preprocess data from the IMDB_top_1000.csv file.
  Train a Logistic Regression model to classify movie genres.
  Save the trained model and vectorizer for future predictions.
  Predict the genre of a new movie description.
  Visualize results:
    Confusion Matrix.
    Classification Report.

How to Run
  Clone the repository: git clone https://github.com/NikitaMarshchonok/IMD_Analysis.git
                        cd IMD_Analysis
  Install dependencies: Ensure you have Python 3.8+ installed on your system.
                        pip install -r requirements.txt
  Run the project: python main.py

  Test predictions: Modify the movie description in main.py to test the model's predictions.


Prediction Example
  Movie Description: "A group of friends embark on a dangerous journey to destroy a powerful artifact."
  Predicted Genre: Comedy


pandas — for data manipulation.
scikit-learn — for text vectorization and model training.
nltk — for text preprocessing (stop-word removal).
matplotlib and seaborn — for visualization.


IMD_Analysis/
├── main.py                # Main file to run the project
├── data_processing.py     # Code for data preprocessing
├── model_training.py      # Code for training the model
├── predictor.py           # Code for genre prediction
├── IMDB_top_1000.csv      # Dataset with movie descriptions
├── requirements.txt       # Dependencies list
├── model.pkl              # Saved model
├── vectorizer.pkl         # Saved vectorizer
└── README.md              # Project description



Potential Improvements
Add more genres for classification.
Use more advanced models (e.g., Random Forest or Neural Networks).
Perform hyperparameter tuning.
Collect a custom dataset for testing.


Author
Nikita Marshchonok

LinkedIn: https://www.linkedin.com/in/nikita-marshchonok
GitHUB: https://github.com/NikitaMarshchonok
