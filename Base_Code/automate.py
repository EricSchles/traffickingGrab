from subprocess import *

#generate the spider
call(['python','generate_craigslist.py'])


#run the spider
call(['python', 'link_scrap.py'])

