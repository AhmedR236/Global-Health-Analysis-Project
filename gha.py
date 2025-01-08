import pandas as pd
import matplotlib.pyplot as plt



#Loading the dataset
df = pd.read_csv("Global Health Statistics.csv")

#Viewing first 5 rows
#print(df.head())

#Check Types
#print(df.info())

#Basic Stats
#print(df.describe())

# (Cleaning Data) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Checks For Null Values Within The DataSet
#print(df.isnull().sum())

#Checking For Dups
df = df.drop_duplicates()

# Look For Outliers {Prevalence Rate} - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
prev_col = ['Prevalence Rate (%)']

for col in prev_col:
    plt.figure(figsize = (8, 4))
    plt.hist(df[col], bins = 30, edgecolor = 'k')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()


# Analyze Global Disease Prevalence Trends - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
setdata = df.groupby(['Year', 'Disease Name'])['Prevalence Rate (%)'].mean().reset_index()

# Plotting disease prevalence trends for selected diseases
selected_diseases = ['Malaria', 'HIV', 'COVID-19']  

plt.figure(figsize = (12, 6))

for disease in selected_diseases:
    subset = setdata[setdata['Disease Name'] == disease]
    plt.plot(subset['Year'], subset['Prevalence Rate (%)'], label=disease)

plt.title('Global Disease Prevalence Trends')
plt.xlabel('Year')
plt.ylabel('Prevalence Rate (%)')
plt.legend(title='Disease Name')
plt.grid(True)
plt.show()

#Identify the top-performing countries in terms of healthcare recovery rates - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
top_countries = df.groupby(['Country'])['Recovery Rate (%)'].mean().nlargest(10)

plt.figure(figsize = (10,6))

top_countries.plot(kind ='bar', color ='skyblue', edgecolor ='k')

plt.title('Top 10 Countries by Recovery Rate')
plt.xlabel('Country')
plt.ylabel('Average Recovery Rate (%)')
plt.xticks(rotation = 45)
plt.grid(axis = 'y')
plt.show()

#Healthcare Access vs Recovery Rate - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

plt.figure(figsize = (10, 6))
plt.scatter(df['Healthcare Access (%)'], df['Recovery Rate (%)'], alpha = 0.5, edgecolors = 'k')
plt.title('Correlation Between Healthcare Access and Recovery Rate')
plt.xlabel('Healthcare Access (%)')
plt.ylabel('Recovery Rate (%)')
plt.grid(True)
plt.show()

#Per Capita Income vs Mortality Rate - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

plt.figure(figsize = (10,6))
plt.scatter(df['Per Capita Income (USD)'], df['Mortality Rate (%)'], alpha = 0.5, edgecolors = 'k')
plt.title('Correlation Between Per Capita Income and Mortality Rate')
plt.xlabel('Per Capita Income (USD)')
plt.ylabel('Mortality Rate (%)')
plt.grid(True)
plt.show()


#Education Index vs Recovery Rate - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
plt.figure(figsize = (10, 6))
plt.scatter(df['Education Index'], df['Recovery Rate (%)'], alpha = 0.5, edgecolors = 'k')
plt.title('Education Index vs Recovery Rate')
plt.xlabel('Education Index')
plt.ylabel('Recovery Rate (%)')
plt.grid(True)
plt.show()

df.to_csv('global_health_cleaned.csv', index=False)