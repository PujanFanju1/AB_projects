import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('all_years.csv')
data.loc[data['Transmission Description'] == 'Selectable Continuously Variable (e.g. CVT with paddles)', 'Transmission Description'] = 'Selectable Continuously Variable'
data.loc[data['Transmission Description'] == 'Automated Manual- Selectable (e.g. Automated Manual with paddles)', 'Transmission Description'] = 'Automated Manual- Selectable'
print(data.columns)

print(data.head(20))

carline_FE = data.groupby('Carline')['Combined FE'].mean().reset_index().sort_values(by='Combined FE', ascending=False)

print("Top 10 most efficient cars:")
print(carline_FE.head(10))
print('\n')
print("Top 10 least efficient cars:")
print(carline_FE.tail(10).sort_values(by='Combined FE', ascending=True))
print('\n')
#--------------------Avg Combined FE for all Divisions:-------------------------------

avg_FE_division = data.groupby('Division')['Combined FE'].mean().reset_index()
print(avg_FE_division.sort_values(by='Combined FE', ascending=False))
print('\n')

#----------------How many carlines does each manufacturer have?-----------------------

count_carline = data.groupby('Mfr Name')['Carline'].nunique().reset_index().sort_values(by='Carline', ascending=False)
print(count_carline)
print('\n')

#-------------------------Distribution of fuel efficiencies---------------------------

plt.hist(data['Combined FE'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Fuel Efficiency')
plt.ylabel('Frequency')
plt.title('Distribution of Fuel Efficiencies')
plt.show()

print(data['Transmission Description'].unique())

#-------------------------Pie chart of total CO2 emissions---------------------------

T_CO2 = data.groupby('Transmission Description')['Combined CO2'].sum().reset_index()

print(T_CO2)

plt.pie(T_CO2['Combined CO2'], labels=T_CO2['Transmission Description'], autopct='%1.1f%%', startangle=140)
plt.show()

#-------------------------Pie chart of total CO2 emissions---------------------------

gears = data.groupby('# Gears')['Combined FE'].mean().reset_index()
CO2 = data.groupby('# Gears')['Combined CO2'].mean().reset_index()
print(gears)

no_gears = gears['# Gears']
FE = gears['Combined FE']
CO2 = CO2['Combined CO2']

fig, ax = plt.subplots()
plt.bar(no_gears, FE)
ax.set_xlabel("Number of Gears")
ax.set_ylabel("Average Fuel Efficiency")
plt.show()

Air_asp = data.groupby('Air Aspiration Method')['Combined FE'].mean().reset_index()

aa = Air_asp['Air Aspiration Method']
fe = Air_asp['Combined FE']

fig, ax = plt.subplots()
plt.bar(aa, fe)
ax.set_xlabel("Air Aspiration Method")
ax.set_ylabel("Average Fuel Efficiency")
plt.show()

print(Air_asp)


#-------------------------------Honda FE----------------------------------------

Honda_data = data[data['Division']=='Honda']
avg_FE_year_honda = data.groupby('Model Year')['Combined FE'].mean().reset_index()

year = avg_FE_year_honda['Model Year']
avg_FE = avg_FE_year_honda['Combined FE']

fig, ax = plt.subplots()
plt.bar(year,avg_FE)
ax.set_xlabel("year")
ax.set_ylabel("avg_FE")
plt.show()

#-------------------------------ED vs FE----------------------------------------

#avg_FE_ED = data.groupby('Engine Displacement')['Combined FE'].mean().reset_index()

#ED = avg_FE_ED['Engine Displacement']
#avg_FE = avg_FE_ED['Combined FE']

fig, ax = plt.subplots()
plt.scatter(data['Engine Displacement'],data['Combined FE'])
ax.set_xlabel("Engine Displacement")
ax.set_ylabel("Fuel Efficiency")
plt.show()

#------------------------How does Transmission affect FE------------------------

avg_FE_T = data.groupby('Transmission Description')['Combined FE'].mean().reset_index().sort_values(by='Combined FE', ascending=False)

print(avg_FE_T)


T = avg_FE_T['Transmission Description']
avg_FE = avg_FE_T['Combined FE']

fig, ax = plt.subplots()
plt.bar(T,avg_FE)
ax.set_xlabel("Transmission")
ax.set_ylabel("Avg. Fuel Efficiency")
plt.xticks(rotation=90)
plt.show()

#------------------------How does FE affect CO2 emmissions------------------------

#avg_FE_CO2 = data.groupby('Combined FE')['Combined CO2'].mean().reset_index()
#FE_CO2 = data[['Combined FE','Combined CO2']]

#FE = avg_FE_ED['Engine Displacement']
#avg_FE = avg_FE_ED['Combined FE']

fig, ax = plt.subplots()
plt.scatter(data['Combined FE'],data['Combined CO2'])
ax.set_xlabel("Combined Fuel Efficiency")
ax.set_ylabel("Combined CO2 Emissions")
plt.show()

#------------------------How has FE changed over the years------------------------

Honda_data = data[data['Division']=='Bugatti']
avg_FE_year = Honda_data.groupby('Model Year')['Combined FE'].mean().reset_index()
#FE_CO2 = data[['Combined FE','Combined CO2']]

#FE = avg_FE_ED['Engine Displacement']
#avg_FE = avg_FE_ED['Combined FE']

fig, ax = plt.subplots()
plt.plot(avg_FE_year['Model Year'],avg_FE_year['Combined FE'])
ax.set_xlabel("Model Year")
ax.set_ylabel("Average Fuel Efficiency")
plt.title("Bugatti")
plt.show()







#-------------------How does Engine displacement affect the FE?----------------

pivot1 = pd.pivot_table(data, 
                        values='Combined FE', #What we are calculating.
                        index=['Engine Displacement'], #What each row represents.
                        columns = ['Mfr Name'], #columns.
                        aggfunc = np.mean)

print(pivot1)

avg_FE_year = avg_FE_year.reset_index()
#print(avg_FE_year[0])

year = avg_FE_year['Model Year']
avg_FE = avg_FE_year['Combined FE']

fig, ax = plt.subplots()
plt.bar(year,avg_FE)
ax.set_xlabel("Model Year")
ax.set_ylabel("Avg. FE")
plt.show()

#print(avg_FE_year)