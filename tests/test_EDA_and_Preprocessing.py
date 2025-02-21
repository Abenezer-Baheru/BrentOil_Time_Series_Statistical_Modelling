import unittest
import pandas as pd
import logging
# Ensure the scripts directory is in your Python path
import sys
sys.path.append('../scripts')
from EDA_and_Preprocessing import EDA_and_Preprocessing


class TestEDAAndPreprocessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("Setting up TestEDAAndPreprocessing class.")
        cls.data_path = '../src/data/BrentOilPrices.csv'
        cls.eda = EDA_and_Preprocessing(cls.data_path)
    
    def test_display_head(self):
        logging.info("Testing display_head method.")
        df_head = self.eda.display_head()
        self.assertIsInstance(df_head, pd.DataFrame)
        self.assertEqual(df_head.shape[1], self.eda.df.shape[1])
    
    def test_check_white_spaces(self):
        logging.info("Testing check_white_spaces method.")
        self.eda.check_white_spaces()
        # Assuming there should be no white spaces, which is checked in the method itself.
    
    def test_check_duplicates(self):
        logging.info("Testing check_duplicates method.")
        duplicate_rows = self.eda.df.duplicated().sum()
        self.assertEqual(duplicate_rows, 0)
    
    def test_check_missing_values(self):
        logging.info("Testing check_missing_values method.")
        missing_values = self.eda.df.isnull().sum().sum()
        self.assertEqual(missing_values, 0)
    
    def test_convert_to_datetime(self):
        logging.info("Testing convert_to_datetime method.")
        self.eda.convert_to_datetime()
        self.assertIsInstance(self.eda.df.index, pd.DatetimeIndex)
        self.assertEqual(self.eda.df.index.name, 'Date')
    
    def test_check_dataset_size(self):
        logging.info("Testing check_dataset_size method.")
        self.eda.check_dataset_size()
        self.assertGreater(self.eda.df.shape[0], 0)
        self.assertGreater(self.eda.df.shape[1], 0)

    def test_display_summary_statistics(self):
        logging.info("Testing display_summary_statistics method.")
        desc = self.eda.df.describe()
        self.assertIsInstance(desc, pd.DataFrame)
        self.assertEqual(desc.shape[1], self.eda.df.shape[1] - 1)  # Excluding Date column

    def test_plot_distribution(self):
        logging.info("Testing plot_distribution method.")
        try:
            self.eda.plot_distribution()
        except Exception as e:
            self.fail(f"plot_distribution() raised Exception unexpectedly: {e}")

    def test_plot_time_series(self):
        logging.info("Testing plot_time_series method.")
        try:
            self.eda.plot_time_series()
        except Exception as e:
            self.fail(f"plot_time_series() raised Exception unexpectedly: {e}")

    def test_decompose_time_series(self):
        logging.info("Testing decompose_time_series method.")
        try:
            self.eda.decompose_time_series()
        except Exception as e:
            self.fail(f"decompose_time_series() raised Exception unexpectedly: {e}")

    def test_plot_rolling_statistics(self):
        logging.info("Testing plot_rolling_statistics method.")
        try:
            self.eda.plot_rolling_statistics()
        except Exception as e:
            self.fail(f"plot_rolling_statistics() raised Exception unexpectedly: {e}")

    def test_plot_acf_pacf(self):
        logging.info("Testing plot_acf_pacf method.")
        try:
            self.eda.plot_acf_pacf()
        except Exception as e:
            self.fail(f"plot_acf_pacf() raised Exception unexpectedly: {e}")

    def test_plot_boxplot(self):
        logging.info("Testing plot_boxplot method.")
        try:
            self.eda.plot_boxplot()
        except Exception as e:
            self.fail(f"plot_boxplot() raised Exception unexpectedly: {e}")

    def test_create_heatmap(self):
        logging.info("Testing create_heatmap method.")
        try:
            self.eda.create_heatmap()
        except Exception as e:
            self.fail(f"create_heatmap() raised Exception unexpectedly: {e}")

    def test_save_cleaned_data(self):
        logging.info("Testing save_cleaned_data method.")
        cleaned_data_path = '../src/data/BrentOilPrices_cleaned_test.csv'
        try:
            self.eda.save_cleaned_data(cleaned_data_path)
            saved_df = pd.read_csv(cleaned_data_path)
            self.assertIsInstance(saved_df, pd.DataFrame)
            self.assertGreater(saved_df.shape[0], 0)
        except Exception as e:
            self.fail(f"save_cleaned_data() raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()