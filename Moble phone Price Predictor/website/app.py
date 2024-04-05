from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Create prediction function
def prediction(input_list):
    # Load the model
    filename = 'Model\my_predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)

    pred_value = model.predict([input_list])
    return pred_value


@app.route('/', methods = ['POST', 'GET'])
def index():
    pred = 0
    if request.method == 'POST':
        ram = request.form['ram']
        rom = request.form['rom']
        company = request.form['company']
        size = request.form['mobile_size']
        prim_cam = request.form['primary_cam']
        selfi_cam = request.form['selfi_cam']
        battery = request.form['battery']

        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(int(rom))
        feature_list.append(float(size))
        feature_list.append(int(prim_cam))
        feature_list.append(int(selfi_cam))
        feature_list.append(int(battery))

        #Get the company
        company_list = ['apple', 'nokia', 'oppo', 'redmi', 'samsung', 'vivo']

        for item in company_list:
            if item == company:
                feature_list.append(1)
            else:
                feature_list.append(0)

        pred = prediction(feature_list)*323.55
        pred = np.round(pred[0])
        print(pred)

        # print(feature_list)
        
    # return "වැඩේ ගොඩ"
    return render_template("index.html", pred = pred)

if __name__ == '__main__':
    app.run(debug=True)