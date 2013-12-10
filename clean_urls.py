import os
import glob

folders = glob.glob("*")

real = []
for i in folders:
    if not ".py" in i:
        if not ".txt" in i:
            if not "Base" in i:
                real.append(i)

for i in real:
    os.chdir(i)
    urls = open("urls_to_scrape.txt","r")
    urls_to_scrape = []
    for i in urls:
        if ".html" in i:
            urls_to_scrape.append(i)
    urls.close()
    urls = open("urls_to_scrape.txt","w")
    for i in urls_to_scrape:
        urls.write(i)
    urls.close()
    os.chdir("../")
