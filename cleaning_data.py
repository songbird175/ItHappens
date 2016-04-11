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

    for col in datafile.columns:
        datafile[col] = datafile[col].astype(str)
    column1 = datafile[title1]

    list1 = []
    for col_value in column1:
        list1.append(col_value)
    return list1

def non_zero_sorting(column_title):
    """makes two lists of tuples (nonzero number and zero numbers). Each tuple 
    includes the name of the college, the number of students and the number 
    of the case specified by 'column_title'.
    """
    name = panda_to_list('Public_public.csv', 'Institution name')
    size = panda_to_list('Public_public.csv', 'Institution Size')
    unsorted_list = panda_to_list('Public_public.csv', column_title)

    nonzero_college = []
    nonzero_size = []
    nonzero_num = []

    zero_college = []
    zero_size = []
    zero_num = []

    for i in range(len(unsorted_list)):
        if unsorted_list[i] == '0.0' or unsorted_list[i] == 'nan':
            zero_college.append(name[i])
            zero_size.append(size[i])
            zero_num.append(0)
        else:
            nonzero_college.append(name[i])
            nonzero_size.append(size[i])
            nonzero_num.append(unsorted_list[i])
    return [nonzero_college, nonzero_size, nonzero_num]
    # return [[nonzero_college, nonzero_size, nonzero_num], [zero_college, zero_size, zero_num]]



def college_coords():
    lname = panda_to_list('hd2011.csv', 'INSTNM')
    lat = panda_to_list('hd2011.csv', 'LATITUDE')
    lon = panda_to_list('hd2011.csv', 'LONGITUD')
    name = non_zero_sorting('Sex offenses - Forcible')[0]

    lons = []
    lats = []
    coords_list = []
    no_coords = []
    coords = []

    for college1 in name:
        for college2 in lname:
            if college1 == college2:
                index = lname.index(college2)
                lons.append(float(lon[index]))
                lats.append(float(lat[index]))
                # tupl3 = (college1, lat[index], lon[index])
                # coords.append(tupl3)
                # coords_list.append(college1)
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

# seg = my_map.states[state_names.index('Texas')]
# poly = Polygon(seg, facecolor='red',edgecolor='red')
# ax.add_patch(poly)

ax = plt.gca() # get current axes instance

def panda_file_to_list(file_name, title1, list1):
    """
    The opens a saved csv file and convert it to a panda file. The 
    panda file is separated into columns and the columns are made into
    lists. The lists are the output of the funciton. 
    """
    datafile = pd.read_csv(file_name) #opens a data file

    # converts the data file into columns
    for col in datafile.columns:
        datafile[col] = datafile[col].astype(str)
    column1 = datafile[title1]
    # column2 = datafile[title2].astype(float)

    # creates lists from the columns
    list1 = []
    for col_value in column1:
        list2.append(col_value)
    return list1

def point_in_polygon(pt, polygon):
    """Returns True iff `pt` is inside `polygon`.
    `polygon` is a list of tuples `(x, y)`."""
    return matplotlib.path.Path(polygon).contains_point(pt)

def OnClick(event):
    # print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        # event.button, event.x, event.y, event.xdata, event.ydata)
    # for state in my_map.drawstates:
        # mouse_in_state = any(point_in_polygon((event.x, event.y), state) for state in my_map.drawstates)
    print "x=%d, y=%d"%(event.x, event.y)

def in_box(event):
    if event.x >= 80 and event.y <= 200:
        print "x=%d, y=%d"%(event.x, event.y)
    else:
        print "x=%d, y=%d w=%d"%(event.x, event.y, 0)

info = college_coords()
lons = info[0]
lats = info[1]
size = non_zero_sorting('Sex offenses - Forcible')[1]
number = non_zero_sorting('Sex offenses - Forcible')[2]

x,y = my_map(lons, lats)

for i in range(len(lons)):
    if float(size[i]) <= 20000:
        my_map.plot(float(x[i]), float(y[i]), 'go', markersize=float(size[i])/3000)
    elif float(size[i]) >= 30000:
        my_map.plot(float(x[i]), float(y[i]), 'ro', markersize=float(size[i])/3000)
    else:
        my_map.plot(float(x[i]), float(y[i]), 'bo', markersize=float(size[i])/3000)
plt.show()

cid_up = fig.canvas.mpl_connect('button_press_event', in_box)

plt.show()

