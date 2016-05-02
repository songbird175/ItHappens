from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
        list1.append(float(col_value))
    return list1

fig = plt.figure() # creates a matplotlib figure

ax = fig.add_subplot(211)
ax.set_title("Click to zoom")
my_map = Basemap(projection='merc', 
                 lat_0=50,
                 lon_0=-100,
                 resolution = 'l', 
                 area_thresh = 100000.0,
                 llcrnrlon=-125,
                 llcrnrlat=24,
                 urcrnrlon=-67, 
                 urcrnrlat=50)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawmapboundary()
my_map.drawstates()

plt.ion

# ZOOM MAP

# fig2 = plt.figure()
# ax = fig.add_subplot(212)
# ax.set_title("Click above to zoom") 
# zoom_map = Basemap(projection='mill',
#                  lat_0=50,
#                  lon_0=-100,
#                  area_thresh = 10000.0,
#                  llcrnrlon=-125,
#                  llcrnrlat=24,
#                  urcrnrlon=-67, 
#                  urcrnrlat=50,
#                  resolution = 'c')

# zoom_map.drawmapboundary()


def in_box(event):
    if event.x >= 80 and event.y <= 200:
        print "x=%d, y=%d"%(event.x, event.y)
    else:
        print "x=%d, y=%d w=%d"%(event.x, event.y, 0)

def on_click(event):
    fig.clf()
    print "CLICKED"
    if event.button != 1:
        return
    
    plt.subplot(2,1,1)

    ax = fig.add_subplot(211)
    ax.set_title("Click to zoom")
    my_map = Basemap(projection='merc', 
                     lat_0=50,
                     lon_0=-100,
                     resolution = 'l', 
                     area_thresh = 100000.0,
                     llcrnrlon=-125,
                     llcrnrlat=24,
                     urcrnrlon=-67, 
                     urcrnrlat=50)
    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.drawmapboundary()
    my_map.drawstates()

    x, y = float(event.xdata), float(event.ydata)
    print x, y
    lon = 0
    lat = 0
    lon, lat = my_map(x,y,inverse=True)

    plt.ion

    ax = fig.add_subplot(212)
    ax.set_title("Zoom Map") 
    zoom_map = Basemap(projection='merc',
                     lat_0=50,
                     lon_0=-100,
                     area_thresh = 10000.0,
                     llcrnrlat=lat-1.5,
                     llcrnrlon=lon-2.75,
                     urcrnrlat=lat+1.5,
                     urcrnrlon=lon+2.75,
                     resolution='i')
    zoom_map.drawcoastlines()
    zoom_map.drawcountries()
    zoom_map.drawmapboundary()
    zoom_map.drawstates()

    fig.canvas.draw()

def dots(self):
    # olin, university of rhode island,bard,northeastern,risd,nyu,tufts
        size = [350, 6694, 6309, 27728, 8000, 20000, 5000]
        lats = [42.293167,41.485338,42.020389,42.339806,41.825842,40.730104,42.407484]
        lons = [-71.265859,-71.531236,-73.912248,-71.091365,-71.40993,-74.002028,-71.121217]
        x,y = self.m(lons, lats)
        for i in range(len(size)):
            if size[i] <= 5000:
                self.m.plot(x[i], y[i], 'go', markersize=size[i]/1000)
            elif size[i] >= 10000:
                self.m.plot(x[i], y[i], 'ro', markersize=size[i]/1000)
            else:
                self.m.plot(x[i], y[i], 'bo', markersize=size[i]/1000)
        plt.show()

cid_up = fig.canvas.mpl_connect('button_press_event', in_box)
fig.canvas.mpl_connect('button_press_event',on_click)

plt.show()


# fig, axes = plt.subplots(nrows=2, ncols=1)


# def on_click(event):
#     print "CLICKED"

#     x2 = np.linspace(0.0, 2.0)
#     y2 = np.linspace(2 * np.pi * x2)
#     plt.subplot(2,1,2)
#     plt.plot(x2, y2, 'r.-')
#     plt.xlabel('time (s)')
#     plt.ylabel('Undamped')

#     fig.canvas.draw()

# fig.canvas.mpl_connect('button_press_event',on_click)
# plt.show