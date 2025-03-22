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
1. **`remove_whitespace():`**  
    Removes leading and trailing whitespaces from string columns.
   
   ```console
   print(DataCleaning(data).remove_whitespace())
   ```
2. **`missing_values():`**  
   Finds the missing value count in the dataset.
     
    ```console
   print(DataCleaning(data).replace_missing_values())
   ```   
3. **`replace_missing_values():`**  
   Replaces missing values in the datasets:
   + Categorical value with mode.
   + Numerical value with mean.
   <br/><br/>
    ```console
    print(DataCleaning(data).replace_missing_values())
   ```
5. **`find_duplicates():`**  
  Finds the duplicate rows in the dataset.

   ```console
    print(DataCleaning(data).find_duplicates())
   ```
6. **`remove_duplicates():`**  
   Removes duplicate rows from the datasets.
   
   ```console
   cleaned_data = DataCleaning(data).remove_duplicates()
   print(cleaned_data)
   ```
## DataAnalysis Module
1. **`statistical_description():`**   
   Computes descriptive statistics(mean, median, SD, etc.).

   ```console
    print(DataAnalysis(data).statistical_description())
   ```

2. **`categorical_description():`**  
    Counts the values in each categories for object columns in a DataFrame.

   ```console
    print(DataAnalysis(data).categorical_description())
   ```
3. **`correlation_matrix():`**  
   Computes and visualize the correlation matrix for numerical features.
   
   ```console
   DataAnalysis(data).correlation_matrix()
   ```

## License

`fuel-consumption-analysis` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
