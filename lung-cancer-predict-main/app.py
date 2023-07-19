from flask import Flask, render_template, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('models/lung_cancer_predictor_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    gender = int(data['GENDER'])
    age = int(data['AGE'])
    smoking = int(data['SMOKING'])
    yellow_fingers = int(data['YELLOW_FINGERS'])
    anxiety = int(data['ANXIETY'])
    peer_pressure = int(data['PEER_PRESSURE'])
    chronic_disease = int(data['CHRONIC_DISEASE'])
    fatigue = int(data['FATIGUE'])
    allergy = int(data['ALLERGY'])
    wheezing = int(data['WHEEZING'])
    alcohol_consuming = int(data['ALCOHOL_CONSUMPTION'])
    coughing = int(data['COUGHING'])
    shortness_of_breath = int(data['SHORTNESS_OF_BREATH'])
    swallowing_difficulty = int(data['SWALLOWING_DIFFICULTY'])
    chest_pain = int(data['CHEST_PAIN'])

    features = np.array([[gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]])

    predictions = model.predict(features)
    if predictions == 1:
        return jsonify({'message': 'This person has a very high chance of having lung cancer. Please see a doctor!'})
    elif predictions == 0:
        return jsonify({'message': 'The probability of this person having lung cancer is very low.'})

if __name__ == '__main__':
    app.run(debug=True)
