from flask import Flask, render_template,request,redirect
import pickle
import numpy as np
from modules.heart_predict import predict_h
from modules.diabetes_predict import predict_d
from modules.park_predict import predict_par

model1 = pickle.load(open("C:/Users/Administrator/Desktop/Check2/ipynbFiles/heart_disease.sav", "rb"))
model2 = pickle.load(open("C:/Users/Administrator/Desktop/Check2/ipynbFiles/classifier.sav", "rb"))
model3=pickle.load(open('C:/Users/Administrator/Desktop/Check2/ipynbFiles/parkinsons.sav', "rb"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")
@app.route("/diabetes")
def diabetes():
    return render_template('diabetes.html')
@app.route("/park")
def park():
    return render_template('park.html')

@app.route("/predict_heart", methods=["POST", "GET"])
def predict_heart():
    if request.method == "POST":
        try:
            predict_list = [float(request.form[f"heart{i}"]) for i in range(1, 14)]
        except (KeyError, ValueError):
            return render_template('heart_result.html', prediction_text="Error: Invalid input. Please go back to the main page and try again.")
        prediction_text = predict_h(predict_list, model1)
        return render_template("heart_result.html", prediction_text=prediction_text)
    else:
        return render_template('heart_result.html',prediction_text="Please Go back to Main Page.")


@app.route("/predict_diabetes",methods=["POST","GET"])
def predict_diabetes():
    if request.method=='POST':
        try:
            predict_list = [float(request.form[f"heart{i}"]) for i in range(1, 9)]
        except (KeyError, ValueError):
            return render_template('diabetes_result.html', prediction_text="Error: Invalid input. Please go back to the main page and try again.")
        prediction_text = predict_d(predict_list, model2)
        return render_template("diabetes_result.html", prediction_text=prediction_text)
    else:
        return render_template('diabetes_result.html',prediction_text="Please Go back to Main Page.")


@app.route("/predict_park",methods=["POST","GET"])
def predict_park():
    if request.method=='POST':
        try:
            predict_list = [float(request.form[f"heart{i}"]) for i in range(1, 23)]
        except (KeyError, ValueError):
            return render_template('park_result.html', prediction_text="Error: Invalid input. Please go back to the main page and try again.")

        prediction_text = predict_par(predict_list, model3)
        return render_template("park_result.html", prediction_text=prediction_text)
    else:
        return render_template('park_result.html',prediction_text="Please Go back to Main Page.")



if __name__ == "__main__":
    app.run(debug=True)
