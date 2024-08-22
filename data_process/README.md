# Software Engineer Salaries Data Processing and Visualization

---------------------------------------------------------------------------------------------------------------------------------

The **Software Engineer Salaries Data Processing and Visualization** script is a Python application designed to process and visualize salary data for software engineers. This script reads raw data from a CSV file, cleans it, extracts relevant information, and generates various plots to analyze salary distribution, company ratings, and other key metrics.

---------------------------------------------------------------------------------------------------------------------------------

## Overview

This project is a data processing and visualization tool built to provide insights into software engineer salaries. It uses Python to handle data extraction, cleaning, processing, and visualization.

---------------------------------------------------------------------------------------------------------------------------------

#### to be updated [Software Demo Video](https://youtu./xGGPXlK9Lvs)

---------------------------------------------------------------------------------------------------------------------------------

### Key Features:

- **Data Cleaning:** Handle missing values and clean raw data to prepare it for analysis.
- **Salary Distribution Analysis:** Generate visualizations to show the distribution of software engineer salaries.
- **Company Ratings Analysis:** Analyze and visualize company ratings and their correlation with salaries.
- **Export Processed Data:** Save the cleaned and processed data to a new CSV file for further analysis or reporting.

---------------------------------------------------------------------------------------------------------------------------------

### Processed Information:

- **Main Data:**
  - **Salary:** The salary of the software engineer.
  - **Company:** The company where the software engineer is employed.
  - **Location:** The location of the job.
  - **Company Rating:** The rating of the company based on employee reviews.

- **Visualizations:**
  - **Salary Distribution:** A plot showing the distribution of salaries across different companies and locations.
  - **Company Ratings vs. Salary:** A scatter plot to visualize the correlation between company ratings and salaries.
  - **Location-based Salary Analysis:** A bar chart displaying salary averages by location.

---------------------------------------------------------------------------------------------------------------------------------

## Development Environment

The Software Engineer Salaries Data Processing and Visualization script was developed using the following tools:

- **Python:** A powerful programming language for data analysis and visualization.
- **Pandas:** A data manipulation and analysis library, used to clean and process the data.
- **Matplotlib & Seaborn:** Libraries used to create visualizations of the processed data.
- **NumPy:** A fundamental package for scientific computing with Python, used for data manipulation.

---------------------------------------------------------------------------------------------------------------------------------

## Installation

To install the necessary dependencies, run the following command:

---------------------------------------------------------------------------------------------------------------------------------

## bash
`pip install pandas matplotlib seaborn numpy`

---------------------------------------------------------------------------------------------------------------------------------

## How to Run the Script
### Running the Script Locally
- Clone the project repository from GitHub to your local machine.

`git clone "repository-url"`
`cd "repository-directory"`

---------------------------------------------------------------------------------------------------------------------------------

## Install Dependencies:
Ensure all required libraries are installed using the command:
`pip install -r requirements.txt`

---------------------------------------------------------------------------------------------------------------------------------

## Run the Script:
Execute the scripts by running one by one:
`data_processing.py`

---------------------------------------------------------------------------------------------------------------------------------

## Check the Output:
The script will generate a CSV file named processed_salaries_data.csv containing all the cleaned and processed data. It will also create several visualizations saved as image files in the output directory. 

---------------------------------------------------------------------------------------------------------------------------------

## Script Workflow
- Data Cleaning:
The script first reads the raw data and handles any missing or inconsistent entries to ensure the dataset is clean.

- Data Processing:
It then processes the data, extracting relevant information such as salary, company, and location details.

- Visualization:
Various plots are generated to help visualize the data, including salary distribution, company ratings, and location-based salary analysis.

- Exporting Data:
The cleaned and processed data is saved to a new CSV file for further analysis or reporting.

---------------------------------------------------------------------------------------------------------------------------------

## Unit Testing
To ensure the reliability of the data processing functions, unit tests have been implemented using the unittest framework. These tests cover:

- Data reading and cleaning functions to validate correctness and data integrity.
- Salary extraction and processing to ensure accurate conversion and calculation.
- Visualization functions to confirm that plots are generated as expected.
- Data export functionality to verify that processed data is saved correctly.

---------------------------------------------------------------------------------------------------------------------------------

## Running the Tests
To run all the tests, execute the following command:
`python -m unittest discover` or 
`test_data_processing.py`

---------------------------------------------------------------------------------------------------------------------------------

## Future Work

While the current version of the Software Engineer Salaries Data Processing and Visualization script provides essential functionality, there are several areas for improvement and future enhancements:

- Advanced Data Analysis: Implement more advanced data analysis techniques such as regression models or clustering.
- Interactive Visualizations: Use libraries like Plotly or Bokeh to create interactive visualizations.
- Real-time Data Processing: Adapt the script to handle real-time data streaming for more dynamic analysis.
- Automated Reports: Generate automated reports in PDF or HTML format based on the processed data.

---------------------------------------------------------------------------------------------------------------------------------

## Useful Websites

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [NumPy Documentation](https://numpy.org/doc/)

---------------------------------------------------------------------------------------------------------------------------------

### License

This project is licensed under the MIT License - see the [LICENSE](/docs/LICENSE) file for details.