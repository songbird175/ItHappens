import matplotlib.pyplot as plt
import pandas as pd

def panda_file_to_list(file_name, title1, title2,title3,title4,title5,title6,title7,title8,title9,title10):
    """
    The function opens a saved csv file and converts it to a panda file. The 
    panda file is separated into columns and the columns are made into lists. 
    """
    datafile = pd.read_csv(file_name) #opens a data file
    # converts the data file into columns
    for col in datafile.columns:
        datafile[col] = datafile[col].astype(str)
    column1 = datafile[title1]
    column2 = datafile[title2].astype(float)
    column3 = datafile[title3].astype(float)
    column4 = datafile[title4].astype(float)
    column5 = datafile[title5].astype(float)
    column6 = datafile[title6].astype(float)
    column7 = datafile[title7].astype(float)
    column8 = datafile[title8].astype(float)
    column9 = datafile[title9].astype(float)
    column10 = datafile[title10].astype(float)
    # creates lists from the columns
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    for col_value in column1:
        list1.append(col_value)
    for col_value in column2:
        list2.append(col_value)
    for col_value in column3:
        list3.append(col_value)
    for col_value in column4:
        list4.append(col_value)
    for col_value in column5:
        list5.append(col_value)
    for col_value in column6:
        list6.append(col_value)
    for col_value in column7:
        list7.append(col_value)
    for col_value in column8:
        list8.append(col_value)
    for col_value in column9:
        list9.append(col_value)
    for col_value in column10:
        list10.append(col_value)
    output = [list1, list2,list3, list4,list5,list6,list7,list8,list9,list10]
    return output

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

# The slices will be ordered and plotted counter-clockwise.
filename = 'testtotal.csv'
info = panda_file_to_list(filename, '2005', '2006','2007','2008','2009','2010','2011','2012','2013','2014')
labels = 'Public'
sizes = info
colors = ['gold', 'lightskyblue']
explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

fig = plt.figure()
ax = fig.gca()
import numpy as np

ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(0, 0), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(1, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(0, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(1, 0), frame=True)

ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["Sunny", "Cloudy"])
ax.set_yticklabels(["Dry", "Rainy"])
ax.set_xlim((-0.5, 1.5))
ax.set_ylim((-0.5, 1.5))

# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.set_aspect('equal')

plt.show()