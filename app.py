from flask import Flask, render_template, request, jsonify
import pandas as pd
from pandas_profiling import ProfileReport

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

def eda(path):
    df = pd.read_csv(path)
    report=ProfileReport(df)
    report.to_file(output_file='templates/output.html')

@app.route('/eda', methods=['POST'])  # This will be called from UI
def read_csv():
    if request.method=='POST':
        csv_file=request.files['path']
        csv_file.save(csv_file.filename)
        eda(csv_file.filename)
        return render_template("output.html")


if __name__ == '__main__':
    app.run()
