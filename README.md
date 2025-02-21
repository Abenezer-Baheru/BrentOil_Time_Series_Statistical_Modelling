Sure! Here is the complete `README.md` file for your project:

### README.md

```markdown
# Brent Oil Prices Time Series Analysis

This project involves the exploration and preprocessing of Brent Oil prices time series data. The primary objective is to perform Exploratory Data Analysis (EDA) and preprocessing, followed by statistical modeling and forecasting. The project is implemented using Python and various data science libraries.

## Project Structure

```
BrentOil_Time_Series_Statistical_Modelling/
├── data/
│   ├── BrentOilPrices.csv
│   ├── BrentOilPrices_cleaned.csv
├── scripts/
│   ├── EDA_and_Preprocessing.py
│   └── test_EDA_and_Preprocessing.py
├── tests/
│   ├── test_EDA_and_Preprocessing.py
│   └──__init__
├── notebooks/
│   └── EDA_and_Preprocessing.ipynb
└── README.md
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

3. Ensure the data files (`BrentOilPrices.csv`) are located in the `data` directory.

## Usage

### EDA and Preprocessing

1. The `EDA_and_Preprocessing.py` script contains the `EDA_and_Preprocessing` class, which includes methods for various EDA and preprocessing tasks.
2. The `EDA_and_Preprocessing.ipynb` notebook provides a step-by-step guide to using the `EDA_and_Preprocessing` class and visualizing the data.

To run the notebook:

```bash
jupyter notebook notebooks/EDA_and_Preprocessing.ipynb
```

### Testing

Unit tests for the `EDA_and_Preprocessing` class are provided in the `test_EDA_and_Preprocessing.py` script. To run the tests:

```bash
python scripts/test_EDA_and_Preprocessing.py
```

## Project Files

- `data/BrentOilPrices.csv`: The raw dataset containing Brent Oil prices.
- `data/BrentOilPrices_cleaned.csv`: The cleaned dataset after preprocessing.
- `scripts/EDA_and_Preprocessing.py`: The script containing the `EDA_and_Preprocessing` class.
- `notebooks/EDA_and_Preprocessing.ipynb`: The Jupyter notebook for EDA and preprocessing.
- `README.md`: The project documentation.

## Authors

- **Your Name** - [Abenezer B.](https://github.com/Abenezer-Baheru/BrentOil_Time_Series_Statistical_Modelling)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This `README.md` provides an overview of the project, setup instructions, usage guidelines, and testing information. It also includes sections for authors, license, and acknowledgments. You can customize it further based on your project's specific details and requirements.
