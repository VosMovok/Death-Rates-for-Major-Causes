# Import Certain Presquites Modules
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import os

# Import CSV file from github repo to dataframe. Source "https://data.world/health/death-rates-for-major-causes"
data = pd.read_csv("https://raw.githubusercontent.com/VosMovok/Death-Rates-for-Major-Causes/main/rows.csv", skiprows=81)

# Convert df to csv file again as I don't know how to append that
df = pd.DataFrame(data)
df.to_csv('eu_terrorism_fatalities_by_year.csv', index = False, header=True)

# Create brackets for plot axes data
x = []
y = []
z = []
p = []

# Open CSV File from root folder that just imported from github repo
with open(r'eu_terrorism_fatalities_by_year.csv') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	for row in plots: # Append the desired data from the csv file
		x.append(row[0])
		y.append(float(row[1]))
		z.append(float(row[2]))
		p.append(float(row[3]))

# Adjusting fig window size as the chart doesn't fit correctly
plt.figure(figsize=(13, 5.5))

width = 0.3
bar1 = np.arange (len(x))
bar2 = [i+width for i in bar1]
bar3 = [i-width for i in bar1]

# Visualizing using bar graph
plt.bar(
	bar1,
	y,
	width,
	color = '#bc5090', # Color for the bar
	label = "Fatalities", # add label cause why not
	)  

plt.bar(
	bar2,
	z,
	width,
	color = '#003f5c', # Color for the bar
	label = "Fatalities", # add label cause why not
	)  	
	
plt.bar(
	bar3,
	p,
	width,
	color = '#ffa600', # Color for the bar
	label = "Fatalities", # add label cause why not
	) 

# Add some dot scatter and line plot
plt.plot(
    bar1, 
    y, 
    color = 'g', 
    alpha = 0.5)   

plt.plot(	
    bar2,	
    z,
    color = 'b',	
    alpha = 0.5)  

# Add labels on top of the center of each bar
#def addlabels(x,y):
#    for i in range(len(x)):
#       plt.text(i, y[i]+10, y[i], ha = 'center', size = 5)
#addlabels(x, y)

# Year data is descending, inverting the x axis.(Deprecated)
# plt.xlim(29, 0)

# Rotating the X's Ticks so the year become readable
plt.xticks(bar1+width/2, x, rotation = 30)

# Adding axes label, title for readibility
plt.xlabel('Year')
plt.ylabel('Fatalties')
plt.title('Europe Terrorism Fatalities by Year')

# Show grid to perfectionate the graph
ax = plt.gca()
ax.grid(which='major', axis='y', linestyle='--')

# Visualize the graph into the fig
plt.show()

# Delete the imported file cause it has to
file = 'eu_terrorism_fatalities_by_year.csv'
if(os.path.exists(file) and os.path.isfile(file)):
  os.remove(file)