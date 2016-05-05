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

class ZoomMap:
    def __init__(self):
        """ Creates main figure where subplots will reside """
        self.fig = plt.figure() # creates a matplotlib figure

        self.ax = self.fig.add_subplot(211) # creates main map subplot 
        self.ax.set_title("Click to zoom")
        self.my_map = Basemap(projection='merc', 
                         lat_0=50,
                         lon_0=-100,
                         resolution = 'l', 
                         area_thresh = 100000.0,
                         llcrnrlon=-125,
                         llcrnrlat=24,
                         urcrnrlon=-67, 
                         urcrnrlat=50)
        self.my_map.drawcoastlines()
        self.my_map.drawcountries()
        self.my_map.drawmapboundary()
        self.my_map.drawstates()

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
                self.my_map.plot(x[i], y[i], 'ko', markersize=size[i]/1300)
            else: # number[i] >= 0:
                self.my_map.plot(x[i], y[i], 'go', markersize=size[i]/1300)

        self.fig.canvas.draw() # draws the figure


    def in_box(self, event):
        """
        If the event values of x and y are within a reasonable range, this function prints 
        the values and a w value of zero. If they're out of range, it just prints their 
        values.
        """
        if event.x >= 80 and event.y <= 200:
            print "x=%d, y=%d"%(event.x, event.y)
        else:
            print "x=%d, y=%d w=%d"%(event.x, event.y, 0)

    def get_x_y(self, lon, lat):
        """ Returns the x, y coordinate of a given longitude and lattitude """
        return self.my_map(*np.asarray([lon, lat]))

    def on_click(self, event):
        """
        This function clears the figure completely and redraws the main map as a subplot. 
        If main map is clicked, a subplot showing a zoomed in version will pop up beneath it.
        If the main map is clicked again, it will zoom in on the newly clicked area.
        """
        self.fig.clf() # Clears the entire figure
        
        print "CLICKED"
        
        """ The function only continues if button has been pressed once """
        if event.button != 1:
            return
        
        self.ax = self.fig.add_subplot(211) # replots the large map subplot
        self.ax.set_title("Click to zoom")
        self.my_map = Basemap(projection='merc', 
                         lat_0=50,
                         lon_0=-100,
                         resolution = 'l', 
                         area_thresh = 100000.0,
                         llcrnrlon=-125,
                         llcrnrlat=24,
                         urcrnrlon=-67, 
                         urcrnrlat=50)
        self.my_map.drawcoastlines()
        self.my_map.drawcountries()
        self.my_map.drawmapboundary()
        self.my_map.drawstates()

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
                self.my_map.plot(x[i], y[i], 'ko', markersize=size[i]/1300)
            else: # number[i] >= 0:
                self.my_map.plot(x[i], y[i], 'go', markersize=size[i]/1300)


        """
        Transfers xdata and ydata from the mouseclick to longitude and latitude coordinates
        """
        # x1, y1 = float(event.xdata), float(event.ydata)
        x1, y1 = event.xdata, event.ydata
        print x1, y1
        lon1 = 0
        lat1 = 0
        lon1, lat1 = self.my_map(x1,y1,inverse=True)

        ax = self.fig.add_subplot(212) # creates a zoomed subplot using lon,lat coordinates 
        ax.set_title("Zoom Map") 
        self.zoom_map = Basemap(projection='merc',
                         lat_0=50,
                         lon_0=-100,
                         area_thresh = 10000.0,
                         llcrnrlat=lat1-1.5,
                         llcrnrlon=lon1-2.75,
                         urcrnrlat=lat1+1.5,
                         urcrnrlon=lon1+2.75,
                         resolution='i')
        self.zoom_map.drawcoastlines()
        self.zoom_map.drawcountries()
        self.zoom_map.drawmapboundary()
        self.zoom_map.drawstates()

        for i in range(len(number)):
            if number[i] == 0:
                self.zoom_map.plot(x[i], y[i], 'ko', markersize=size[i]/1300)
            else: # number[i] >= 0:
                self.zoom_map.plot(x[i], y[i], 'go', markersize=size[i]/1300)

        self.fig.canvas.draw() # draws the figure

    def run(self):
        """
        This functions runs the other functions in the class. When the mouse is clicked,
        first in_box runs then on_click to make the experience interactive
        """
        cid_up = self.fig.canvas.mpl_connect('button_press_event', self.in_box)
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        plt.show()

""" Runs the ZoomMap class and its methods """
zm = ZoomMap()
zm.run()