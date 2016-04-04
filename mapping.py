from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

my_map = Basemap(projection='merc', lat_0=50, lon_0=-100, resolution = 'l', area_thresh = 1000.0,llcrnrlon=-125, llcrnrlat=24, urcrnrlon=-67, urcrnrlat=50)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawmapboundary()
my_map.drawstates()



#olin, harvard, cmu,washu,ucdavis,plymouth state,maine orno,bradley university
#unh,university of rhode island, u of dayton,u of wisconsin whitewater
#u of wisconsin green bay,westfield state,u of redlands,suny plattsburgh
#stanford,emory,northern michigan u,csu monterey bay,yale,brown,u of rochester,
#ramapo college,vanderbilt,princeton,dartmouth
size = [350, 6694, 6309, 7401, 27728, 3787, 9339, 4588, 12840,
        13589, 8529, 10971, 6668, 5590, 3779, 5565, 7019, 7829,
        8001, 6234, 5477, 6548, 6266, 5710, 6851, 5391, 4289]
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
# print x
# print type(x)
for i in range(len(size)):
	if size[i] <= 5000:
		my_map.plot(x[i], y[i], 'go', markersize=size[i]/1000)
	elif size[i] >= 10000:
		my_map.plot(x[i], y[i], 'yo', markersize=size[i]/1000)
	else:
		my_map.plot(x[i], y[i], 'bo', markersize=size[i]/1000)
plt.show()
