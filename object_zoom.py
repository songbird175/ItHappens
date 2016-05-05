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

        self.ax = self.fig.add_subplot(211)
        self.ax.set_title("Click to zoom")
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
  
        file1 = 'public_public_nonforcible_forcible.csv'

        lons = panda_to_list(file1, 'lons')
        lats = panda_to_list(file1, 'lats')
        size = panda_to_list(file1, 'size')
        number = panda_to_list(file1, 'Combined')

        # creates the x and y coordinates 
        x, y = self.get_x_y(lons, lats)

        # creates different sized dots based on number reported
        for i in range(len(number)):
            if number[i] == 0:
                self.my_map.plot(x[i], y[i], 'ko', markersize=size[i]/1100)
            else: # number[i] >= 0:
                self.my_map.plot(x[i], y[i], 'go', markersize=size[i]/1100)

        plt.show()

    def get_x_y(self, lon, lat):
        """ Returns the x, y coordinate of a given longitude and lattitude """
        return self.my_map(*np.asarray([lon, lat]))

    # def in_box(event):
    #     if event.x >= 80 and event.y <= 200:
    #         print "x=%d, y=%d"%(event.x, event.y)
    #     else:
    #         print "x=%d, y=%d w=%d"%(event.x, event.y, 0)

    def on_click(event):
        """ Returns the x, y coordinate of a given longitude 
        and lattitude """
        fig.clf()
        print "CLICKED"
        if event.button != 1:
            return
        plt.subplot(2,1,1)
        print "x=%d, y=%d"%(event.x, event.y)
        if event.button != 1:
            return
        # fx, fy = float(event.xdata), float(event.ydata)
        # print fx, fy
        # flon = 0
        # flat = 0
        # flon, flat = my_map(fx,fy,inverse=True)

        # ax = fig.add_subplot(212)
        # ax.set_title("Zoom Map") 
        # zoom_map = Basemap(projection='merc',
        #                  lat_0=50,
        #                  lon_0=-100,
        #                  area_thresh = 10000.0,
        #                  llcrnrlat=flat-1.5,
        #                  llcrnrlon=flon-2.75,
        #                  urcrnrlat=flat+1.5,
        #                  urcrnrlon=flon+2.75,
        #                  resolution='i')
        # zoom_map.drawcoastlines()
        # zoom_map.drawcountries()
        # zoom_map.drawmapboundary()
        # zoom_map.drawstates()

        # fig.canvas.draw()
        
        # plt.subplot(2,1,1)


    def run(self):
        while True:
            plt.pause(0.1)


if __name__ == '__main__':
    cm = Normal_Map()
    # cm = Shaded_States()
    cm.run()