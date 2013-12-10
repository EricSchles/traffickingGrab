"This script sets up the scrapers for all 50 states"

from subprocess import *
import os

national = open("national_links.txt","r")

for url in national:
    
    url,name = url.split(",")[0],url.split(",")[1]
    url = url.rstrip().lstrip()
    
    name = name.rstrip().lstrip()
    name = name.replace("(","")
    name = name.replace(")","")
    name = name.replace("-","")
    name = name.replace("/","")
    name = name.replace(" ","_")
    
    os.mkdir(name)
    call(['cp','Base_Code/config.py',name+"/config.py"])
    call(['cp','Base_Code/automate.py',name+"/automate.py"])
    call(['cp','Base_Code/classify_men.py',name+"/classify_men.py"])
    call(['cp','Base_Code/classify_women.py',name+"/classify_women.py"])
    call(['cp','Base_Code/generate_craigslist.py',name+"/generate_craigslist.py"])
    call(['cp','Base_Code/link_scrap.py',name+"/link_scrap.py"])
    call(['cp','Base_Code/phone_analysis.py',name+"/phone_analysis.py"])
    call(['cp','Base_Code/posts_over_time.py',name+"/posts_over_time.py"])
    call(['cp','Base_Code/recursive_scrape.py',name+"/recursive_scrape.py"])
    call(['cp','Base_Code/results_filter_men.py',name+"/results_filter_men.py"])
    call(['cp','Base_Code/results_filter_women.py',name+"/results_filter_women.py"])
    call(['cp','Base_Code/hash_scrap.py',name+"/hash_scrap.py"])
    call(['cp','Base_Code/recursive_generate.py',name+"/recursive_generate.py"])
    
    os.chdir(name)
    call(['python','config.py',url])
    os.chdir("../")
    
    
