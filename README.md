# BugSense AI 🐛

An AI-powered web application that automatically classifies bug reports by severity and category using Natural Language Processing and Machine Learning.

## What Problem Does It Solve?

In software companies, testers write dozens of bug reports every day. Manually reading and prioritizing each bug wastes hours. BugSense AI solves this by instantly classifying any bug report into:

- **Severity** → Critical / High / Medium / Low
- **Category** → Backend / UI / Performance / Security

## Tech Stack

- **Python** — Core programming language
- **Flask** — Web framework for backend API
- **Scikit-learn** — Machine learning library
- **TF-IDF Vectorizer** — Converts bug text into numbers
- **Logistic Regression** — Classifies severity and category
- **Chart.js** — Interactive dashboard charts
- **Bootstrap 5** — Frontend styling

## Features

- Paste any bug report and get instant classification
- Confidence score showing how sure the model is
- Real time dashboard with charts
- Bug history table with timestamps
- Responsive dark themed UI

## Project Structure
BugSenseAI/
├── app.py              # Flask backend and API routes
├── model.py            # ML model training script
├── bugs.csv            # Training dataset (118 bug reports)
├── models/
│   ├── severity_model.pkl
│   └── category_model.pkl
└── templates/
    ├── index.html      # Main classifier page
    └── dashboard.html  # Analytics dashboard

## How To Run

1. Clone the repository
   git clone https://github.com/MerigalaPallavi/BugSenseAI.git
   cd BugSenseAI

2. Install dependencies
   pip install flask scikit-learn pandas numpy

3. Train the model
   python model.py

4. Run the app
   python app.py

5. Open browser and go to
   http://127.0.0.1:5000

## How It Works

1. User pastes a bug report into the text box
2. Flask sends the text to the trained ML model
3. TF-IDF converts text into numerical features
4. Logistic Regression predicts severity and category
5. Result is displayed with confidence score
6. Dashboard updates with charts and bug history

## Sample Results

| Bug Report | Severity | Category |
|-----------|----------|----------|
| App crashes on login | Critical | Backend |
| Button color is wrong | High | UI |
| Page loads in 15 seconds | High | Performance |
| SQL injection on search | High | Security |

## Developer

**Pallavi** — B.Tech AIML Student











