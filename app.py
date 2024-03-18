from flask import Flask, render_template, request, url_for
import numpy as np
import pickle


app = Flask(__name__)
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in) 

@app.route('/')
def inputs():
    return render_template('inputs.html')

@app.route('/predictions', methods=['GET','POST'])
def predictions():
    if request.method =='POST':
        result= request.form
        result= list(result.values())
        result= np.array(result)
        output = model.predict(result)[0]
        return render_template("predictions.html")

if __name__ == "__main__":
    app.run(debug=True)