#  cleaning up data

import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.patches import Polygon
from matplotlib.pyplot import figure, show

## DATA LISTS

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

def non_zero_sorting(column_title):
    """
    returns a list of information about the college. This program is meannt to 
    separate the colleges by the number they reported (either zero, 'nan', or nonzero).
    """
    # the data converted to a list
    name = panda_to_list('Public_public.csv', 'Institution name')
    size = panda_to_list('Public_public.csv', 'Institution Size')
    unsorted_list = panda_to_list('Public_public.csv', column_title)

    # initialize empty lists for nonzero numbers
    nonzero_college = []
    nonzero_size = []
    nonzero_num = []

    # initialize empty lists for zero numbers
    zero_college = []
    zero_size = []
    zero_num = []

    # separates the unsorted list according to zero versus nonzero
    for i in range(len(unsorted_list)):
        if unsorted_list[i] == '0.0' or unsorted_list[i] == 'nan':
            zero_college.append(name[i])
            zero_size.append(size[i])
            zero_num.append(0)
        else:
            nonzero_college.append(name[i])
            nonzero_size.append(size[i])
            nonzero_num.append(unsorted_list[i])
    return [nonzero_college, nonzero_size, nonzero_num, zero_college, zero_size, zero_num]

def college_coords(list1):
    """
    returns the latitude and longitude depending on the list of colleges
    determined by the variable 'list1'. 
    """
    # data containing the college name and colelge coordinates
    lname = panda_to_list('hd2011.csv', 'INSTNM')
    lat = panda_to_list('hd2011.csv', 'LATITUDE')
    lon = panda_to_list('hd2011.csv', 'LONGITUD')
    name = non_zero_sorting('Sex offenses - Forcible')[list1]

    # initializes empty lists
    lons = []
    lats = []
    coords_list = []
    no_coords = []
    coords = []

    # sorts between the two data lists by checking if
    # the names of the colleges match. If the names of the 
    # colleges match, that college has a latitude and longitude.
    # If the names of the colleges don't match, that college gets
    # added to a list of colleges we need coordinates for.
    for college1 in name:
        for college2 in lname:
            if college1 == college2:
                index = lname.index(college2)
                lons.append(float(lon[index]))
                lats.append(float(lat[index]))
                coords_list.append(college1)
        if college1 not in coords_list:
            no_coords.append(college1)
    return [lons, lats]


## BASEMAP STUFF

fig = plt.figure()

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

my_map.readshapefile('st99_d00', name='states', drawbounds=True)

state_names = []
for shape_dict in my_map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca()

# changes the color of texas to red
# seg = my_map.states[state_names.index('Texas')]
# poly = Polygon(seg, facecolor='red',edgecolor='red')
# ax.add_patch(poly)

ax = plt.gca() # get current axes instance

def point_in_polygon(pt, polygon):
    """Returns True iff `pt` is inside `polygon`.
    `polygon` is a list of tuples `(x, y)`."""
    return matplotlib.path.Path(polygon).contains_point(pt)

def OnClick(event):
    print "x=%d, y=%d"%(event.x, event.y)

# nonzero
info = college_coords(0)
lons = info[0]
lats = info[1]
size = non_zero_sorting('Sex offenses - Forcible')[1]
number = non_zero_sorting('Sex offenses - Forcible')[2]

# zero
# info = college_coords(3)
# lons = info[0]
# lats = info[1]
# size = non_zero_sorting('Sex offenses - Forcible')[4]
# number = non_zero_sorting('Sex offenses - Forcible')[5]

x,y = my_map(lons, lats)

for i in range(len(lons)):
    if float(size[i]) <= 20000:
        my_map.plot(float(x[i]), float(y[i]), 'go', markersize=float(size[i])/3000)
    elif float(size[i]) >= 30000:
        my_map.plot(float(x[i]), float(y[i]), 'ro', markersize=float(size[i])/3000)
    else:
        my_map.plot(float(x[i]), float(y[i]), 'bo', markersize=float(size[i])/3000)
plt.show()

cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)

plt.show()
