# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 20:07:21 2025

@author: taher
"""
import matplotlib.pyplot as plt
import seaborn as sns


class DataAnalysis:
    """Impleiments data analysis on a given dataset."""

    def __init__(self, dataset):
        """
        Initialize whit a pandas DataFrame.

        Parameters
        ----------
        dataset : pd.DataFrame
            The dataset that should be analyse.
        """
        self.dataset = dataset

    def statistical_description(self):
        """
        Compute descriptive statistics(mean, median, standard deviation, etc.).

        Returns
        -------
        pd.DataFrame
            Summary statistics for numerical columns.
        """
        return self.dataset.describe()

    def correlation_matrix(self):
        """
        Compute and visulaize the correlation matrix for numerical features.
        """
        # Select numeric columns
        numeric_data = self.dataset.select_dtypes(include=["number"])
        if numeric_data.empty:
            print("No numeric columns in dataset.")
            return
        plt.figure(figsize=(10, 6))
        sns.heatmap(
            numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5
        )
        plt.title("Correlation Matrix")
        plt.show()
