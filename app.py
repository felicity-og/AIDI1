from flask import Flask, render_template, request, url_for
from joblib import load

app = Flask(__name__)
classifier= load('fish_classifier.joblib')

@app.route('/')
def inputs():
    return render_template('inputs.html')

@app.route('/predictions', methods=['GET','POST'])
def predictions():
    if request.method =='POST':
        result= request.form
        result= list(result.values())
        output = classifier.predict(result)[0]
        return render_template("predictions.html")

if __name__ == "__main__":
    app.run(debug=True)