# a program to sort the data needed for the map
# and then put the usable data into a new csv file

import pandas as pd
import numpy as np 
import csv

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
        list1.append(col_value)
    return list1

def college_coords(name):
    """
    returns the latitude and longitude depending on the list of colleges
    determined by the variable 'list1'. 
    """
    # data containing the college name and colelge coordinates
    size = panda_to_list('Public_public.csv', 'Institution Size')
    case = panda_to_list('Public_public.csv', 'Sex offenses - Non-forcible')
    lname = panda_to_list('hd2011.csv', 'INSTNM')
    lat = panda_to_list('hd2011.csv', 'LATITUDE')
    lon = panda_to_list('hd2011.csv', 'LONGITUD')

    # initializes empty lists
    lons = []
    lats = []
    coords_list = []
    no_coords = []
    sizes = []
    cases = []

    # sorts between the two data lists by checking if
    # the names of the colleges match. If the names of the 
    # colleges match, that college has a latitude and longitude.
    # If the names of the colleges don't match, that college gets
    # added to a list of colleges we need coordinates for.
    for college1 in name:
        for college2 in lname:
            if college1 == college2:
                index = lname.index(college2)
                index2 = name.index(college1)
                lons.append(float(lon[index]))
                lats.append(float(lat[index]))
                sizes.append(float(size[index2]))
                cases.append(float(case[index2]))
                coords_list.append(college1)
        if college1 not in coords_list:
            no_coords.append(college1)
    return [coords_list, lons, lats, sizes, cases]

college_info = college_coords(panda_to_list('Public_public.csv', 'Institution name'))
college_name = college_info[0]
college_lons = college_info[1]
college_lats = college_info[2]
college_size = college_info[3]
college_case = college_info[4]

# creating columns in the csv file
my_df = pd.DataFrame({'name' : college_name, 
                      'size' : college_size,
                      'lats' : college_lats,
                      'lons' : college_lons,
                      'case' : college_case})
my_df.to_csv('output2.csv', index=False)
