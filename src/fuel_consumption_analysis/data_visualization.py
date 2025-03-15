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
        Creates a scatter plots to visualize the relationship between two
        numerical features.

        Parameters:
            x_axis (str): Column name for the x_axis (Numerical).
            y_axis (str): Column name for the y_axis (Numerical).
            hue_column: The points are colored based on the hue_column.

        If there are too many unique categories in hue column, only the top 5
        will be displayed while others are grouped as 'other'
        """

        dataset_copy = self.dataset.copy()

        top_categories = dataset_copy[hue_column].value_counts().index[:5]

        dataset_filtered = dataset_copy[
            dataset_copy[hue_column].isin(top_categories)
        ]

        aggregated_data = (
            dataset_filtered.groupby([x_axis, hue_column])[y_axis]
            .mean()
            .reset_index()
        )
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x=x_axis,
            y=y_axis,
            hue=hue_column,
            data=aggregated_data,
            s=100,
            edgecolor="black",
            alpha=0.8,
        )
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Scatter Plot: {x_axis} vs Mean {y_axis}")
        plt.legend(
            title=hue_column,
            title_fontsize=14,
            fontsize=10,
            frameon=True,
            loc="upper left",
            bbox_to_anchor=(1, 1),
        )
        plt.tight_layout()
        plt.show()

    def bar_plot(self, x_axis, y_axis, hue_column):
        """
        Create a line plot to compare categories against a numerical variable.
        Parameters:
            x_axis: Column name for x_axis (Categorical).
            y_axis: Column name for x_axis (Numerical).
            hue_column: Column name to group data by different categories
            (Categorical)
        If there are too many unique categories in hue column, only the top 5
        will be displayed while others are grouped as 'other'
        """

        palette = sns.color_palette("Set2")

        # Plot
        plt.figure(figsize=(12, 6))
        sns.barplot(
            x=x_axis,
            y=y_axis,
            hue=hue_column,
            palette=palette,
            data=self.dataset,
            estimator=np.mean,
            errorbar=None,
        )

        plt.title("Average CO₂ Emissions by Fuel Type", fontsize=14)
        plt.xlabel("Fuel Type", fontsize=12)
        plt.ylabel("CO₂ Emissions (g/km)", fontsize=12)
        plt.legend(
            title=hue_column,
            bbox_to_anchor=(1, 1),
            loc="upper left",
            fontsize=10,
        )
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
            x=x_axis,
            data=self.dataset,
            order=self.dataset[x_axis].value_counts().index,
        )
        plt.xlabel(x_axis)
        plt.ylabel("Count")
        plt.title(f"Distribution of {x_axis} ")
        plt.xticks(rotation=45)
        plt.show()
