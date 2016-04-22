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
    returns the latitude and longitude depending of the list of colleges
    determined by the input variable "name". The variable name is a list of 
    the name of colleges in a file matching to assault data (a dataset that
    does not contain college coordinates). The purpose of this function is to
    match a college to it's coordinates by comparing two datasets. The ouput
    of this function can then be put into a csv file for later use.
    """
    # lists from college we have case data for 
    size = panda_to_list('Public_public.csv', 'Institution Size')
    case = panda_to_list('Public_public.csv', 'Sex offenses - Forcible')

    # lists from college we have coordinates for 
    names_with_coords = panda_to_list('hd2011.csv', 'INSTNM')
    lat = panda_to_list('hd2011.csv', 'LATITUDE')
    lon = panda_to_list('hd2011.csv', 'LONGITUD')

    # initializes empty lists
    lons = []
    lats = []
    coords_list = []
    no_coords = []
    sizes = []
    cases = []

    # Sorts between the two data lists by checking if the names of
    # the colleges match (if college1 == college2). If the names of the 
    # colleges match, that college  can be matched with a latitude 
    # and longitude. If the names of the colleges don't match, that
    # college gets added to a list of colleges we need coordinates for.
    for college1 in name:
        for college2 in names_with_coords:
            if college1 == college2:
                index = names_with_coords.index(college2)
                index2 = name.index(college1)
                lons.append(float(lon[index]))
                lats.append(float(lat[index]))
                sizes.append(float(size[index2]))
                cases.append(float(case[index2]))
                coords_list.append(college1)
        if college1 not in coords_list:
            no_coords.append(college1)
    return [coords_list, lons, lats, sizes, cases]


def non_zero_sorting(return_what):
    """
    returns a list of information about the college used in basemap. This 
    program is meant to separate the colleges by the number they reported 
    (either zero, 'nan', or nonzero).
    """
    college_info = college_coords(panda_to_list('Public_public.csv', 'Institution name'))
    name = college_info[0]
    lons = college_info[1]
    lats = college_info[2]
    size = college_info[3]
    unsorted_list = college_info[4]

    # initialize empty lists for nonzero numbers
    nonzero_college = []
    nonzero_size = []
    nonzero_num = []
    nonzero_lats = []
    nonzero_lons = []

    # initialize empty lists for zero numbers
    zero_college = []
    zero_size = []
    zero_num = []
    zero_lats = []
    zero_lons = []
    
    # separates the unsorted list according to zero versus nonzero
    for i in range(len(unsorted_list)):
        if unsorted_list[i] == 0.0 or unsorted_list[i] == 'nan':
            zero_college.append(name[i])
            zero_size.append(float(size[i]))
            zero_num.append(float(0))
            zero_lats.append(float(lats[i]))
            zero_lons.append(float(lons[i]))
        elif unsorted_list[i] > 0:
            nonzero_college.append(name[i])
            nonzero_size.append(float(size[i]))
            nonzero_num.append(float(unsorted_list[i]))
            nonzero_lats.append(float(lats[i]))
            nonzero_lons.append(float(lons[i]))
    if return_what == 'nonzero':
        return [nonzero_college, nonzero_lons, nonzero_lats, nonzero_size, nonzero_num]
    elif return_what == 'zero':
        return [zero_college, zero_lons, zero_lats, zero_size, zero_num]


info = non_zero_sorting('zero')
c_name = info[0]
c_lons = info[1]
c_lats = info[2]
c_size = info[3]
c_case = info[4]

# creating columns in the csv file
my_df = pd.DataFrame({'name' : c_name, 
                      'size' : c_size,
                      'lats' : c_lats,
                      'lons' : c_lons,
                      'case' : c_case})
my_df.to_csv('output3.csv', index=False)

