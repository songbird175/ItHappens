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
    name = panda_file_to_list('Public_public.csv', 'Institution name')
    size = panda_file_to_list('Public_public.csv', 'Institution Size')
    unsorted_list = panda_file_to_list('Public_public.csv', column_title)
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

print(non_zero_sorting('Sex offenses - Forcible'))



