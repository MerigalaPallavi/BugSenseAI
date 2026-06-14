import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("bugs.csv")
print(f"Total records loaded: {len(df)}")

# Create models folder
os.makedirs("models", exist_ok=True)

# ---- SEVERITY MODEL ----
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['severity'], test_size=0.2, random_state=42
)

severity_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=5000)),
    ('clf', LogisticRegression(max_iter=1000))
])

severity_pipeline.fit(X_train, y_train)
sev_predictions = severity_pipeline.predict(X_test)
print(f"Severity Model Accuracy: {accuracy_score(y_test, sev_predictions)*100:.2f}%")

# ---- CATEGORY MODEL ----
X_train2, X_test2, y_train2, y_test2 = train_test_split(
    df['text'], df['category'], test_size=0.2, random_state=42
)

category_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=5000)),
    ('clf', LogisticRegression(max_iter=1000))
])

category_pipeline.fit(X_train2, y_train2)
cat_predictions = category_pipeline.predict(X_test2)
print(f"Category Model Accuracy: {accuracy_score(y_test2, cat_predictions)*100:.2f}%")

# ---- SAVE MODELS ----
pickle.dump(severity_pipeline, open("models/severity_model.pkl", "wb"))
pickle.dump(category_pipeline, open("models/category_model.pkl", "wb"))

print("✅ Models saved successfully!")