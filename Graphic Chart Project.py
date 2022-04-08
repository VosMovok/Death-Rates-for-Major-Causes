# Import Certain Presquites Modules
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os

# Import CSV file from github repo to dataframe. Source "https://data.world/fivethirtyeight/terrorism"
data = pd.read_csv('https://query.data.world/s/hz6trlzlk3zocf43r2w5atptcc3syq', skiprows=1)

# Convert df to csv file again as I don't know how to append that
df = pd.DataFrame(data)
df.to_csv('eu_terrorism_fatalities_by_year.csv', index = False, header=True)

# Create brackets for plot axes data
x = []
y = []

# Open CSV File from root folder that just imported from github repo
with open(r'eu_terrorism_fatalities_by_year.csv') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	for row in plots: # Append the desired data from the csv file
		x.append(row[0]) 
		y.append(int(row[1]))

# Adjusting fig window size as the chart doesn't fit correctly
plt.figure(figsize=(10, 5.5))

# Visualizing using bar graph
plt.bar(
	x,
	y,	
	alpha = 0.7,
	width = 0.7, 
	color = 'r', # Color for the bar
	label = "Fatalities" # add label cause why not
	)  

# Add some dot scatter and line plot
plt.plot(
	x, 
	y, 
	marker = 'o', # Add dot scatter to the plot
	markersize = 4, # Adjusting dot size
	color = 'b', # Color for the Line
	alpha = 0.5 # Adjust alpha mask so the label become a lil bit readable
	)   

# Add labels on top of the center of each bar
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+10, y[i], ha = 'center')
addlabels(x, y)

# Year data is descending, inverting the x axis.
plt.xlim(29, 0)

# Rotating the X's Sticks so the year become readable
plt.xticks(rotation = 30)

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