import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import lag_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import logging
import warnings

warnings.filterwarnings('ignore')

class EDA_and_Preprocessing:
    def __init__(self, data_path):
        self.data_path = data_path
        try:
            self.df = pd.read_csv(self.data_path)
            logging.info("Dataset loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading dataset: {e}")
    
    def display_head(self):
        return self.df.head()
    
    def check_white_spaces(self):
        try:
            logging.info("Column headers before stripping white spaces:")
            logging.info(self.df.columns)
            has_white_spaces = self.df.applymap(lambda x: isinstance(x, str) and x.strip() != x).any().any()
            logging.info(f"White spaces found in data: {has_white_spaces}")
        except Exception as e:
            logging.error(f"Error checking white spaces: {e}")
    
    def check_duplicates(self):
        try:
            duplicate_rows = self.df.duplicated().sum()
            logging.info(f"Number of duplicate rows: {duplicate_rows}")
        except Exception as e:
            logging.error(f"Error checking duplicate rows: {e}")
    
    def check_missing_values(self):
        try:
            missing_values = self.df.isnull().sum()
            logging.info(f"Missing values:\n{missing_values}")
        except Exception as e:
            logging.error(f"Error checking missing values: {e}")
    
    def convert_to_datetime(self):
        try:
            self.df['Date'] = pd.to_datetime(self.df['Date'], infer_datetime_format=True)
            self.df.set_index('Date', inplace=True)
            logging.info("Date column converted to datetime and set as index.")
        except Exception as e:
            logging.error(f"Error converting Date column to datetime: {e}")

    def create_heatmap(self):
        try:
            self.df['Year'] = self.df.index.year
            self.df['Month'] = self.df.index.month
            pivot_table = self.df.pivot_table(values='Price', index='Year', columns='Month', aggfunc='mean')
            plt.figure(figsize=(12, 8))
            sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap='coolwarm')
            plt.title('Heatmap of Monthly and Yearly Trends')
            plt.xlabel('Month')
            plt.ylabel('Year')
            plt.show()
            self.df.drop(['Year', 'Month'], axis=1, inplace=True)
        except Exception as e:
            logging.error(f"Error creating heatmap: {e}")

    def check_dataset_size(self):
        try:
            logging.info(f"Dataset contains {self.df.shape[0]} rows and {self.df.shape[1]} columns.")
        except Exception as e:
            logging.error(f"Error checking dataset size: {e}")
    
    def display_summary_statistics(self):
        try:
            logging.info(self.df.describe())
        except Exception as e:
            logging.error(f"Error displaying summary statistics: {e}")
    
    def plot_distribution(self):
        try:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.df['Price'], kde=True)
            plt.xlabel('Price (USD per barrel)')
            plt.title('Distribution of Brent Oil Prices')
            plt.show()
        except Exception as e:
            logging.error(f"Error plotting distribution: {e}")

    def plot_time_series(self):
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(self.df.index, self.df['Price'], label='Brent Oil Price')
            plt.xlabel('Date')
            plt.ylabel('Price (USD per barrel)')
            plt.title('Brent Oil Prices Over Time')
            plt.legend()
            plt.show()
        except Exception as e:
            logging.error(f"Error plotting time series: {e}")
    
    def decompose_time_series(self):
        try:
            decomposition = seasonal_decompose(self.df['Price'], model='multiplicative', period=12)
            fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 12))
            decomposition.observed.plot(ax=ax1, title='Observed')
            decomposition.trend.plot(ax=ax2, title='Trend')
            decomposition.seasonal.plot(ax=ax3, title='Seasonal')
            decomposition.resid.plot(ax=ax4, title='Residual')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logging.error(f"Error decomposing time series: {e}")
    
    def plot_rolling_statistics(self):
        try:
            rolling_mean = self.df['Price'].rolling(window=12).mean()
            rolling_std = self.df['Price'].rolling(window=12).std()
            self.df['Moving_Avg'] = self.df['Price'].rolling(window=12).mean()
            correlation_matrix = self.df.corr()
            logging.info(f"Correlation matrix:\n{correlation_matrix}")
            fig, axs = plt.subplots(2, 2, figsize=(15, 12))
            axs[0, 0].plot(self.df.index, self.df['Price'], label='Brent Oil Price')
            axs[0, 0].plot(self.df.index, self.df['Moving_Avg'], label='12-Month Moving Average', color='red')
            axs[0, 0].set_xlabel('Date')
            axs[0, 0].set_ylabel('Price (USD per barrel)')
            axs[0, 0].set_title('Brent Oil Prices with Moving Average')
            axs[0, 0].legend()
            axs[0, 1].plot(self.df.index, self.df['Price'], label='Brent Oil Price')
            axs[0, 1].plot(self.df.index, rolling_mean, label='12-Month Rolling Mean', color='red')
            axs[0, 1].plot(self.df.index, rolling_std, label='12-Month Rolling Std', color='green')
            axs[0, 1].set_xlabel('Date')
            axs[0, 1].set_ylabel('Price (USD per barrel)')
            axs[0, 1].set_title('Rolling Mean and Standard Deviation of Brent Oil Prices')
            axs[0, 1].legend()
            lag_plot(self.df['Price'], ax=axs[1, 0])
            axs[1, 0].set_title('Lag Plot')
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=axs[1, 1])
            axs[1, 1].set_title('Correlation Matrix')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logging.error(f"Error plotting rolling statistics: {e}")

    def plot_acf_pacf(self):
        try:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
            plot_acf(self.df['Price'], lags=50, ax=ax1)
            ax1.set_xlabel('Lags')
            ax1.set_ylabel('Autocorrelation')
            ax1.set_title('Autocorrelation Function (ACF) of Brent Oil Prices')
            plot_pacf(self.df['Price'], lags=50, ax=ax2)
            ax2.set_xlabel('Lags')
            ax2.set_ylabel('Partial Autocorrelation')
            ax2.set_title('Partial Autocorrelation Function (PACF) of Brent Oil Prices')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logging.error(f"Error plotting ACF and PACF: {e}")
    
    def plot_boxplot(self):
        try:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=self.df['Price'])
            plt.title('Boxplot of Brent Oil Prices')
            plt.xlabel('Price (USD per barrel)')
            plt.show()
        except Exception as e:
            logging.error(f"Error plotting boxplot: {e}")
    
    def save_cleaned_data(self, output_path):
        try:
            self.df.to_csv(output_path, index=False)
            logging.info(f"Cleaned data saved to {output_path}")
        except Exception as e:
            logging.error(f"Error saving cleaned data: {e}")