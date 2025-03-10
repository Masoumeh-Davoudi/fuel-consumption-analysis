# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 22:15:16 2025

@author: Masoumeh
"""
import seaborn as sns
import matplotlib.pyplot as plt


class DataVisualization:

    def __init__(self, dataset):

        self.dataset = dataset

    def scatterPlot(self, x_axis, y_axis, category=None):
        plt.figure(figsize=(8, 8))
        sns.scatterplot(x=x_axis, y=y_axis, hue=category, data=self.dataset)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Scattor Plot: {x_axis} vs {y_axis}")
        plt.show()

    def enter_fitures_and_plot(self):

        print("Available columns:", self.dataset.columns.tolist())
        x_selected = input("Enter column name for X-axis: ")
        y_selected = input("Enter column name for Y-axis: ")

        if (
            x_selected not in self.dataset.columns
            or y_selected not in self.dataset.columns
        ):
            print(
                "Error: Column names are incorrect. Please select from the provided list."
            )
            return

        self.scatterPlot(x_selected, y_selected)
