# import pickle
# import numpy as np
# from flask import Flask, jsonify, render_template, request

# app = Flask(__name__)

# # Load the pickled model
# with open("diabetes_model.pkl", "rb") as f:
#     loaded_model = pickle.load(f)


# @app.route("/")
# def home():
#     return render_template("index.html")
# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     input_data = np.array(data["input_data"])

#     # Reshape and standardize the input data
#     input_data_reshaped = input_data.reshape(1, -1)
#     std_data = scaler.transform(input_data_reshaped)

#     # Make prediction using the loaded model
#     prediction = loaded_model.predict(std_data)

#     # Prepare the response
#     if prediction[0] == 0:
#         result = "You are not diabetic."
#     else:
#         result = "You are diabetic. Please consult a doctor."

#     return jsonify({"result": result})


# if __name__ == "__main__":
#     app.run(debug=True)

import pickle

import numpy as np
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Load the pickled model
with open("diabetes_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_data = np.array(data["input_data"])

    # Reshape the input data
    input_data_reshaped = input_data.reshape(1, -1)

    # Make prediction using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)

    # Prepare the response
    if prediction[0] == 0:
        result = "You are not diabetic."
    else:
        result = "You are diabetic. Please consult a doctor."

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
