from flask import Flask, render_template, request, url_for
import pickle
import os
import sys
import warnings



def likely_error():
    accept_deprecated_sklearn_package_install = os.environ.get(
        "SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL", "unset"
    )
    accept_deprecated_sklearn_package_install = (
        accept_deprecated_sklearn_package_install.lower()
    )

    if accept_deprecated_sklearn_package_install == "true":
        return

app = Flask(__name__)
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in) 

@app.route('/inputs')
def inputs():
    return render_template('inputs.html')

@app.route('/predictions', methods=['GET','POST'])
def predictions():
    if request.method =='POST':
        result= request.form
        result= list(result.values())
        output = model.predict(result)[0]
        return render_template("predictions.html")

if __name__ == "__main__":
    app.run(debug=True)