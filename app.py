from flask import Flask, render_template, request, url_for, redirect
import joblib
from Text_Transformer import text_transformer as tt
import gunicorn

# load our model file
model = joblib.load('spam_sms_model.mnb')

# Object for Flask
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['input']
        # 1. Preprocess
        transformed_text = tt(input_text)

        # 2. Vectorize and Predict
        result = model.predict([transformed_text])[0]

        # 3. Display
        if result == 0:
            return render_template('index.html', prediction_text='NOT SPAM')
        else:
            return render_template('index.html', prediction_text='SPAM')


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')
