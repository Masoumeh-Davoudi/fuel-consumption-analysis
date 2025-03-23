# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 11:29:27 2025

@author: taher
"""
import pandas as pd


class DataCleaning:
    """Implements cleaning datasets."""

    def __init__(self, dataset):
        """
        Initialize with a pandas DataFrame.

        Parameters
        ----------
        dataset : pd.DataFrame
            the dataset to be cleaned.
        """
        assert isinstance(
            dataset, pd.DataFrame
        ), "The dataset must be a pandas DataFrame."

        self.dataset = dataset

    def remove_whitespace(self):
        """
        Removes leading and trailing whitespaces from string columns.

        Returns
        -------
        pd.DataFrame
            A dataset with leading and trailing whitespaces removed.
        """
        self.dataset.columns = self.dataset.columns.str.strip()

        # Check dataset contain at least one string (object) column
        assert any(self.dataset.dtypes == "object"), "No string cloumns found"

        # Apply strip() function to remove whitespace from string columns
        return self.dataset.apply(
            lambda x: x.str.strip() if x.dtype == "object" else x)

    def missing_values(self):
        """
        Finds the missing value count in the dataset.

        Returns
        -------
        pd.Series
            Number of missing value in each column.

        Examples
        --------
        >>> data = pd.DataFrame({
        >>>     "Name": ["Tara", "Alice", "Ali", "Sara", "Fara"],
        >>>     "Age": [24, 33, np.nan, 19, 26],
        >>>     "Salary": [2000, np.nan, 3500, 4000, 2700],
        >>>     "Department": ["Finance", np.nan, "IT", np.nan, "IT"]
        >>>    })
        >>> print(DataCleaning(data).missing_values())
        """
        return self.dataset.isnull().sum()

    def replace_missing_values(self):
        """
        Replaces missing values in the datasets:
        - Categorical value with mode,
        - Numerical value with mean.

        Returns
        -------
        pd.DataFrame
            A dataset where missing values are handled.

        Examples
        --------
        >>> cleaned_data = DataCleaning(data).replace_missing_values()
        >>> print(cleaned_data)
        """
        missing_values = self.missing_values()

        # If there are no missing valuse, return the dataset
        if missing_values.sum() == 0:
            print("No Missing Values in Dataset")
            return self.dataset
        else:
            for column in self.dataset.columns:
                if self.dataset[column].dtype == "object":
                    # Fill missing categorical values whit mode
                    self.dataset.loc[:, column] = self.dataset[column].fillna(
                        self.dataset[column].mode()[0]
                    )
                else:
                    # Fill missing numerical values whit mean
                    self.dataset.loc[:, column] = self.dataset[column].fillna(
                        self.dataset[column].mean()
                    )
            return self.dataset

    def find_duplicates(self):
        """
        Finds the duplicate rows in the dataset.

        Returns
        -------
        pd.DataFrame
            DataFrame containing duplicate rows.

        Examples
        --------
        >>> print(DataCleaning(data).find_duplicates())
        """
        duplicate_rows = self.dataset[self.dataset.duplicated(keep=False)]

        # Check if any duplicate rows exist
        if duplicate_rows.empty:
            print("No Duplicate Rows in Dataset.")
        else:
            print("Duplicate Rows:")
        return duplicate_rows

    def remove_duplicates(self):
        """
        Removes duplicate rows from the datasets.

        Returns
        -------
        pd.DataFrame
           A dataset without duplicates.

        Examples
        --------
        >>> cleaned_data = DataCleaning(data).remove_duplicates()
        >>> print(cleaned_data)
        """
        return self.dataset.drop_duplicates()
