# Global-Health-Analysis-Project

### Project Overview:

This projects provides a detailed breakdown of the steps taken to analyze the dataset Global Health Statistics.csv, from Kaggle. I used data cleaning process, and exploratory data analysis (EDA) in python. After that I transfered the cleaned dataset into excel, and created a visual dashboard on PowerBI.

Attachments:
- Python file for exploratory data analysis (EDA), and data cleaning
- PowerBi dashboard
- global_health_cleaned.csv (Cleaned dataset)


### Objectives:

- To identify trends in global disease prevalence over time
- To assess healthcare system performance by examining recovery rates and healthcare access
- To highlight top-performing countries in terms of recovery rates.

### Data:

Dataset from Kaggle: "Global Health Statistics.csv"
https://www.kaggle.com/datasets/malaiarasugraj/global-health-statistics/data  

### Tools:

-Python (Data Analysis)
-Power Bi (Data Visualization)
-Excel (Observing the dataset)

### Data Cleaning:

The dataset was imported using the panda's library in Python. Initial inspection (head() and info()) was performed to understand the data types. I handled missing values by using using isnull().sum(). However upon observation there was no missing values.
I removed duplicates by using the drop_duplicates() function to eliminate duplicate rows to ensure accuracy and avoid redundant data. I then verified numerical columns such as Prevalence Rate (%), Recovery Rate (%), and Mortality Rate (%) were correctly recognized as numerical types. The cleaned dataset was saved as global_health_cleaned.csv.

### Exploratory Data Analysis (EDA):

Analyzed the distribution of the Prevalence Rate column using the matplotlib library to identify and visualize any irregularities. However, after conducting the visualization I noticed there was consistency among the data, and there weren't any outliers. 

Trends in Global Disease Prevalence:
-Grouped data by Year and Disease Name using groupby() to calculate the mean Prevalence Rate. Plotted line charts for selected diseases. After observing the charts there was a sharp increase in the prevalence of COVID-19 around the 2020s and diseases like Malaria and HIV displayed steady trends, demonstrating ongoing global challenges.

Top 10 Countries by Recovery Rate:
- Here I was trying to identify the best-performing countries in terms of recovery rates. What I first did was use the groupby() function on the Country column and calculated the average Recovery Rate. Then I extracted the top 10 countries using largest(), and visualized the results with a bar chart. What I gathered from this is that countries like Russia, South Africa, and Germany were among the highest countries in terms of recovery rates. 

Correlations Between Key Health Variables:
- Used scatter plots to determine comparisons between Healthcare Access vs. Recovery Rate, and Per Capita Income vs. Mortality Rate.

### PowerBI:

Global Disease Prevalence Trends:
- A line chart showing trends for diseases like COVID-19, HIV, and Malaria from 2000 to 2020.

Top 10 Countries by Recovery Rate:
- A bar chart depicting countries with the highest recovery rates. 

Mortality Rate Distribution by Income:
- A scatter plot showing the relationship between Per Capita Income (USD) and Mortality Rate.

Healthcare Access vs. Recovery Rate:
- A scatter plot demonstrating the positive correlation between Healthcare Access and Recovery Rate.

Slicers:
- I added the year, country, and disease name in order to filter data and explore specific areas of interest.

KPI Cards:
-Global Average Recovery Rate (%): 74.5%
-Global Average Mortality Rate (%): 5.05%










