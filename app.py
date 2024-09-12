from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__, template_folder='views')

# Load the model
with open('C:/Users/USER/Documents/my_first_linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        features = [float(request.form[f'feature_{i}']) for i in range(1, 7)]  # Assuming 7 features
        prediction = model.predict([np.array(features)])[0]
    return render_template('index.html', prediction=prediction)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(data['features'])])
    return jsonify(prediction[0])

if __name__ == '__main__':
    app.run(port=5000, debug=True)