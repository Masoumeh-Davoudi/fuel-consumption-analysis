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
4. Install the Required Dependancies are Installed     
   Ensure the required packages are installed:
   
   ```console
   pip install numpy pandas matplotlib seaborn
   ```
5. Install the Package
   ```console
   python -m pip install -e .
   ```
## Usage 
After the Installation, you can import the package modules:
```console
from fuel_consumption_analysis.data_cleaning import DataCleaning.
from fuel_consumption_analysis.data_analysis import DataAnalysis.
from fuel_consumption_analysis.data_visualization import DataVisualization.
```

## License

`fuel-consumption-analysis` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
