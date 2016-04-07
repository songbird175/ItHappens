#  cleaning up data
import pandas as pd

def panda_file_to_list(file_name, title1):
    """
    The opens a saved csv file and convert it to a panda file. The 
    panda file is separated into columns and the columns are made into
    lists. The lists are the output of the funciton. 
    """
    datafile = pd.read_csv(file_name) #opens a data file

    # converts the data file into columns
    for col in datafile.columns:
        datafile[col] = datafile[col].astype(str)
    column1 = datafile[title1]
    # column2 = datafile[title2].astype(float)

    # creates lists from the columns
    list1 = []
    for col_value in column1:
        list1.append(col_value)
    return list1

def non_zero_sorting(column_title):
    """makes two lists of tuples (nonzero number and zero numbers). Each tuple 
    includes the name of the college, the number of students and the number 
    of the case specified by 'column_title'.
    """
    name = panda_file_to_list('Public_public.csv', 'Institution name')
    size = panda_file_to_list('Public_public.csv', 'Institution Size')
    unsorted_list = panda_file_to_list('Public_public.csv', column_title)

    lname = panda_file_to_list('hd2011.csv', 'INSTNM')
    lat = panda_file_to_list('hd2011.csv', 'LATITUDE')
    lon = panda_file_to_list('hd2011.csv', 'LONGITUD')

    nonzero_list = []
    zero_list = []

    for i in range(len(unsorted_list)):
        if unsorted_list[i] == '0.0' or unsorted_list[i] == 'nan':
            tupl2 = (name[i], size[i], unsorted_list[i])
            zero_list.append(tupl2)
        else:
            tupl1 = (name[i], size[i], unsorted_list[i])
            nonzero_list.append(tupl1)
    return nonzero_list


def college_coords():
    lname = panda_file_to_list('hd2011.csv', 'INSTNM')
    lat = panda_file_to_list('hd2011.csv', 'LATITUDE')
    lon = panda_file_to_list('hd2011.csv', 'LONGITUD')
    name = panda_file_to_list('Public_public.csv', 'Institution name')

    coords = []
    coords_list = []
    no_coords = []

    for college1 in name:
        for college2 in lname:
            if college1 == college2:
                index = lname.index(college2)
                tupl3 = (college1, lat[index], lon[index])
                coords.append(tupl3)
                coords_list.append(college1)
        if college1 not in coords_list:
            no_coords.append(college1)
    return [len(coords), len(coords_list), len(no_coords)


print(college_coords())
