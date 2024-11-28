import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

def train_intent_classifier():
    # Load dataset
    data = pd.read_csv('keyword_intent_dataset.csv')
    X = data['Keyword']
    y = data['Intent']

    # Create a text processing and classification pipeline
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'keyword_intent_model.pkl')
    print("Model trained and saved!")

if __name__ == "__main__":
    train_intent_classifier()