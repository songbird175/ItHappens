# a program that uses the csv from the cleaning_data code
# and maps data based on the size of the college and the 
# percent of cases (number of cases/college size)

import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.patches import Polygon
from matplotlib.pyplot import figure, show

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
        list1.append(col_value)
    return list1


def non_zero_sorting(file1, return_what):
    """
    returns a list of information about the college. This program is meannt to 
    separate the colleges by the number they reported (either zero, 'nan', or nonzero).
    """
    # the data converted to a list
    name = panda_to_list(file1, 'name')
    size = panda_to_list(file1, 'size')
    unsorted_list = panda_to_list(file1, 'case')
    lats = panda_to_list(file1, 'lats')
    lons = panda_to_list(file1, 'lons')

    # initialize empty lists for nonzero numbers
    nonzero_college = []
    nonzero_size = []
    nonzero_num = []
    nonzero_lats = []
    nonzero_lons = []

    # initialize empty lists for zero numbers
    zero_college = []
    zero_size = []
    zero_num = []
    zero_lats = []
    zero_lons = []

    # separates the unsorted list according to zero versus nonzero
    for i in range(len(unsorted_list)):
        if unsorted_list[i] == '0.0' or unsorted_list[i] == 'nan':
            zero_college.append(name[i])
            zero_size.append(float(size[i]))
            zero_num.append(0)
            zero_lats.append(float(lats[i]))
            zero_lons.append(float(lons[i]))
        else:
            nonzero_college.append(name[i])
            nonzero_size.append(float(size[i]))
            nonzero_num.append(float(unsorted_list[i]))
            nonzero_lats.append(float(lats[i]))
            nonzero_lons.append(float(lons[i]))
    if return_what == 'nonzero':
        return [nonzero_college, nonzero_size, nonzero_num, nonzero_lons, nonzero_lats]
    else:
        return [zero_college, zero_size, zero_num, zero_lons, zero_lats]

fig = plt.figure() # creates a matplotlib figure

# the specifications for the size and type of map
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

# nonzero or zero
# [nonzero_college, nonzero_size, nonzero_num, nonzero_lons, nonzero_lats]
info = non_zero_sorting('output2.csv', 'nonzero')
lons = info[3]
lats = info[4]
size = info[1]
number = info[2]
percent_list = []

# creates the percent list
for i in range(len(size)):
    try:
        percentage = (number[i]/size[i])*10000
        percent_list.append(percentage)
    except:
        percent_list.append(0.0)

# uses the lons and lats data to define x and y on the map
x,y = my_map(lons, lats)

# creates a size and color distinction, where the size
# of the school is proportional to the size of the dot
# and the color of the dot indicates the percentage of cases
for i in range(len(percent_list)):
    if percent_list[i] <= 1:
        my_map.plot(x[i], y[i], 'go', markersize=size[i]/1500)
    elif percent_list[i] >= 5:
        my_map.plot(x[i], y[i], 'ro', markersize=size[i]/1500)
    else:
        my_map.plot(x[i], y[i], 'bo', markersize=size[i]/1500)

# calls the function that displays the x,y of the mouse click
cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)

plt.show()

