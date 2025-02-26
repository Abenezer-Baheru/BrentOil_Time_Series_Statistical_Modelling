from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the analysis results data
data_path = '../src/data/BrentOilPrices.csv'
df = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')

# Define route to serve data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = df.to_dict(orient='records')
    return jsonify(data)

# Define route to serve model results (replace with actual model results)
@app.route('/api/model-results', methods=['GET'])
def get_model_results():
    # Dummy data for example purposes
    model_results = {
        "var_rmse": 96.02,
        "var_mae": 95.99,
        "lstm_rmse": 15.23,
        "lstm_mae": 12.34
    }
    return jsonify(model_results)

if __name__ == '__main__':
    app.run(debug=True)