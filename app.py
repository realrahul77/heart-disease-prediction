from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained pipeline
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:

        # Create input dataframe
        input_data = pd.DataFrame(
            [
                {
                    "age": float(request.form["age"]),
                    "sex": float(request.form["gender"]),
                    "cp": float(request.form["cp"]),
                    "trestbps": float(request.form["trestbps"]),
                    "chol": float(request.form["chol"]),
                    "fbs": float(request.form["fbs"]),
                    # Hidden default values
                    "restecg": 1,
                    "thalch": 150,
                    "exang": 0,
                    "oldpeak": 1.0,
                    "slope": 1,
                    "ca": 0,
                    "thal": 2,
                }
            ]
        )

        prediction = model.predict(input_data)[0]

        if prediction == 1:

            result = {
                "status": "High Risk",
                "message": "Based on the provided clinical parameters, the model predicts a higher risk of heart disease. Please consult a qualified healthcare professional for proper medical evaluation.",
                "color": "danger",
            }

        else:

            result = {
                "status": "Low Risk",
                "message": "Based on the provided clinical parameters, the model predicts a lower risk of heart disease. This prediction is intended for educational purposes only and is not a medical diagnosis.",
                "color": "success",
            }

        return render_template("index.html", result=result)

    except Exception as e:

        return render_template(
            "index.html",
            result={"status": "Error", "message": str(e), "color": "warning"},
        )


if __name__ == "__main__":
    app.run(debug=True)
