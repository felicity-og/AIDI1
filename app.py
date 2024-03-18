from flask import *
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb')) 

@app.route('/')
def inputs():
    return render_template('inputs.html')

@app.route('/predictions', methods=['POST', 'GET'])
def predictions():
    if request.method =='POST':
        result= request.form.to_dict()
        result= list(result.values())
        output = model.predict(result)
        return render_template("predictions.html",output)

if __name__ == "__main__":
    app.run(debug=True)