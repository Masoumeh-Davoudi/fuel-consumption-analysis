# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 22:15:16 2025

@author: Masoumeh
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class DataVisualization:
    """
    A class for visualizing data using Seaborn and Matplotlib.

    Attributes
    ----------
        dataset : the dataset used for visualization.

    """

    def __init__(self, dataset):
        """
        Initializes the dataset in the DataVisualization class.

        Parameters
        ----------
            dataset: The file path to a CSV file containing the data to be visualized.
        """

        assert isinstance(
            dataset, pd.DataFrame
        ), "The dataset must be a pandas DataFrame."

        self.dataset = dataset  # Store dataset for visualization

    def scatter_plot(self, x_axis, y_axis, hue_column):
        """
        Creates a scatter plots to visualize the relationship between two
        numerical features.

        Parameters
        ----------
            x_axis (str): Column name for the x-axis (numerical).
            y_axis (str): Column name for the y-axis (numerical).
            hue_column (str): Column name used for color grouping (categorical).

        If there are too many unique categories in hue column, only the top 5
        will be displayed.

        Example
        -------
            DataVisualization(cleaned_data).scatter_plot("ENGINE SIZE", "FUEL CONSUMPTION", "MAKE")
        """
        numerical_cols = self.dataset.select_dtypes(
            include=["number"]
        ).columns.tolist()

        categorical_cols = self.dataset.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        assert (
            x_axis in numerical_cols
        ), f"Error: {x_axis} is not a numerical column"
        assert (
            y_axis in numerical_cols
        ), f"Error: {y_axis} is not a numerical column"
        assert (
            hue_column in categorical_cols
        ), f"Error: {hue_column} is not a categorical column"

        dataset_copy = (
            self.dataset.copy()
        )  # Create a copy to avoid modifying the original dataset

        top_categories = (
            dataset_copy[hue_column].value_counts().index[:5]
        )  # Get the top 5 frequent categories in hue_column

        # Filter the dataset to keep only these top categories
        dataset_filtered = dataset_copy[
            dataset_copy[hue_column].isin(top_categories)
        ]

        # Aggregate data by taking the mean of y_axis for each (x_axis, hue_column) pair.
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
            s=100,  # Set point size
            edgecolor="black",
            alpha=0.8,  # Adjust transparency for better visibility
        )
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Scatter Plot: {x_axis} vs Mean {y_axis}")

        # Adjust legend position
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
        Creates a bar plot to compare categories against a numerical variable.
        Parameters
        ----------
            x_axis: Column name for x_axis (Categorical).
            y_axis: Column name for y_axis (Numerical).
            hue_column: Column name to group data by different categories
            (Categorical)
        Example
        -------
            DataVisualization(cleaned_data).bar_plot("FUEL","COEMISSIONS","VEHICLE CLASS")
        """
        numerical_cols = self.dataset.select_dtypes(
            include=["number"]
        ).columns.tolist()

        categorical_cols = self.dataset.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        assert (
            x_axis in categorical_cols
        ), f"Error: {x_axis} is not a categorical column"

        assert (
            y_axis in numerical_cols
        ), f"Error: {y_axis} is not a numerical column"

        assert (
            hue_column in categorical_cols
        ), f"Error: {hue_column} is not a categorical column"

        # Generate a color pallete based on unique categories in hue_column
        palette = sns.color_palette(
            "tab20", n_colors=self.dataset[hue_column].nunique()
        )

        plt.figure(figsize=(12, 6))
        sns.barplot(
            x=x_axis,
            y=y_axis,
            hue=hue_column,
            palette=palette,
            data=self.dataset,
            estimator=np.mean,  # Use mean as aggregation function
            errorbar=None,
            dodge=True,  # Ensure bars are side by side instead of stacked
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
        plt.xticks(
            rotation=0, ha="center"
        )  # Rotate labels for better readability
        plt.show()

    def box_plot(self, x_axis, y_axis):
        """
        Creates a box plot to show the distribution of a numerical variable across categorical variable.

        Parameters
        ----------
            x_axis: Column name for x_axis (Categorical).
            y_axis: Column name for y_axis (Numerical).

        Box plots help to identify the spread of the data and the outliers.

        Example
        -------
            DataVisualization(cleaned_data).box_plot("VEHICLE CLASS", "FUEL CONSUMPTION")
        """

        numerical_cols = self.dataset.select_dtypes(
            include=["number"]
        ).columns.tolist()

        categorical_cols = self.dataset.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        assert (
            x_axis in categorical_cols
        ), f"Error: {x_axis} is not a categorical column"

        assert (
            y_axis in numerical_cols
        ), f"Error: {y_axis} is not a numerical column"

        plt.figure(figsize=(10, 6))
        sns.boxplot(x=x_axis, y=y_axis, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Box Plot of {x_axis} vs {y_axis}")
        plt.xticks(rotation=45)
        plt.show()

    def histogram_plot(self, x_axis):
        """
        Creates a histogram to show the distribution of a numerical variables.

        Parameters
        ----------
            x_axis: Column name for x_axis (Numerical)

        A KDE (Kernel Density Estimate) curve is overlaid on the histogram.

        Example
        -------
            DataVisualization(cleaned_data).histogram_plot("COEMISSIONS")
        """

        numerical_cols = self.dataset.select_dtypes(
            include=["number"]
        ).columns.tolist()

        assert (
            x_axis in numerical_cols
        ), f"Error: {x_axis} is not a Numerical column"

        plt.figure(figsize=(10, 8))
        sns.histplot(
            x=x_axis, data=self.dataset, bins=10, kde=True
        )  # Add KDE for smooth density estimation
        plt.xlabel(x_axis)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {x_axis} ")
        plt.xticks(rotation=45)
        plt.show()

    def heat_map_plot(self):
        """
        Creates a heatmap to visualize the correlation matrix of  the numerical variables.

        The correlation heatmap helps identify the relationship between numerical variables.

        Parameters
        ----------
            None
        Example
        -------
            DataVisualization(cleaned_data).heat_map_plot()
        """

        plt.figure(figsize=(10, 8))
        numerical_df = self.dataset.select_dtypes(
            include=[np.number]
        )  # Select only numerical columns
        print(
            "This is the list of numerical features that you can check their correclations: "
        )
        print(numerical_df.columns.tolist())

        x_selected = input("Please enter the first feature name (x_axis): ")
        y_selected = input("Please enter the second feature name (y_axis): ")

        if not x_selected or not y_selected:
            print("Feature names cannot be empty")
            return

        if x_selected not in numerical_df or y_selected not in numerical_df:
            print("One or both feature names are incorrect")
            return

        selected_df = numerical_df[[x_selected, y_selected]]
        corr = selected_df.corr()  # Compute correlation matrix
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap for Numerical Features")
        plt.xticks(rotation=45)
        plt.show()

    def count_plot(self, x_axis):
        """
        Creates a count plot to show the distribution of categories in a specified column.

         Parameters
         ----------
             x_axis: Column name for x_axis (Categorical)

        Example
        -------
            DataVisualization(cleaned_data).count_plot("TRANSMISSION")

        """
        categorical_cols = self.dataset.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        assert (
            x_axis in categorical_cols
        ), f"Error: {x_axis} is not a Categorical column"

        plt.figure(figsize=(6, 8))
        sns.countplot(
            x=x_axis,
            data=self.dataset,
            order=self.dataset[x_axis]
            .astype("category")
            .value_counts()
            .index,  # Sort bars by count
        )
        plt.xlabel(x_axis)
        plt.ylabel("Count")
        plt.title(f"Distribution of {x_axis} ")
        plt.xticks(rotation=45)
        plt.show()
