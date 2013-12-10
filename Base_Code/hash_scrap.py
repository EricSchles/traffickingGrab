from subprocess import *
import os
import hashlib
import glob





present_dir = os.getcwd()

config = open("config.txt","r")

#md5 function comes from http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python/4213255#4213255

#we strip the trailing newlines with strip() because it causes a formatting error
#when we try to write to the name_spider.py file  
name = config.readline()    
print name
name_unique = "craigslist"+(name.split("/")[-1].split(".")[0])
name = name.split('.')
name = name[1]

config.close()
        
def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()



#change directories into the top of the scrapper
os.chdir(name_unique+'scraper/')
print "starting the scraper for the desired webpages"

call(['scrapy', 'crawl', name_unique])



