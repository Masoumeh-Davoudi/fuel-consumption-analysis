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
            the dataset to be clean.
        """
        self.dataset = dataset

    def remove_whitespace(self):
        """
        Removes leading and trailing whitespaces from string columns.

        Returns
        -------
        pd.DataFrame
            A dataset with leading and trailing whitespaces is handled.

        """
        return self.dataset.apply(lambda x:
                                  x.str.strip() if x.dtype == "object" else x)

    def missing_values(self):
        """
        finds the missing value count in the dataset.

        Returns
        -------
        pd.Series
            Number of missing value of each column.

        Examples
        --------
        >>> data = pd.DataFrame(
        >>>    {"Name": [
        >>>        "Tara",
        >>>        "Alice",
        >>>        "Ali",
        >>>        "Sara",
        >>>        "Fara"
        >>>    ],
        >>>     "Age": [24, 33, np.nan, 19, 26],
        >>>     "Salary": [2000, np.nan, 3500, 4000, 2700],
        >>>     "Department": ["Finance", np.nan, "IT", np.nan, "IT"]
        >>>    }
        >>> )
        >>> print(DataCleaning(data).missing_values())
        """
        return self.dataset.isnull().sum()

    def replace_missing_values(self):
        """
        replaces missing values in the datasets:
        - categorical value with mode,
        - numerical value with mean.

        Returns
        -------
        pd.DataFrame
            A dataset that missing values handled.

        Examples
        --------
        >>> DataCleaning(data).replace_missing_values()
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
        finds the duplicate rows in the dataset.

        Returns
        -------
        duplicate_rows : pd.DataFrame
            DataFrame containing duplicate rows.

        Examples
        --------
        >>> print(DataCleaning(data).find_duplicates())
        """
        duplicate_rows = self.dataset[self.dataset.duplicated(keep=False)]
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
        >>> DataCleaning(data).remove_duplicates()
        """
        return self.dataset.drop_duplicates()
