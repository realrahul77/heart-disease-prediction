from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        final_input = np.array([data])
        prediction = model.predict(final_input)[0]
        output = "🫀 Person is likely to have Heart Disease" if prediction == 1 else "💚 Person is Healthy"
        return render_template('index.html', prediction_text=output)
    except:
        return render_template('index.html', prediction_text="⚠️ Please enter valid numeric values")

if __name__ == "__main__":
    app.run(debug=True)
