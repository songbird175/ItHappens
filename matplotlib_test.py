from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np 
import usa_map
import pandas as pd
import random
from matplotlib.patches import Polygon
from matplotlib.pyplot import figure, show


fig_zoom = plt.figure()
fig = plt.figure()

zoom_map = Basemap(projection='merc', lat_0=50, lon_0=-100, resolution = 'l', area_thresh = 1000.0,llcrnrlon=-125, llcrnrlat=24, urcrnrlon=-67, urcrnrlat=50)
zoom_map.drawcoastlines()
zoom_map.drawcountries()
zoom_map.drawmapboundary()
zoom_map.drawstates()

my_map = Basemap(projection='merc', lat_0=50, lon_0=-100, resolution = 'l', area_thresh = 1000.0,llcrnrlon=-125, llcrnrlat=24, urcrnrlon=-67, urcrnrlat=50)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawmapboundary()
my_map.drawstates()

plt.ion

my_map.readshapefile('st99_d00', name='states', drawbounds=True)

state_names = []
for shape_dict in my_map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca()

seg = my_map.states[state_names.index('Texas')]
poly = Polygon(seg, facecolor='red',edgecolor='red')
ax.add_patch(poly)

ax = plt.gca() # get current axes instance
print ax


def remap_interval(val, input_start, input_end, output_start, output_end):
    """
    takes an input interval, a value in the input interval and returns a 
    subsequent value in the output interval 

    >>> remap_interval(5, 0, 10, 0, 20)
    10
    """
    #everything needs to be a float
    float(val)
    float(input_end)
    float(input_start)
    float(output_end)
    float(output_start)

    #everything needs to be a float
    input_space = float(input_end-input_start)
    output_space = float(output_end-output_start)
    diff = val - input_start

    #gets the value in a form that compares it to the input interval
    ratio = output_space/input_space
    newval = output_start + diff*ratio
    return int(newval)


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
        # my_map = Basemap(projection='merc', lat_0=30, lon_0=-100, resolution = 'l', area_thresh = 1000.0,llcrnrlon=-125, llcrnrlat=24, urcrnrlon=-67, urcrnrlat=50)
        # plt.axis([event.x-.5, event.x+.5, event.y-.5, event.y+.5])


def onpress(event):
    if event.button != 1:
        return
    x, y = event.x, event.y
    axzoom.set_xlim(x - 0.5, x + 0.5)
    axzoom.set_ylim(y - 0.5, y + 0.5)
    zoom_map.plot(markersize=5)

cid_up = fig.canvas.mpl_connect('button_press_event', in_box)
zoom1 = fig_zoom.canvas.mpl_connect('button_press_event', onpress)

#olin, harvard, cmu,washu,ucdavis,plymouth state,maine orno,bradley university
#unh,university of rhode island, u of dayton,u of wisconsin whitewater
#u of wisconsin green bay,westfield state,u of redlands,suny plattsburgh
#stanford,emory,northern michigan u,csu monterey bay,yale,brown,u of rochester,
#ramapo college,vanderbilt,princeton,dartmouth

lats = [42.29, 42.37, 40.44,38.64,38.53,43.75,44.90,40.70,
        43.13,42.40,41.48,39.74,42.83,
        44.53,42.13,34.06,44.69,
        37.42,33.79,46.55,36.65,41.31,41.82,43.13,
        41.08,36.14,40.34,43.70]
lons = [-71.26, -71.11, -79.94,-90.31,-121.76,-71.69,-68.67,-89.61,
        -70.93,-71.12,-71.53,-84.18,-88.74,
        -87.92,-72.79,-117.16,-73.46,
        -122.17,-84.32,-87.40,-121.81,-72.92,-71.40,-77.62,
        -74.1768,-86.80,-74.74,-72.29]

x,y = my_map(lons, lats)

my_map.plot(x, y, 'bo', markersize=5)
plt.show()

