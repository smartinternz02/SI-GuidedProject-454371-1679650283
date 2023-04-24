from flask import Flask, render_template, request
import numpy as np 
import pickle
import pandas as pd 

model=pickle.load(open(r"C:\Users\Akula sandesh varma\ml project\flask\payments.pkl",'rb'))
app = Flask(__name__)

@app.route("/")
def about():
    return render_template('home.html')

@app.route("/home")
def about1():
    return render_template('home.html')

@app.route("/predict")
def home1():
    return render_template('predict.html')

@app.route("/pred", methods=['POST','GET'])
def predict():
    x=[[x for x in request.form.values()]]
    print(x)

    x = np.array(x)
    print(x.shape)

    print(x)
    pred = model.predict(x)
    print(pred[0])
    output = " "
    if pred[0]==0:
        output = "is not fraud"
    else:
        output = "is fraud"


    return render_template('submit.html',p = output)


if __name__ == "__main__":
    app.run(debug=False)