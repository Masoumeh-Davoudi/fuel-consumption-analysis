# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 11:29:27 2025

@author: taher
"""


class DataCleaning:
    """Implements cleaning datasets."""

    def __init__(self, dataset):
        """
        Initialize with a pandas DataFrame.

        Parameters
        ----------
        dataset : pd.DataFrame
            the dataset that should be clean.
        """
        self.dataset = dataset
        
    def remove_whitespace(self):
        

    def missing_values(self):
        """
        finds the missing value in the dataset.

        Returns
        -------
        pd.Series
            Number of missing value of each column.
        """
        return self.dataset.isnull().sum()

    def replace_missing_values(self):
        """
        replace the missing values in datasets:
        categorical value with mode,
        numerical value with mean.

        Returns
        -------
        pd.DataFrame
            Dataset that missing values handled.
        """
        missing_values = self.missing_values()
        if missing_values.sum() == 0:
            print("No Missing Values in Dataset")
            return self.dataset
        else:
            for column in self.dataset.columns:
                if self.dataset[column].dtype == "object":
                    self.dataset.loc[:, column] = self.dataset[column].fillna(
                        self.dataset[column].mode()[0]
                    )
                else:
                    self.dataset.loc[:, column] = self.dataset[column].fillna(
                        self.dataset[column].mean()
                    )
            return self.dataset

    def find_duplicates(self):
        """
        find the duplicate rows in the dataset.

        Returns
        -------
        duplicate_rows : pd.DataFrame
            DataFrame containing duplicate rows.

        """
        duplicate_rows = self.dataset[self.dataset.duplicated(keep=False)]
        if duplicate_rows.empty:
            print("No Duplicate Rows in Dataset.")
        else:
            print("Duplicate Rows:")
        return duplicate_rows

    def remove_duplicates(self):
        """
        Remove duplicate rows from the datasets.

        Returns
        -------
        pd.DataFrame
            Dataset without duplicates.

        """
        return self.dataset.drop_duplicates()
