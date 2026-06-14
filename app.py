from flask import Flask, render_template, request, jsonify
import pickle
import json
from datetime import datetime

app = Flask(__name__)

# loading both models i trained earlier
sev_model = pickle.load(open("models/severity_model.pkl", "rb"))
cat_model = pickle.load(open("models/category_model.pkl", "rb"))

# this list keeps track of all bugs classified in current session
all_bugs = []

# severity levels with color names
severity_colors = {
    "Critical": "Red",
    "High": "Orange",
    "Medium": "Yellow",
    "Low": "Green"
}

# home page
@app.route("/")
def home():
    return render_template("index.html")

# this route takes bug text and returns prediction
@app.route("/predict", methods=["POST"])
def predict():
    incoming = request.get_json()
    bug_text = incoming.get("text", "").strip()

    # dont process empty input
    if not bug_text:
        return jsonify({"error": "Bug description cannot be empty"}), 400

    # run both models
    severity = sev_model.predict([bug_text])[0]
    category = cat_model.predict([bug_text])[0]

    # get how confident the model is
    proba = sev_model.predict_proba([bug_text])[0]
    confidence = round(max(proba) * 100, 1)

    # build the result
    bug_result = {
        "text": bug_text,
        "severity": severity,
        "category": category,
        "confidence": confidence,
        "color": severity_colors.get(severity, "Grey"),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    # save it to our list
    all_bugs.append(bug_result)

    return jsonify(bug_result)

# dashboard page to see all bugs
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",
                           data=json.dumps(all_bugs),
                           total=len(all_bugs))

# api to get raw bug history
@app.route("/history")
def history():
    return jsonify(all_bugs)

if __name__ == "__main__":
    app.run(debug=True)