from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

# All files are in the same folder
app = Flask(__name__, template_folder=".")

# Load trained model
model = joblib.load("blood_sugar_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_data = pd.DataFrame([{
            "Age": float(data["Age"]),
            "BMI": float(data["BMI"]),
            "Physical_Activity_Min": float(data["Physical_Activity_Min"]),
            "Sleep_Hours": float(data["Sleep_Hours"]),
            "Stress_Level": float(data["Stress_Level"]),
            "Daily_Carb_Intake_g": float(data["Daily_Carb_Intake_g"]),
            "Family_History": int(data["Family_History"]),
            "Previous_Glucose": float(data["Previous_Glucose"])
        }])

        prediction = model.predict(input_data)[0]

        return jsonify({
            "success": True,
            "prediction": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)