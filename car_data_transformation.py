import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_cleaned = {}  # Create an empty dictionary to store cleaned DataFrames

data = pd.read_csv('2015.csv')
data_cleaned['2015'] = data

year = 2016
while year <= 2024:
    year_str = str(year)
    
    # Read the Excel file into a DataFrame
    data = pd.read_excel(f'{year_str}.xlsx')
    
    # Clean the DataFrame by selecting specific columns and renaming them
    data_cleaned[year_str] = data[['Model Year', 'Mfr Name', 'Division', 'Carline', 'Eng Displ', '# Cyl', 'Transmission',
                                   'City FE (Guide) - Conventional Fuel', 'Hwy FE (Guide) - Conventional Fuel',
                                   'Comb FE (Guide) - Conventional Fuel', 'Air Aspiration Method Desc',
                                   'Trans Desc', '# Gears', 'Drive Desc', 'Carline Class Desc', 'Release Date',
                                   'City CO2 Rounded Adjusted', 'Hwy CO2 Rounded Adjusted',
                                   'Comb CO2 Rounded Adjusted (as shown on FE Label)']]
    
    data_cleaned[year_str].columns = ['Model Year', 'Mfr Name', 'Division', 'Carline', 'Engine Displacement', '# Cylinders',
                                      'Transmission', 'City FE', 'Highway Fe', 'Combined FE',
                                      'Air Aspiration Method', 'Transmission Description', '# Gears',
                                      'Drive Desc', 'Carline Class Desc', 'Release Date', 'City CO2',
                                      'Highway CO2', 'Combined CO2']
    
    year += 1

#print(data_cleaned)
data_cleaned_list = list(data_cleaned.values())
all_years = pd.concat(data_cleaned_list, ignore_index=True)

all_years.to_csv('all_years.csv', index = False)

# Now, you have a dictionary 'data_cleaned' containing cleaned DataFrames for each year from 2016 to 2024.