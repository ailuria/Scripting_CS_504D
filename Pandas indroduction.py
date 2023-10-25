
"""
Name : Ajay vardhan reddy Ailuri
Date : 10/16/2023
Title : Pandas and Data Analysis
"""


# importing pandas module for proceesing data and analyize
import pandas as pd
import matplotlib.pyplot as plt # importing matplotlib for visualizing the data


# This method is for exploring the basic data
def exploringBasicData(data):
   
    print("Displaying first few rows:")
     # by using head() method we can display first few rows so that we can understand the data.
    print(data.head())

    # checking if any values present in the data are missing so that we can be carefull about them in calculations.
    value_missing = data.isnull().sum()
    print("The values missing are:", value_missing)

    # Getting the statistics summary of the whole data so that we can sum up the what data we have got
    stats_numeric= data.describe()
    print("sttistics are are:", stats_numeric)


# method is used for the visualizing the data in a graphical manner which give easy understanding of the data
def visualizingData(data):
    # making a sales histogram
    plt.hist(data['Sale'], bins=10, edgecolor='w')
    plt.xlabel('Sale') # nameing the x axis of histogram
    plt.ylabel('Frequency') # nameing the y axis of histogram
    plt.title('Distribution of Sale') # giving the title of the histogram
    plt.show() # showing the graph that we created

    # discount vs scale scattering plot. That will give reltion ship between the discount vs sale
    plt.scatter(data['Sale'], data['Discount'])
    plt.xlabel('Sale')  # nameing the x axis of scattering plot
    plt.ylabel('Discount') # nameing the y axis of scattering plot
    plt.title('Scatter Plot: Sale vs Discount') # giving the title of the scatter plot
    plt.show() # showing the graph visually


# cleaning the data and preprocessing
def preprocessingCleaning(data):
    data['Sale'].fillna(data['Discount'].mean(), inplace=True)
    data.drop_duplicates(inplace=True)
    # according to need convert data types
    # saving the clean data set
    data.to_csv('cleaned_dataset.csv', index=False)


# (market_data.csv) is the first data set loading and using that
data_market = pd.read_csv('market_data.csv')
print("Operations for market_data:")
exploringBasicData(data_market) # calling the function to do basic data exploration
visualizingData(data_market) # calling the function to see the visual analysis of the data
preprocessingCleaning(data_market) # calling the function to clean the null values

#  (market_data_messy.csv) loading the second data set and utilizing it
data_market_messy = pd.read_csv('market_data_messy.csv')
print("diffrent operations  for  the market_data_messy:")
exploringBasicData(data_market_messy) # calling the function to do basic data exploration
visualizingData(data_market_messy)  # calling the function to see the visual analysis of the data
preprocessingCleaning(data_market_messy) # calling the function to clean the null values
