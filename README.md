# fuel_consumption_analysis

[![PyPI - Version](https://img.shields.io/pypi/v/fuel-consumption-analysis.svg)](https://pypi.org/project/fuel-consumption-analysis)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fuel-consumption-analysis.svg)](https://pypi.org/project/fuel-consumption-analysis)

-----

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview
The `fuel_consumption_analysis` package provides tools for **data analysis** and **visualization** of the FuelConsumption dataset.
This package focuses on three critical aspects:

1. **Data Cleaning:**
   - Data cleaning is the process of identifying and correcting errors and missing values in datasets.
   - It ensures the dataset is accurate, reliable, and suitable for analysis.
   - It improves data quality and consistency and ensures datasets are complete and structured properly.
     
2. **Data Analysis:**  
   - Data analysis is a process of discovering useful information, concluding, and making decisions based on data.
   - It uses statistical and computational techniques.
      
3. **Data Visualization:**
   - Data visualization is the process of representing data visually through charts, plots, graphs, and other graphical formats to make it easier to understand and    analyze.
   - Effective visualization makes complex data more accessible, understandable, and actionable.

## Installation
1. Clone the Repository
   ```console
   git clone https://github.com/Masoumeh-Davoudi/fuel-consumption-analysis.git
   cd fuel-consumption-analysis
   ```
2. Set up a Virtual Environment     
   Create and Activate a Conda environment:
   
   ```console
   conda create --name fuel_env python=3.10 -y
   conda activate fuel_env
   ```
4. Install the Required Dependancies      
   Ensure the Required Packages are Installed:
   
   ```console
   pip install numpy pandas matplotlib seaborn
   ```
5. Install the Package
   ```console
   python -m pip install -e .
   ```
## Usage 
After the Installation, you can import the package modules:
```python
from fuel_consumption_analysis.data_cleaning import DataCleaning
from fuel_consumption_analysis.data_analysis import DataAnalysis
from fuel_consumption_analysis.data_visualization import DataVisualization
```
### DataCleaning Module
1. **`Handling whitespace:`** Removes leading and trailing whitespaces from string columns.
2. **`Finding missing values:`** Finds the missing value count in the dataset.
3. **`Handling missing values:`** Replaces missing values in the datasets.
4. **`Finding duplicate rows:`** Finds the duplicate rows in the dataset.
5. **`Removing duplicate rows:`** Removes duplicate rows from the datasets.

**Example:**  
**`missing_values():`**  
   Finds the missing value count in the dataset.
     
   ```console
   print(DataCleaning(data).missing_values())
   ```   


### DataAnalysis Module
1. **`Descriptive statistics:`** Computes descriptive statistics(mean, median, SD, etc.).
2. **`Categorical variable description:`** Counts the values in each categories for object columns in a DataFrame.
3. **`Correlation matrix visualization:`** Computes and visualize the correlation matrix for numerical features.

**Ecample:**  
**`categorical_description():`**  
    Counts the values in each categories for object columns in a DataFrame.

   ```console
    print(DataAnalysis(data).categorical_description())
   ```

### DataVisualization Module
1. **`Scatter Plot:`** Creates a scatter plots to visualize the relationship between two numerical features.
2. **`Bar Plot:`** Creates a bar plot to compare categories against a numerical variable.
3. **`Box Plot:`** Creates a box plot to show the distribution of a numerical variable across categorical variable.
4. **`Hist Plot:`** Creates a histogram to show the distribution of a numerical variables.
5. **`Heat Map Plot:`** Creates a heatmap to visualize the correlation matrix of  the numerical variables.
6. **`Count Plot:`** Creates a count plot to show the distribution of categories in a specified column.

**Ecample:**    
**`scatter_plot():`**    
   Creates a scatter plots to visualize the relationship between two numerical features.

   ```console
   DataVisualization(data).scatter_plot("ENGINE SIZE", "FUEL CONSUMPTION", "MAKE")
   ```

## License

`fuel-consumption-analysis` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
