from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/seguro')
def seguro():
    price=request.args.get('price');
    power=request.args.get('power');
    insurance=(float(power)*0.001)+(float(price)*0.005);

    return render_template('seguro.html', insurance=insurance)

if __name__ == "__main__":
    app.run(debug=True)