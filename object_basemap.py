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


class Normal_Map(object):
    """maps"""
    def __init__(self):
        """creates the map 
        """
        self.fig = plt.figure()
        self.my_map = Basemap(projection='merc', 
                 lat_0=50,
                 lon_0=-100,
                 resolution = 'l', 
                 area_thresh = 1000.0,
                 llcrnrlon=-125,
                 llcrnrlat=24,
                 urcrnrlon=-67, 
                 urcrnrlat=50)
        self.my_map.drawcoastlines()
        self.my_map.drawcountries()
        self.my_map.drawmapboundary()
        self.my_map.drawstates()
        plt.ion()

        self.lons = panda_to_list('output2.csv', 'lons')
        self.lats = panda_to_list('output2.csv', 'lats')
        self.size = panda_to_list('output2.csv', 'size')
        self.number = panda_to_list('output2.csv', 'case')

        self.x, self.y = self.my_map(self.lons, self.lats)


    def on_click(event):
        """ Returns the x, y coordinate of a given longitude 
        and lattitude """
        print "x=%d, y=%d"%(event.x, event.y)

    def run(self):
        if len(x) == len(y):
            for i in range(len(self.number)):
                if self.number[i] == 0:
                    self.my_map.plot(self.x[i], self.y[i], 'ko', markersize=self.size[i]/1600)
                elif self.number[i] >= 1:
                    self.my_map.plot(self.x[i], self.y[i], 'bo', markersize=self.size[i]/1600)
                else:
                    self.my_map.plot(self.x[i], self.y[i], 'ro', markersize=self.size[i]/1600)

        plt.show()


if __name__ == '__main__':
    cm = Normal_Map()
    cm.__init__()
