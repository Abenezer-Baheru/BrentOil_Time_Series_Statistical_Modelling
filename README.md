# Brent Oil Prices Time Series Analysis

This project involves the exploration and preprocessing of Brent Oil prices time series data. The primary objective is to perform Exploratory Data Analysis (EDA) and preprocessing, followed by statistical modeling and forecasting. The project is implemented using Python and various data science libraries.

## Project Structure

```
BrentOil_Time_Series_Statistical_Modelling/
├── src/
│   ├── data/
│   │   ├── BrentOilPrices.csv
│   │   ├── BrentOilPrices_cleaned.csv
├── app/
│   ├── app.py
├── dashboard/
│   ├── public
│   ├── src
├── scripts/
│   ├── EDA_and_Preprocessing.py
│   ├── test_EDA_and_Preprocessing.py
│   ├── __init__.py
├── tests/
│   ├── test_EDA_and_Preprocessing.py
│   ├── __init__.py
├── notebooks/
│   ├── EDA_and_Preprocessing.ipynb
│   ├── __init__.py
├── .gitignore
├── requirements.txt
├── README.md
```

## Getting Started

### Prerequisites

Ensure you have the following libraries installed:

- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- warnings
- logging
- tensorflow
- pymc
- ruptures
- arch
- Flask

You can install the required libraries using the following command:

```bash
pip install pandas numpy matplotlib seaborn statsmodels
```

### Project Setup

1. Clone the repository:

```bash
git clone https://github.com/Abenezer-Baheru/BrentOil_Time_Series_Statistical_Modelling.git
cd BrentOil_Time_Series_Statistical_Modelling
```

2. Navigate to the project directory:

```bash
cd BrentOil_Time_Series_Statistical_Modelling
```

3. Ensure the data files (`BrentOilPrices.csv`) are located in the `src/data` directory.

## Usage

### EDA and Preprocessing

1. The `EDA_and_Preprocessing.py` script contains the `EDA_and_Preprocessing` class, which includes methods for various EDA and preprocessing tasks.
2. The `EDA_and_Preprocessing.ipynb` notebook provides a step-by-step guide to using the `EDA_and_Preprocessing` class and visualizing the data.

To run the notebook:

```bash
jupyter notebook notebooks/EDA_and_Preprocessing.ipynb
```

### Testing

Unit tests for the `EDA_and_Preprocessing` class are provided in the `test_EDA_and_Preprocessing.py` script in the `tests` directory. To run the tests:

```bash
python -m unittest discover tests
```

## Project Files

- `src/data/BrentOilPrices.csv`: The raw dataset containing Brent Oil prices.
- `src/data/BrentOilPrices_cleaned.csv`: The cleaned dataset after preprocessing.
- `app/app.py`: The Flask backend application.
- `dashboard/`: The React frontend application.
- `scripts/EDA_and_Preprocessing.py`: The script containing the `EDA_and_Preprocessing` class.
- `tests/test_EDA_and_Preprocessing.py`: The script containing unit tests for the `EDA_and_Preprocessing` class.
- `notebooks/EDA_and_Preprocessing.ipynb`: The Jupyter notebook for EDA and preprocessing.
- `README.md`: The project documentation.

## Model Evaluation and Comparison

### ARIMA and GARCH Model

### VAR Model

1. **Training**: Fit a VAR model using differenced data.
2. **Evaluation**: Calculate RMSE and MAE for the VAR model predictions.

### LSTM Model

1. **Training**: Prepare data and fit an LSTM model.
2. **Evaluation**: Calculate RMSE and MAE for the LSTM model predictions.

## Developing an Interactive Dashboard for Data Analysis Results

### Backend (Flask)

1. **Create the Flask App**: Define your Flask application in `app/app.py`.

### Frontend (React)

1. **Create the React App**: Set up your React application.
2. **Install Dependencies**: Install necessary dependencies.
3. **Fetch Data and Display Visualizations**:
4. **Proxy Setup**: Add proxy in `package.json`.

### Key Features

- Present historical trends, forecasts, and correlations with events.
- Allow users to see how specific events influenced Brent oil prices.
- Enable users to filter data, select date ranges, and drill down into details for deeper insights.
- Display key indicators like volatility, average price changes, and model accuracy metrics (e.g., RMSE, MAE).

## Author

- **Abenezer E.** - [Abenezer-Baheru](https://github.com/Abenezer-Baheru)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
