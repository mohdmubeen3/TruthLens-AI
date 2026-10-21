# 🔍 TruthLens AI

An AI-powered News Credibility Analyzer built using **Natural Language Processing (NLP)** and **Machine Learning**.

TruthLens AI classifies complete news articles as **Real** or **Fake** based on linguistic patterns learned from a labeled dataset.

> ⚠️ This application is an ML-based classifier, not a real-time fact-checking system.

---


## ✨ Features

- 🔍 Analyze complete news articles
- 🤖 Linear SVM classifier
- 📊 TF-IDF feature extraction
- 🌐 Flask web application
- 🎨 Responsive modern UI
- 📰 Example article feature
- 📈 Model performance metrics

---

## 🧠 Machine Learning Pipeline

Dataset

↓

Text Cleaning

↓

Tokenization

↓

Stopword Removal

↓

Stemming

↓

TF-IDF Vectorization

↓

Model Training

↓

Prediction

---

## 📊 Models Compared

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 99.03% |
| Passive Aggressive | 99.71% |
| **Linear SVM** | **99.73%** ✅ |
| Random Forest | 99.52% |
| Naive Bayes | 95.63% |

---

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- NLTK
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
TruthLens-AI
│
├── app.py
├── requirements.txt
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
│
├── static
│   ├── style.css
│   └── script.js
│
├── templates
│   └── index.html
│
├── utils
│   └── preprocess.py
│
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/TruthLens-AI.git

cd TruthLens-AI

pip install -r requirements.txt

python app.py
```

---

## 🎯 Future Improvements

- Fact-checking using trusted APIs
- URL-based article analysis
- Explainable AI (LIME/SHAP)
- User authentication
- Docker support

---

## 👨‍💻 Developer

**Mohd Mubeen**

B.Tech CSE (AI & ML)

Machine Learning | NLP | Flask

---

⭐ If you found this project useful, consider giving it a star!
