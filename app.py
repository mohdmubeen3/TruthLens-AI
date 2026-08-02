from flask import Flask, render_template, request, jsonify
import joblib

from utils.preprocess import preprocess_text

app = Flask(__name__)

# Load model and vectorizer once when the app starts
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        news = data.get("news", "").strip()

        if not news:
            return jsonify({
                "success": False,
                "message": "Please enter some news text."
            })

        # Preprocess
        cleaned = preprocess_text(news)

        # Vectorize
        vector = vectorizer.transform([cleaned])

        # Predict
        prediction = model.predict(vector)[0]

        # Decision score (since LinearSVC has no predict_proba)
        score = abs(model.decision_function(vector)[0])

        confidence = min(round(score * 100, 2), 99.99)

        result = "REAL NEWS" if prediction == 1 else "FAKE NEWS"

        return jsonify({
            "success": True,
            "prediction": result,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)