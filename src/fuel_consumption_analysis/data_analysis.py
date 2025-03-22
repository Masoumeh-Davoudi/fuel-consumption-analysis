# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 20:07:21 2025

@author: taher
"""
import pandas as pd
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
        assert isinstance(
            dataset, pd.DataFrame
        ), "The dataset must be a pandas DataFrame."

        self.dataset = dataset

    def statistical_description(self):
        """
        Computes descriptive statistics(mean, median, SD, etc.).

        Returns
        -------
        pd.DataFrame
            Summary statistics for numerical columns.

        Examples
        --------
        print(DataAnalysis(data).statistical_description())
        """
        return self.dataset.describe()

    def categorical_description(self):
        """
        Counts the values in each categories for object columns in a DataFrame.

        Returns
        -------
        None (Prints the results).

        Examples
        --------
        print(DataAnalysis(data).categorical_description())
        """
        for col in self.dataset.select_dtypes(include=["object"]).columns:
            print(self.dataset[col].value_counts())
            print("-" * 35)

    def correlation_matrix(self):
        """
        Computes and visulaize the correlation matrix for numerical features.

        Returns
        -------
        None (Plots the heatmap).
        """
        # Select numeric columns
        numeric_data = self.dataset.select_dtypes(include=["number"])
        if numeric_data.empty:
            print("No numeric columns in dataset.")
            return
        plt.figure(figsize=(10, 6))
        sns.heatmap(
            numeric_data.corr(), annot=True, cmap="coolwarm",
            fmt=".2f", linewidths=0.5
        )
        plt.title("Correlation Matrix")
        plt.show()
