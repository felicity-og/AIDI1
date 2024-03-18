from flask import Flask, render_template, request, url_for
import joblib
import numpy as np
app = Flask(__name__)
classifier= joblib.load('fish_classifier.joblib')

@app.route('/')
def inputs():
    return render_template('inputs.html')

@app.route('/predictions', methods=['GET','POST'])
def predictions():
    if request.method =='POST':
        measurements = [x for x in request.form.values()]
        value = [np.array(measurements)]
        final = np.array(value, dtype=float) 
        predict = classifier.predict(final)
        return render_template("predictions.html",predict=predict[0] )

if __name__ == "__main__":
    app.run(debug=True)