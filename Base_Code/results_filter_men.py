import re
import os
from subprocess import *
import glob

#terminal nodes
def m4w_check(contents):
    pattern = re.compile("m4w")
    m = pattern.search(contents)
    if m == None:
        return False
    else:
        return True

def picture_check(contents):
    pattern = re.compile(".jpg")
    m = pattern.search(contents)
    if m == None:
        return False
    else:
        return True

#none terminal nodes
def number_of_pictures(contents):
    m = re.findall(".jpg",contents)
    return len(m)

def time_posted(contents):
    offset = contents.find("Posted: <time datetime=")
    date = contents[offset+23:offset+49] 
    #this is a based on the conventions within craigslist
    #date format: year-month-dayTHour:minute:second-timezone (based on gmt)
    return date

    
def digit_grab(body):
    #there are a few distinct obfuscation patterns:
    #one: numbers interlaced in the text
    phone_number = []
    for i in body:
        if i.isdigit():
            phone_number.append(i)
    if len(phone_number) == 9 or len(phone_number) == 10:
        
        return ''.join(phone_number)
    else:
        return None



#three: special characters interlaced with text - this may not matter

def word_to_digit(text):
    text = text.replace("ONE","1")
    text = text.replace("TWO","2")
    text = text.replace("THREE","3")
    text = text.replace("FOUR","4")
    text = text.replace("FIVE","5")
    text = text.replace("SIX","6")
    text = text.replace("SEVEN","7")
    text = text.replace("EIGHT","8")
    text = text.replace("NINE","9")
    text = text.replace("ZERO","0")
    return text

def year_old(contents):
    year_old = contents.find("year old")
    
    if year_old != -1:
        age_final = contents[year_old-3:year_old-1]
        return age_final
    else:
        return None

#md5 function comes from http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python/4213255#4213255

def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()



#generate a list of phone numbers, check for duplicates between postings.
#This may inform possible collusion and may lead to trafficking rings.


#implement other checks as functions, call all of them on the contents
#based on the results from each function check, create an entry in the database,
#these entries determine the overall likelihood of a given posting being what you expect

os.chdir("results")


if not os.path.exists("results_men"):
    os.mkdir("results_men")
results = open("results.csv","w")
files_to_check = glob.glob("*.html")
for i_file in files_to_check:
    j_file = open(i_file,"r")
    j_contents = j_file.read()
    m4w = m4w_check(j_contents)
    #picture_exists = picture_check(j_contents)
    #with women seeking men and picture we are able to conclusively determine
    #whether a given posting is not a prostitute
    if m4w:
        call(['mv', "./"+i_file, "results_men/"])

#I need more time to figure out how to use this...        

# os.chdir("cleaned_results")    
# files_to_check = glob.glob("*.html")
# initial = []
# w_translate = []
# for i_file in files_to_check:
#     j_file = open(i_file,"r")
#     j_contents = j_file.read()
#     start_offset = j_contents.find('<section id="postingbody">')
#     end_offset = j_contents.find('</section>',start_offset)
#     post_body = j_contents[start_offset:end_offset]

#     #determine phone numbers
#     translated_body = post_body.upper()
#     translated_body = word_to_digit(translated_body)
#     phone_number = digit_grab(post_body)
#     phone_translated = digit_grab(translated_body)
#     initial.append([phone_number,i_file])
#     w_translate.append([phone_translated,i_file])

#     age = year_old(post_body)



    
    
# # print "initial results\n"
# # for i in initial:
# #     print i

# # print "\nwith translation\n"
# # for i in w_translate:
# #     print i
    
   
    

