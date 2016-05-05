import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.patches import Polygon
from matplotlib.pyplot import figure, show
from matplotlib.patches import Rectangle
from pylab import *
import sys

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
    """
    The map of points for colleges that reported zero cases
    versus colleges that reported a number greater than zero
    """
    def __init__(self):
        """initializes characteristics of the map"""

        self.fig = plt.figure() # creates a figure
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
        plt.ion() # allows for interaction
  
        # calls on CSV files for coordinate and case data
        # file1 = 'private_oncampus_nonforcible_forcible.csv'
        # file1 = 'private_non_nonforcible_forcible.csv'
        # file1 = 'private_public_nonforcible_forcible.csv'

        # file1 = 'public_oncampus_nonforcible_forcible.csv'
        # file1 = 'public_non_nonforcible_forcible.csv'
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

    def on_click(event):
        """ prints the x, y coordinates when the mouse is clicked"""
        print "x=%d, y=%d"%(event.x, event.y)

    def run(self):
        """runs the program"""
        while True:
            plt.pause(0.1)


class Shaded_States(object):
    """creates the map of shaded states"""
    def __init__(self):
        """initializes characteristics of the map"""""

        self.fig2 = plt.figure() # creates a figure
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
        plt.ion() # allows for interaction

        # a shapefile of the states in the U.S.
        self.my_map.readshapefile('st99_d00', name='states', drawbounds=True)

        # creates a list of state names
        state_names = []
        for shape_dict in self.my_map.states_info:
            state_names.append(shape_dict['NAME'])
        print state_names

        # data
        names = ['New Jersey', 'New York', 'Virginia', 'Vermont', 
        'North Carolina', 'Hawaii', 'California', 'Maryland', 'Wisconsin', 
        'Georgia', 'West Virginia', 'Massachusetts', 'Missouri', 'Louisiana', 
        'Indiana', 'Connecticut', 'Pennsylvania', 'Delaware', 'Wyoming', 'Alabama', 
        'Florida', 'Rhode Island', 'Mississippi', 'Illinois', 'Maine', 'Iowa', 
        'Kentucky', 'Oregon', 'Texas', 'Idaho', 'Minnesota', 'Tennessee', 'Ohio', 
        'Washington', 'Utah', 'Nevada', 'New Hampshire', 'Arizona', 
        'South Carolina', 'Kansas', 'Montana', 'Nebraska', 'North Dakota', 'Colorado', 
        'Oklahoma', 'Arkansas', 'New Mexico', 'Michigan', 'South Dakota', 'Alaska'] 

        number  = [11.7, 14.6, 17.7, 19.3, 20.3, 20.5, 20.6, 21, 21.3, 21.4, 22.7, 24.7, 25.1, 25.2, 25.5, 25.6, 26.1, 26.5, 26.7, 26.9, 27.2, 27.4, 27.5, 27.7, 28, 28.3, 29, 29.2, 29.6, 30, 30.5, 31.5, 31.7, 31.8, 33, 33.7, 34, 34.7, 35.5, 36.5, 37.7, 38.3, 38.9, 40.7, 41.6, 42.3, 45.9, 46.4, 70.2, 79.7]

        ax = plt.gca()

        # creates different state colors based on the number of cases
        for i in range(len(number)):
            if number[i] <= 25:
                seg = self.my_map.states[state_names.index(names[i])]
                edge = [1, 1, 1]
                poly = Polygon(seg, facecolor=edge,edgecolor=edge)
                ax.add_patch(poly)
            elif number[i] <= 35:
                seg = self.my_map.states[state_names.index(names[i])]
                edge = [.6, .6, .6]
                poly = Polygon(seg, facecolor=edge,edgecolor=edge)
                ax.add_patch(poly)
            elif number[i] <= 45:
                seg = self.my_map.states[state_names.index(names[i])]
                edge = [.3, .3, .3]
                poly = Polygon(seg, facecolor=edge,edgecolor=edge)
                ax.add_patch(poly)
            else:
                seg = self.my_map.states[state_names.index(names[i])]
                edge = [0, 0, 0]
                poly = Polygon(seg, facecolor=edge,edgecolor=edge)
                ax.add_patch(poly)

        plt.show()

    def run(self):
        """ runs the program """
        while True:
            plt.pause(0.1)


if __name__ == '__main__':
    cm = Normal_Map()
    # cm = Shaded_States()
    cm.run()
    