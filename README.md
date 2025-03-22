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
It helps explore fuel efficiency, CO₂ emissions, and other vehicle-related insights.

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
## DataCleaning Module
1. **`Handling whitespace:`**  Removes leading and trailing whitespaces from string columns.

2. **`Finding missing values:`**  Finds the missing value count in the dataset.

3. **`Handling missing values:`**  Replaces missing values in the datasets.
4. **`Finding duplicate rows:`**  Finds the duplicate rows in the dataset.

5. **`Removing duplicate rows:`**  Removes duplicate rows from the datasets.

## DataAnalysis Module
1. **`Descriptive statistics:`**   Computes descriptive statistics(mean, median, SD, etc.).
2. **`Categorical variable description:`**  Counts the values in each categories for object columns in a DataFrame.
3. **`Correlation matrix visualization:`**  Computes and visualize the correlation matrix for numerical features.
   


## License

`fuel-consumption-analysis` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
