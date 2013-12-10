import glob
import os
from subprocess import *

to_fix_places = glob.glob("*")

places = []
for i in to_fix_places:
    if not ".py" in i:
        if not ".txt" in i:
            if not "Base" in i:
                places.append(i)


for place in places:
    os.chdir(place)
    call(['python','automate.py'])
    os.chdir("../")

