import glob
import os
from subprocess import *
import time

to_fix_places = glob.glob("*")

places = []
for i in to_fix_places:
    if not ".py" in i:
        if not ".txt" in i:
            if not "Base" in i:
                places.append(i)


for place in places:
    os.chdir(place)
    os.getcwd()

    #most of this is being careful
    #call(['rm','recursive_scrape.py'])
    #call(['cp','../Base_Code/recursive_scrape.py','../'+place+'/recursive_scrape.py'])

    # if os.path.exists("results"):
    #     os.chdir("results")
    #     curr_dir = glob.glob("*")

    #     if curr_dir != []:
    #         os.chdir("../../")
    #         continue
        
    #     os.chdir("../")
    #     os.rmdir("results")
        

    # if os.path.exists("recursive_top_level"):
    #     os.chdir("recursive_top_level")
    
    #     files_to_delete = glob.glob("*")
    #     for i in files_to_delete:
    #         os.remove(i)

    #     os.chdir("../")
    #     os.rmdir("recursive_top_level")
    
    

    call(['python','recursive_scrape.py'])
    os.getcwd()
    os.chdir("../")
    time.sleep(3)


