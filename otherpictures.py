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
    #find the size of the input and output spaces
    input_space = float(input_end-input_start)
    output_space = float(output_end-output_start)
    #gets the value in a form that compares it to the input interval
    diff = val - input_start
    ratio = output_space/input_space
    #The new value will be the distance between the input ratio start 
    #and the value, scaled by the ratio between the output and input
    #spaces and inserted into the ouput space
    newval = output_start + diff*ratio
    return newval

#Institutions that we can put on polar charts
#rank and tuition are from US news, size and reporting are from our data
#size, rank, tuition, reporting
HIGH = [3.36]#the presumed actual percentage of college students assaulted
#anually, based on the famous "1 in 5 or 16" survey
BLANK = [0,0,0,0] #for when you want to do fewer than four
auburn = [25912,102,28040,(5.0/25912)*100]#Auburn University
babson = [3049,100,46784,(8.0/3049)*100]#Babson College
barnard = [2573,29,47631,(7.0/2573)*100]#Barnard College
bates = [1773,25,48435,(12.0/1773)*100]#Bates College
brandeis = [5945,34,49598,(10.0/5945)*100]#Brandeis University
brown = [9181,14,49346,(43.0/9181)*100]#Brown University
brynmawr = [1709,25,47140,(6.0/1709)*100]#Bryn Mawr College
bostonu = [32112,41,48436,(13.0/32112)*100]#Boston Univeristy
bostoncollege = [14317,30,49324,(23.0/14317)*100]#Boston College
calpolyslo = [20186,10,20160,(14.0/20186)*100]#California Polytechnic State University-San Luis Obispo
caltech = [2209,10, 45390,(6.0/2209)*100]#California Institute of Technology
columbia = [27589,4,51008,(27.0/27589)*100]#Columbia University
cornell = [21679,15,49116,(17.0/21679)*100]#Cornell University
dartmouth= [6298,12,49506,(48.0/6298)*100]#Dartmouth College
harvard = [28791,2,45278,(40.0/28791)*100]#Harvard University
lsu = [31044,129,26467,(9.0/31044)*100]#Louisiana State University
lehigh = [7119,47,46230,(7.0/7119)*100]#Lehigh University
mit = [11319,7,46704,(22.0/11319)*100]#Massachusetts Institute of Technology
mississippi= [20138,140,20674,(7.0/20138)*100]#University of Mississippi
olemiss = [22503,161,20142,(4.0/22503)*100]#Mississippi State
michiganstate = [50081,75,36360,(21.0/50081)*100]#Michigan State
mountholyoke = [2255,35,43886,(3.0/2255)*100]#Mount Holyoke College
northeastern = [19798,47,45530,(14.0/19798)*100]#Northeastern University
nyu = [49274,32,46170,(6.0/49274)*100]#New York University
olin = [350,3,45525/2,(2/350.)*100.]#Olin College of Engineering
oregon = [28886,103,30888,(9.0/28886)*100]#Oregon State University
pitt = [28617,66,28958,(27.0/28617)*100]#University of Pittsburgh
princeton = [8088,1,43450,(6.0/8088)*100]#Princeton University
simmons = [4802,116,37380,(3.0/4802)*100]#Simmons College
smith = [2989,14,46288,(3.0/2989)*100]#Smith College
stanford = [16963,4,46320,(30.0/16963)*100]#Stanford University
scripps = [988,29,49152,(4.0/988)*100]#Scripps College
texasam = [61642,70,26536,(8.0/61642)*100]#Texas A&M University
wellesley = [2323,4,46836,(6.0/2323)*100]#Wellesley College
washstate = [28686,140,25567,(6.0/28686)*100]#Washington State
washu = [14348,15,48093,(17.0/14348)*100]#Washington University in St. Louis
wesleyan = [711,158,20290,(1.0/711)*100]#Wesleyan College
bama = [36047,96,25950,(17.0/36047)*100]#The University of AlabamaI
ucberkeley =[37565,20,38140,(24.0/37565)*100]#University of California Berkeley
ucdavis = [34508,41,38659,(19.0/34508)*100]#University of California Davis
ucla = [41845,23,35631,(26.0/41845)*100]#University of California LA
uflorida = [49459,47,28591,(6.0/49459)*100]#University of Florida
ugeorgia = [35197,61,29832,(16.0/35197)*100]#University of Georgia
ukentucky = [29203,129,24268,(21.0/29203)*100]#University of Kentucky
umissouri = [35425,103,25166,(12.0/35425)*100]#University of Missouri
usc = [42453,108,29440,(2.0/42453)*100]#University of South Carolina
utennessee = [30386,103,30138,(11.0/30386)*100]#University of Tennessee
ucsd = [30709,39,38066,(10.0/30709)*100]#University of California San Diego
upenn = [24806,9,49536,(13.0/24806)*100]#University of Pennsylvania
uarkansas = [26237,129,23320,(4.0/26237)*100]#University of Arkansa
umassamherst = [28635,75,30689,(12.0/28635)*100]#UMass Amherst 
umich = [43625,29,43377,(25.0/43625)*100]#University of Michigan
uvermont = [12856,89,37874,(28.0/12856)*100]#University of Vermont 
vanderbilt = [12686,15,43838,(23.0/12686)*100]#Vanderbilt University 
uofa = [42236,121,30025,(20.0/42236)*100]#University of Arizona
uw = [44784,52,33513,(10.0/44784)*100]#University of Washington 
yale = [12336,3,47600,(17.0/12336)*100]#Yale University
#average of the ivy league
ivies_average=[(brown[0]+columbia[0]+cornell[0]+dartmouth[0]+harvard[0]+upenn[0]+princeton[0]+yale[0])/8,
(brown[1]+columbia[1]+cornell[1]+dartmouth[1]+harvard[1]+upenn[1]+princeton[1]+yale[1])/8,
(brown[2]+columbia[2]+cornell[2]+dartmouth[2]+harvard[2]+upenn[2]+princeton[2]+yale[2])/8,
(brown[3]+columbia[3]+cornell[3]+dartmouth[3]+harvard[3]+upenn[3]+princeton[3]+yale[3])/8]
#average of the SEC
SEC_average=[(bama[0]+auburn[0]+uflorida[0]+ugeorgia[0]+ukentucky[0]+lsu[0]+olemiss[0]+umissouri[0]+usc[0]+utennessee[0]+vanderbilt[0]+uarkansas[0]+mississippi[0]+texasam[0])/14,
(bama[1]+auburn[1]+uflorida[1]+ugeorgia[1]+ukentucky[1]+lsu[1]+olemiss[1]+umissouri[1]+usc[1]+utennessee[1]+vanderbilt[1]+uarkansas[1]+mississippi[1]+texasam[1])/14,
(bama[2]+auburn[2]+uflorida[2]+ugeorgia[2]+ukentucky[2]+lsu[2]+olemiss[2]+umissouri[2]+usc[2]+utennessee[2]+vanderbilt[2]+uarkansas[2]+mississippi[2]+texasam[2])/14,
(bama[3]+auburn[3]+uflorida[3]+ugeorgia[3]+ukentucky[3]+lsu[3]+olemiss[3]+umissouri[3]+usc[3]+utennessee[3]+vanderbilt[3]+uarkansas[3]+mississippi[3]+texasam[3])/14] 
#average of five women's colleges
womens_average = [(barnard[0]+brynmawr[0]+mountholyoke[0]+smith[0]+wesleyan[0])/5,
(barnard[1]+brynmawr[1]+mountholyoke[1]+smith[1]+wesleyan[1])/5,
(barnard[2]+brynmawr[2]+mountholyoke[2]+smith[2]+wesleyan[2])/5,
(barnard[3]+brynmawr[3]+mountholyoke[3]+smith[3]+wesleyan[3])/5]

def make_lists(s1,s2,s3,s4):
    """makes the scaled lists of sizes,ranks,tuitions,and reporting
    with four schools as inputs"""
    HIGH = 3.36
    #the non-relative numbers for each category
    sizes_raw = [s1[0],s2[0],s3[0],s4[0]]
    ranks_raw = [s1[1],s2[1],s3[1],s4[1]]
    tuitions_raw =[s1[2],s2[2],s3[2],s4[2]]
    reporting_2014_raw = [s1[3],s2[3],s3[3],s4[3]]
    reporting_2014_raw_high = [s1[3],s2[3],s3[3],s4[3],HIGH]
    #make the empty lists
    sizes = []
    ranks = []
    tuitions = []
    reporting_2014 = []
    #scale the raw lists relative to themselves
    for i in sizes_raw:
        a = remap_interval(i, 0, max(sizes_raw), 0,20)
        sizes.append(a)
    for i in ranks_raw:
        if i !=0:
            a = remap_interval(max(ranks_raw)+1-i, 0, max(ranks_raw), 0.0,20.0)
            ranks.append(a)
        else: #deals with use of BLANK
            a = remap_interval(i, 0.0, max(ranks_raw), 0.0,20.0)
            ranks.append(a)
    for i in tuitions_raw:
        a = remap_interval(i, 0.0, max(tuitions_raw), 0.0,20.0)
        tuitions.append(a)
# in case we don't want to compare to estimated actual rate
    # for i in reporting_2014_raw:
    #     a = remap_interval(i, 0.0, max(reporting_2014_raw), 0.0,20.0)
        # reporting_2014.append(a)
#scale the reporting numbers relative to themseves and actual rate
    for i in reporting_2014_raw_high:
        a = remap_interval(i, 0.0, max(reporting_2014_raw_high), 0.0,20.0)
        reporting_2014.append(a)
    #remove the actual rate
    reporting_2014 = reporting_2014[0:4]
    return sizes+ranks+tuitions+reporting_2014
def plot_it(c1,c2,c3,c4,s1,s2,s3,s4):
    """makes the polar plot with colors and schools as input"""
    #radii gives lengths of bars, theta puts each category (size,rank,
    #tuition, or reporting) into the correct zone
    radii = make_lists(s1,s2,s3,s4)
    theta = [1.15,1.3,1.45,1.6,2.7,2.85,3,3.15,4.3,4.45,4.6,4.75,5.85,6,6.15,6.3]
    white_theta = [6.1]
    high = 20.0 #the radius value for the white bar
    width = 0.4
    colors = [c1,c2,c3,c4,c1,c2,c3,c4,c1,c2,c3,c4,c1,c2,c3,c4]
    ax = plt.subplot(111, projection='polar',axisbg='w')#the polar plot
    #outer labels
    ax.set_xticklabels(['                  Relative Reporting \n                     (2014)', '', 'Relative Size', '', 'Prestige                                                 \n(Relative US News Rank 2015)                                                                                 ', '', 'Relative Tuition', ''],fontsize=18)
    #establishes our bars for colleges and estimated actual rate
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    white_bar = ax.bar(white_theta,high,width=width, bottom=0.0)
    #eliminates an unwanted label by setting the font size to zero
    ax.set_rgrids([5,10,15,20,25], angle=22., color='w', fontsize=0)
    #creates the legend
    ax.legend([plt.bar(0,0,color=c1),plt.bar(0,0,color=c2),plt.bar(0,0,color=c3),plt.bar(0,0,color=c4),
    plt.bar(0,0,color='whitesmoke')],['Olin College',"Stanford University","University of California at Berkeley",'Massachusetts Institute of Technology','Estimated actual \nsexual assault rate'],loc=4)
    color_index = 0
    #sets the colors of the college bars by iterating through the color list
    for r, bar in zip(radii, bars):
        bar.set_facecolor(colors[color_index])
        bar.set_alpha(0.5)
        color_index = color_index + 1
    #sets the color of the white bar
    for r,bar in zip(HIGH,white_bar):
        bar.set_facecolor('white')
        bar.set_alpha(0.5)
    plt.show()

plot_it('cyan','red','gold','lightgrey',olin,stanford,ucberkeley,mit)
