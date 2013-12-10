import re
import os
from subprocess import *
import glob

def time_posted(contents):
    offset = contents.find("Posted: <time datetime=")
    date = contents[offset+24:offset+33] 
    #this is a based on the conventions within craigslist
    #date format: year-month-dayTHour:minute:second-timezone (based on gmt)
    #example: <time datetime="2013-11-22T
    return date

def count_occurrence(dates):
    exists = {}
    for date in dates:
        if date in exists:
            exists[date] += 1
        else:
            exists[date] = 0
    return exists

os.chdir("results/cleaned_results")

dates = []
files_to_check = glob.glob("*.html")
for i_file in files_to_check:
    j_file = open(i_file,"r")
    j_contents = j_file.read()
    date = time_posted(j_contents) 
    dates.append(date)


freq = count_occurrence(dates)

timeline = open("timeline.csv","w")
for i in freq:
    timeline.write(i+","+str(freq[i])+"\n")

timeline.close()
