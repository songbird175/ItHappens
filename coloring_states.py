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

# ax = fig.add_subplot(211)
# ax.set_title("Normal Map")
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
    

number = [0, 2, 1, 1, 0, 1, 4, 5, 0, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 2, 0, 0, 9, 8, 7, 6, 2, 1, 4, 3, 0, 4, 5, 0, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
names = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
         'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho', 
         'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
         'Maine', 'Maryland','Massachusetts','Michigan','Minnesota',
         'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
         'New Hampshire','New Jersey','New Mexico','New York',
         'North Carolina','North Dakota','Ohio',    
         'Oklahoma','Oregon','Pennsylvania','Rhode Island',
         'South Carolina','South Dakota','Tennessee','Texas','Utah',
         'Vermont','Virginia','Washington','West Virginia',
         'Wisconsin','Wyoming']

for i in range(len(number)):
    if number[i] == 0:
        seg = my_map.states[state_names.index(names[i])]
        edge = [0, 0, 0]
        poly = Polygon(seg, facecolor=edge,edgecolor=edge)
        ax.add_patch(poly)
    elif number[i] <= 2:
        seg = my_map.states[state_names.index(names[i])]
        edge = [.3, .3, .3]
        poly = Polygon(seg, facecolor=edge,edgecolor=edge)
        ax.add_patch(poly)
    elif number[i] <= 4:
        seg = my_map.states[state_names.index(names[i])]
        edge = [.6, .6, .6]
        poly = Polygon(seg, facecolor=edge,edgecolor=edge)
        ax.add_patch(poly)
    else:
        seg = my_map.states[state_names.index(names[i])]
        edge = [1, 1, 1]
        poly = Polygon(seg, facecolor=edge,edgecolor=edge)
        ax.add_patch(poly)

ax = plt.gca() # get current axes instance

plt.show()
