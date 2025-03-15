# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 22:15:16 2025

@author: Masoumeh
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class DataVisualization:
    """
    A class for visualizing data using Seaborn and Matplotlib.

    Atrributes:
        dataset : the dataset used for visualization.

    """

    def __init__(self, dataset):
        """
        Initializes the dataset in the DataVisualization class.

        Parameters:
            dataset: A pandas csv file containing the data to be visualized.
        """

        self.dataset = dataset

    def scatter_plot(self, x_axis, y_axis, hue_column):
        """
        Creates a scatter plots to visualize the relationship between two numerical features.

        Parameters:
            x_axis (str): Column name for the x_axis (Numerical).
            y_axis (str): Column name for the y_axis (Numerical).
            hue_column: The points are colored based on the hue_column.
        """

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=x_axis, y=y_axis, hue=hue_column, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Scatter Plot: {x_axis} vs {y_axis}")
        plt.show()

    def line_plot(self, x_axis, y_axis, hue_column):
        """
        Create a line plot to show trends between two numerical variable.

        Parameters:
            x_axis: Column name for x_axis (Numerical).
            y_axis: Column name for x_axis (Numerical).
            hue_column: The lines are colored based on the hue_column.
        """
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=x_axis, y=y_axis, hue=hue_column, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Line Plot: {x_axis} vs {y_axis}")
        plt.show()

    def bar_plot(self, x_axis, y_axis):
        """
        Create a line plot to compare categories against a numerical variable.
        Parameters:
            x_axis: Column name for x_axis (Categorical).
            y_axis: Column name for x_axis (Numerical).
        """

        plt.figure(figsize=(10, 6))
        hue_column = "MAKE" if "MAKE" in self.dataset.columns else None
        sns.barplot(
            x=x_axis,
            y=y_axis,
            hue=hue_column,
            data=self.dataset,
            estimator=np.mean,
        )
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Bar Plot: {x_axis} vs {y_axis}")
        plt.xticks(rotation=45)
        plt.show()

    def box_plot(self, x_axis, y_axis):
        """
        Creates a box plot to show the distribution of a numerical variable across categorical variable.

        Parameters:
            x_axis: Column name for x_axis (Categorical).
            y_axis: Column name for x_axis (Numerical).

        Box plots help to identify the spread of the data and the outliers.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=x_axis, y=y_axis, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Box Plot: {x_axis} vs {y_axis}")
        plt.xticks(rotation=45)
        plt.show()

    def histogram_plot(self, x_axis):
        """
        Creates a histogram to show the distribution of a numerical variables.

        Parameters:
            x_axis: Column name for x_axis (Numerical)

        A KDE (Kernel Density Estimate) curve is overlaid on the histogram.
        """
        plt.figure(figsize=(10, 8))
        sns.histplot(x=x_axis, data=self.dataset, bins=10, kde=True)
        plt.xlabel(x_axis)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {x_axis} ")
        plt.xticks(rotation=45)
        plt.show()

    def heat_map_plot(self):
        """
        Creates a heatmap to visualize the correlation matrix of  the numerical variables.

        The correclation heatmap helps identify the relationship between numerical variables.

        """
        plt.figure(figsize=(10, 8))
        numerical_df = self.dataset.select_dtypes(include=[np.number])
        corr = numerical_df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap Only for Numerical Features")
        plt.xticks(rotation=45)
        plt.show()

    def count_plot(self, x_axis):
        """
        Creates a count plot to show the distribution of categories in a specified column.

         Parameters:
             x_axis: Column name for x_axis (Numerical)

        """
        plt.figure(figsize=(6, 8))
        sns.countplot(
            x=column,
            data=self.dataset,
            order=self.dataset[x_axis].value_counts().index,
        )
        plt.xlabel(x_axis)
        plt.ylabel("Count")
        plt.title(f"Distribution of {x_axis} ")
        plt.xticks(rotation=45)
        plt.show()
