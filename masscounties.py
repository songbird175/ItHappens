from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np



class CountyMap(object):
    """ A class that encompasses an interactive visualization of some
        of the counties in the Northeast """

    def __init__(self):
        """ Initialize the map by creating the Basemap object,
            drawing the county outlines, filling in some of the
            counties with various colors, and plotting a dot
            on Olin College. """
        self.m = Basemap(projection='mill',
                         llcrnrlat=40,
                         llcrnrlon=-75,
                         urcrnrlat=43,
                         urcrnrlon=-69.5,
                         resolution='c')
        self.last_hover = None
        self.counties = self.m.drawcounties(linewidth=1)
        x, y = self.get_x_y(-71.2639, 42.2935)
        self.m.plot(x, y, 'k.')
        self.dots()
        plt.gcf().canvas.mpl_connect('motion_notify_event', self.on_hover)
        plt.ion()
        plt.show()
        self.text = None

    def get_x_y(self, lon, lat):
        """ Returns the x, y coordinate of a given longitude and lattitude """
        return self.m(*np.asarray([lon, lat]))

    def get_lon_lat(self, x, y):
        """ Returns longitude, lattitude for a given x, y plot coordinate """
        return self.m(*np.asarray([x, y]), inverse=True)

    def on_hover(self, event):
        """ Handle matplotlib mouse events.  All we do currently is save
            the coordinates of the mouse for later processing """
        if event.xdata and event.ydata:
            self.last_hover = (event.xdata, event.ydata)

    def run(self):
        """ The main run loop of the program.  The loop continuously updates
            the plot using the last registered position of the mouse.
            The mouse position is also used to compute which county the
            user is currently hovering over.  Based on this determination
            the text displayed to the user is updated.
        """
        # cache the paths for faster performance in the loop
        paths = self.counties.properties()['paths']
        # while True:
        #     if self.last_hover:
        #         lon, lat = self.get_lon_lat(self.last_hover[0],
        #                                     self.last_hover[1])
        #         new_text = "Lattitude %f, \nLongitude %f" % (lat, lon)

        #         for i, path in enumerate(paths):
        #             if (path.contains_point(self.last_hover)):
        #                 new_text += "\n" + self.m.counties_info[i]['NAME']
        #                 break
        #         if not self.text:
        #             self.text = plt.gca().text(self.last_hover[0],
        #                                        self.last_hover[1],
        #                                        new_text,
        #                                        style='italic',
        #                                        bbox={'facecolor': 'red',
        #                                              'alpha': 0.5,
        #                                              'pad': 10})
        #         else:
        #             self.text.set_x(self.last_hover[0])
        #             self.text.set_y(self.last_hover[1])
        #             self.text.set_text(new_text)

        #     # make sure that the plot is redrawn
        #     plt.gcf().canvas.update()
        #     plt.gcf().canvas.flush_events()
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



if __name__ == '__main__':
    cm = CountyMap()
    cm.run()