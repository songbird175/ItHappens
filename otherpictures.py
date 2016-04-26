import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pylab import *
import sys

def remap_interval(val, input_start, input_end, output_start, output_end):
    """
    takes an input interval, a value in the input interval and returns a 
    subsequent value in the output interval 
    """
    #everything needs to be a float
    float(val)
    float(input_end)
    float(input_start)
    float(output_end)
    float(output_start)
    input_space = float(input_end-input_start)
    output_space = float(output_end-output_start)
    diff = val - input_start
    #gets the value in a form that compares it to the input interval
    ratio = output_space/input_space
    newval = output_start + diff*ratio
    return int(newval)


#size, rank, tuition, reporting
BLANK = [0,0,0,0] #for when you want to do fewer than four
babson = [3343,100,46784, (6.0/3343)*100]#Babson College
bates = [1773,25,48435,(8.0/1773)*100]#Bates College
brandeis = [5945,34,49598,(12.0/5945)*100]#Brandeis University
brown = [9181,14,49346, (21.0/9181)*100]#Brown University
bostonu = [32112,41,48436,(8.0/32112)*100]#Boston Univeristy
bostoncollege = [13575,30,49324,(11.0/13575)*100]#Boston College
# calpolyslo = [19246,10,20160,    ]
caltech = [2209,10, 45390, (4.0/2209)*100]#California Institute of Technology
columbia = [24221,4,51008,(22.0/24221)*100]#Columbia University
cornell = [21850,15,49116,(11.0/21850)*100]#Cornell University
dartmouth= [6298,12,49506,(26.0/6298)*100]#Dartmouth College
harvard = [19929,2,45278,(35.0/19929)*100]#Harvard University
mit = [11319,7,46704,(13.0/11319)*100]#Massachusetts Institute of Technology
#michiganstate = [50085,75,36360,   ]
northeastern = [19798,47,45530,(11.0/19798)*100]#Northeastern University
nyu = [49274,32,46170,(4.0/49274)*100]#New York University
olin = [350,3,45525/2,(1.0/350)*100]#Olin College of Engineering
#oregon = [24096,103,30888,   ]
pitt = [28617,66,28958,(47.0/28617)*100]#University of Pittsburgh
princeton = [8088,1,43450,(17.0/8088)*100]#Princeton University
stanford = [16795,4,46320,(26.0/16795)*100]#Stanford University
wellesley = [2323,4,46836,(6.0/2323)*100]#Wellesley College
# washstate = [23867,140,25567   ]
washu = [7401,15,48093,(21.0/7401)*100]#Washington University in St. Louis
ucberkeley =[37581,20,38140,(39.0/37581)*100]#University of California Berkeley
ucdavis = [34508,41,38659,(32.0/34508)*100]#University of California Davis
ucla = [43239,23,35631,(43.0/43239)*100]#University of California LA
#ucsd = [24810,39,38066   ]
upenn = [9746,9,49536,(17.0/9746)*100]#University of Pennsylvania
#umassamherst = [22252,75,30689,   ]
#umich = [43625,29,43377,   ]
#uofa = [32987,121,30025,   ]
#uw = [30672,52,33513,    ]
yale = [5477,3,47600,(12.0/5477)*100]

ivies_average=[(brown[0]+columbia[0]+cornell[0]+dartmouth[0]+harvard[0]+upenn[0]+princeton[0]+yale[0])/8,
(brown[1]+columbia[1]+cornell[1]+dartmouth[1]+harvard[1]+upenn[1]+princeton[1]+yale[1])/8,
(brown[2]+columbia[2]+cornell[2]+dartmouth[2]+harvard[2]+upenn[2]+princeton[2]+yale[2])/8,
(brown[3]+columbia[3]+cornell[3]+dartmouth[3]+harvard[3]+upenn[3]+princeton[3]+yale[3])/8]
#SEC_average= 
# CLAREMONT

def make_lists(s1,s2,s3,s4):
    sizes_raw = [s1[0],s2[0],s3[0],s4[0]]
    ranks_raw = [s1[1],s2[1],s3[1],s4[1]]
    tuitions_raw =[s1[2],s2[2],s3[2],s4[2]]
    reporting_2014_raw = [s1[3],s2[3],s3[3],s4[3]]
    sizes = []
    ranks = []
    tuitions = []
    reporting_2014 = []
    for i in sizes_raw:
        a = remap_interval(i, 0, max(sizes_raw), 0,20)
        sizes.append(a)
    for i in ranks_raw:
        if i !=0:
            a = remap_interval(max(ranks_raw)+1-i, 0, max(ranks_raw), 0,20)
            ranks.append(a)
        else:
            a = remap_interval(i, 0, max(ranks_raw), 0,20)
            ranks.append(a)
    for i in tuitions_raw:
        a = remap_interval(i, 0, max(tuitions_raw), 0,20)
        tuitions.append(a)
    for i in reporting_2014_raw:
        a = remap_interval(i, 0, max(reporting_2014_raw), 0,20)
        reporting_2014.append(a)
    return sizes+ranks+tuitions+reporting_2014

def plot_it(c1,c2,c3,c4,s1,s2,s3,s4):
    """makes the polar plot with colors"""
    radii = make_lists(s1,s2,s3,s4)
    theta = [1.15,1.3,1.45,1.6,2.7,2.85,3,3.15,4.3,4.45,4.6,4.75,5.85,6,6.15,6.3]
    width = 0.4
    colors = [c1,c2,c3,c4,c1,c2,c3,c4,c1,c2,c3,c4,c1,c2,c3,c4]
    ax = plt.subplot(111, projection='polar',axisbg='w')
    ax.set_xticklabels(['         Relative \n            Reporting \n         (2015)', '', 'Relative Size', '', 'Prestige                   \n(Relative US News                                               \nRank 2015)                              ', '', 'Relative Tuition', ''])
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    ax.set_rgrids([5,10,15,20,25], angle=22., color='w')
    ax.legend([plt.bar(0,0,color=c1),plt.bar(0,0,color=c2),plt.bar(0,0,color=c3),
    plt.bar(0,0,color=c4)],['MIT','Average of Ivy League','Olin','UCLA'],loc=4)
    color_index = 0
    for r, bar in zip(radii, bars):
        bar.set_facecolor(colors[color_index])
        bar.set_alpha(0.5)
        color_index = color_index + 1
    plt.show()

plot_it('blue','yellow','red','cyan',mit,ivies_average,olin,dartmouth)
