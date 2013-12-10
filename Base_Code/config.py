"""
This script creates a file that has the domain name and the starting urls for a new scrapper class.  These urls are line seperated.
"""

from sys import argv

config = open("config.txt","w")


base = argv[1]
start = base+"/cas/"
to_append = start
url_list = []
url_list.append(base)
url_list.append(start)

for i in xrange(1,100):
    to_append += "index"+str(i)+"00.html"
    url_list.append(to_append)
    to_append = start

for i in url_list:
    config.write(i + "\n")


config.close()
