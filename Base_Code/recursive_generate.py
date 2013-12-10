
"""
Creates a new scrapy project with 'name' taken from the config.txt file.
Then copies the config.txt file into the spider directory in the newly created project.
"""
from subprocess import *
import os
import sys, string
#backend code generator class, comes from: http://effbot.org/zone/python-code-generator.htm

class CodeGeneratorBackend:
    
    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        return string.join(self.code, "")
    
    def write(self, string):
        self.code.append(self.tab * self.level + string)
        
    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "already level 0, you cannot dedent less than 0, silly"
        self.level = self.level - 1


config = open("config.txt","r")

#we strip the trailing newlines with strip() because it causes a formatting error
#when we try to write to the name_spider.py file  
name = config.readline()    #for line is always the name of the scraper
name_unique = "craigslist"+(name.split("/")[-1].split(".")[0])
name = name.split('.')
domain_name = name[1]+"."+name[2] #domain name
domain_name = domain_name.split("/")[0]
domain_name = domain_name.strip()
name = name[1]


config.seek(0)  #reset config file to first line


urls_to_scrap = []
for i in config:
    if i != "\n":
        urls_to_scrap.append(i.strip())

config.close()

#You MUST not use the name for the project as the scraper otherwise it will throw an error
#I have no idea why this would happen, however I found the solution here:
#https://groups.google.com/forum/#!topic/scrapy-users/KGgL8RMLtuY
#My solution was to simply append 'scraper' to the directory names
print "calling scrapy, startproject,", name_unique
call(['scrapy', 'startproject', name_unique+'scraper'])
print "moving config to spiders directory"
call(['cp', 'config.txt' ,'./'+name_unique+'scraper/'+name_unique+'scraper/spiders/'])


#here we make items.py to define the elements we scrap
print "generating items.py"
#we don't need to change this because it is only staticly generated content
item_py_contents = """
from scrapy.item import Item, Field

class """+name_unique+"""Item(Item):
    title = Field()
    link = Field()
    desc = Field()
"""
item_py= open("items.py", "w")
item_py.write(item_py_contents)
item_py.close()

print "moving items.py into /"+name_unique+"scraper/"+name_unique+"scraper/"
call(['cp', 'items.py', './'+name_unique+'scraper/'+name_unique+'scraper/'])
 
#here we make the spider, which does most of the scraping for us
#eventually we'll need to take parameters that are passed in, to make this spider more flexible
print "generating "+name_unique+"_spider.py"

#what the spider used to look like:
spider_py_contents_start = """

from scrapy.spider import BaseSpider

class """+name_unique+"""Spider(BaseSpider):
    name = \""""+name_unique+"""\"
    allowed_domains = """ +'["'+domain_name+'"]'+ """
    start_urls = ["""
        
spider_py_contents_end =""" 
]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        #prefix = response.url.split("/")[-3]
        #open(prefix+"_"+filename+".html", 'wb').write(response.body)
        open(filename+".html", 'wb').write(response.body)

"""

spider_py_contents_middle = CodeGeneratorBackend()
spider_py_contents_middle.begin()

spider_py_contents_middle.write("\n")
spider_py_contents_middle.indent()

spider_py_contents_middle.indent()

#need quotes otherwise it won't be read as a string

urls = []
for i in urls_to_scrap[:-1]:
    urls.append(i)
last_one = urls_to_scrap[-1]
#the reason we do [0,n-1] is because there is no comma on the last element in the listing
for i in urls:
    spider_py_contents_middle.write(' "'+i+'",\n')
spider_py_contents_middle.write(' "'+last_one+'"\n')

spider_py_contents_done = spider_py_contents_middle.end()

spider_py_contents_full = spider_py_contents_start + spider_py_contents_done + spider_py_contents_end

spider_py= open(name_unique+"_spider.py", "w")
spider_py.write(spider_py_contents_full)
spider_py.close()

print "moving "+name_unique+"_spider.py into /"+name_unique+"scraper/"+name_unique+"scraper/spiders"
call(['cp', name_unique+'_spider.py', './'+name_unique+'scraper/'+name_unique+'scraper/spiders/'])

#cleaning up
print "cleaning up residue files..."
call(['rm', name_unique+'_spider.py'])
call(['rm', 'items.py'])
