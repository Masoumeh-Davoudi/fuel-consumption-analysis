# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 22:15:16 2025

@author: Masoumeh
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd


class DataVisualization:

    def __init__(self, dataset):
        self.dataset = dataset
        self.dataset.columns = self.dataset.columns.str.replace(
            " ", "_"
        ).str.upper()
        self.switch_case = {
            "scatterplot": self.scatter_plot,
            "lineplot": self.line_plot,
            "barplot": self.bar_plot,
            "boxplot": self.box_plot,
            "histplot": self.histogram_plot,
            "heatmap": self.heat_map_plot,
        }

        self.categorical_cols = [
            "YEAR",
            "MAKE",
            "MODEL",
            "VEHICLE_CLASS",
            "TRANSMISSION",
            "FUEL",
        ]
        self.numerical_cols = [
            "ENGINE_SIZE",
            "CYLINDERS",
            "FUEL_CONSUMPTION",
            "COEMISSIONS",
        ]

    def scatter_plot(self, x_axis, y_axis):
        if not np.issubdtype(
            self.dataset[x_axis].dtype, np.number
        ) or not np.issubdtype(self.dataset[y_axis].dtype, np.number):
            print(
                f"Error: Scatter plots require numerical columns. '{x_axis}' or '{y_axis}' is not numerical."
            )
            return
        plt.figure(figsize=(8, 8))
        hue_column = "MAKE" if "MAKE" in self.dataset.columns else None
        sns.scatterplot(x=x_axis, y=y_axis, hue=hue_column, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Scatter Plot: {x_axis} vs {y_axis}")
        plt.show()

    def line_plot(self, x_axis, y_axis):
        if not np.issubdtype(
            self.dataset[x_axis].dtype, np.number
        ) or not np.issubdtype(self.dataset[y_axis].dtype, np.number):
            print(
                f"Error: Line plots require numerical columns. '{x_axis}' or '{y_axis}' is not numerical."
            )
            return
        plt.figure(figsize=(8, 8))
        hue_column = "MAKE" if "MAKE" in self.dataset.columns else None
        sns.lineplot(x=x_axis, y=y_axis, hue=hue_column, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Line Plot: {x_axis} vs {y_axis}")
        plt.show()

    def bar_plot(self, x_axis, y_axis):
        if np.issubdtype(self.dataset[x_axis].dtype, np.number):
            print(
                f"Error: Bar plots require a categorical x-axis. '{x_axis}' is not categorical."
            )
            return

        if not np.issubdtype(self.dataset[y_axis].dtype, np.number):
            print(
                f"Error: Bar plots require a numerical y-axis. '{y_axis}' is not numerical."
            )
            return
        plt.figure(figsize=(8, 8))
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
        if np.issubdtype(self.dataset[x_axis].dtype, np.number):
            print(
                f"Error: Box plots require a categorical x-axis. '{x_axis}' is not categorical."
            )
            return

        if not np.issubdtype(self.dataset[y_axis].dtype, np.number):
            print(
                f"Error: Box plots require a numerical y-axis. '{y_axis}' is not numerical."
            )
            return
        plt.figure(figsize=(8, 8))
        sns.boxplot(x=x_axis, y=y_axis, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Box Plot: {x_axis} vs {y_axis}")
        plt.xticks(rotation=45)
        plt.show()

    def histogram_plot(self, x_axis):
        if not np.issubdtype(self.dataset[x_axis].dtype, np.number):
            print(
                f"Error: Histograms require a numerical column. '{x_axis}' is not numerical."
            )
            return
        plt.figure(figsize=(8, 8))
        sns.histplot(x=x_axis, data=self.dataset, bins=10, kde=True)
        plt.xlabel(x_axis)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {x_axis} ")
        plt.xticks(rotation=45)
        plt.show()

    def heat_map_plot(self):
        plt.figure(figsize=(8, 8))
        numerical_df = self.dataset.select_dtypes(include=[np.number])
        corr = numerical_df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap Only for Numerical Features")
        plt.xticks(rotation=45)
        plt.show()

    def plot_help_table(self):
        help_table = {
            "Plot Type": [
                "Scatter Plot",
                "Line Plot",
                "Bar Plot",
                "Box Plot",
                "Histogram",
                "Heatmap",
            ],
            "X-axis Data Type": [
                "Numerical",
                "Numerical",
                "Categorical",
                "Categorical",
                "Numerical",
                "Numerical (All)",
            ],
            "Y-axis Data Type": [
                "Numerical",
                "Numerical",
                "Numerical",
                "Numerical",
                "N/A",
                "Numerical (All)",
            ],
            "Special Considerations": [
                "Works best with numerical features",
                "Both must be continuous",
                "X must be categorical, Y must be numeric",
                "X must be categorical, Y must be numeric",
                "Only one numerical column",
                "Handles only numerical correlation",
            ],
        }

        df_help = pd.DataFrame(help_table)
        print(df_help)

    plotNames = [
        "scatterplot",
        "lineplot",
        "barplot",
        "boxplot",
        "histplot",
        "heatmap",
    ]

    def enter_fitures_and_plot(self):

        print(f"Available Plots are : {self.plotNames}, choose one to plot")

        while True:
            plotName = (
                input(
                    "Enter the name of the plot based on the provided list: "
                )
                .strip()
                .lower()
            )
            if plotName in self.switch_case:
                break
            else:
                print(
                    "Invalid plot name. Please choose from the following list: ",
                    self.plotNames,
                )

        plot_function = self.switch_case.get(plotName.lower())

        if plot_function:
            if plotName == "heatmap":
                plot_function()
                return

            self.plot_help_table()
            print("Numerical columns:", self.numerical_cols)
            print("Categorical columns:", self.categorical_cols)
            x_selected = (
                input("Enter column name for X-axis: ").strip().upper()
            )
            y_selected = (
                input("Enter column name for Y-axis: ").strip().upper()
                if plotName != "histplot"
                else None
            )

            if x_selected not in self.dataset.columns or (
                y_selected and y_selected not in self.dataset.columns
            ):
                print(
                    "Error: Column names are incorrect. Please select from the provided list."
                )
                return

            if plotName == "histplot":
                plot_function(x_selected)
            else:
                plot_function(x_selected, y_selected)
