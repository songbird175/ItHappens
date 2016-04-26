# a program that uses the csv from the cleaning_data code
# and maps data based on the size of the college and the 
# percent of cases (number of cases/college size)

import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.patches import Polygon
from matplotlib.pyplot import figure, show
from matplotlib.patches import Rectangle

def panda_to_list(file_name, title1):
    """
    The opens a saved csv file and convert it to a panda file. The 
    panda file is separated into columns and the columns are made into
    lists. The lists are the output of the funciton. 
    """
    datafile = pd.read_csv(file_name) #opens a data file

    # puts the data in a column
    for col in datafile.columns:
        datafile[col] = datafile[col].astype(str)
    column1 = datafile[title1]

    # creates a list from column data in the csv
    list1 = [] 
    for col_value in column1:
        list1.append(float(col_value))
    return list1

fig = plt.figure() # creates a matplotlib figure

ax = fig.add_subplot(211)
ax.set_title("Normal Map")
my_map = Basemap(projection='merc', 
                 lat_0=50,
                 lon_0=-100,
                 resolution = 'l', 
                 area_thresh = 1000.0,
                 llcrnrlon=-125,
                 llcrnrlat=24,
                 urcrnrlon=-67, 
                 urcrnrlat=50)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawmapboundary()
my_map.drawstates()

# a shapfile containing the states (for later use)
my_map.readshapefile('st99_d00', name='states', drawbounds=True)

# creates a list containing the name of each state
state_names = []
for shape_dict in my_map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca()

# # changes the color of texas to red
# seg = my_map.states[state_names.index('Texas')]
# poly = Polygon(seg, facecolor='red',edgecolor='red')
# ax.add_patch(poly)

ax = plt.gca() # get current axes instance

def point_in_polygon(pt, polygon):
    """Returns True iff `pt` is inside `polygon`.
    `polygon` is a list of tuples `(x, y)`."""
    # not used currently
    return matplotlib.path.Path(polygon).contains_point(pt)

def OnClick(event):
    """prints the x and y position of the mouse
    when a location is clicked on the map.
    """
    print "x=%d, y=%d"%(event.x, event.y)


# data from csv
lons = panda_to_list('output2.csv', 'lons')
lats = panda_to_list('output2.csv', 'lats')
size = panda_to_list('output2.csv', 'size')
number = panda_to_list('output2.csv', 'case')
percent_list = panda_to_list('output2.csv', 'perc')

# uses the lons and lats data to define x and y on the map
x, y = my_map(lons, lats)

# creates a size and color distinction, where the size
# of the school is proportional to the size of the dot
# and the color of the dot indicates the percentage of cases
for i in range(len(number)):
    if percent_list[i] == 0:
        my_map.plot(x[i], y[i], 'go', markersize=size[i]/1500)
    elif percent_list[i] >= 5:
        my_map.plot(x[i], y[i], 'bo', markersize=size[i]/1500)
    else:
        my_map.plot(x[i], y[i], 'go', markersize=size[i]/1500)

cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)



# ZOOM MAP

# fig2 = plt.figure()
ax = fig.add_subplot(212)
ax.set_title("Zoom Map - Massachusetts") 
zoom_map = Basemap(projection='merc',
                 llcrnrlat=40,
                 llcrnrlon=-75,
                 urcrnrlat=43,
                 urcrnrlon=-69.5,
                 resolution='l')
zoom_map.drawcoastlines()
zoom_map.drawcountries()
zoom_map.drawmapboundary()
zoom_map.drawstates()

x1, y1 = zoom_map(lons, lats)

for i in range(len(percent_list)):
    if percent_list[i] <= 1:
        zoom_map.plot(x1[i], y1[i], 'ro', markersize=size[i]/1500)
    elif percent_list[i] >= 5:
        zoom_map.plot(x1[i], y1[i], 'ro', markersize=size[i]/1500)
    else:
        zoom_map.plot(x1[i], y1[i], 'ro', markersize=size[i]/1500)

plt.show()


