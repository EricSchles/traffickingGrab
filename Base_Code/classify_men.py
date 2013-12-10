import glob
import os
from subprocess import *

#classifier comes from http://www.stevenloria.com/how-to-build-a-text-classification-system-with-python-and-textblob/

from textblob.classifiers import NaiveBayesClassifier

os.chdir("results/results_men/john/")
positive_train_files = glob.glob("*.html")
train = []
test = []

for i_file in positive_train_files:
    j_file = open(i_file,"r")
    j_contents = j_file.read()
    j_file.close()
    
    start_offset = j_contents.find('<section id="postingbody">')
    end_offset = j_contents.find('</section>',start_offset)
    post_body = j_contents[start_offset:end_offset]
    post_body = post_body.replace('<section id="postingbody">','')
    
    try:
        post_body = post_body.decode('utf-8')
    except UnicodeDecodeError:
        continue


    train.append((post_body,'positive'))
    


os.chdir("../non_john")
negative_train_files = glob.glob("*.html")
for i_file in negative_train_files:
    j_file = open(i_file,"r")
    j_contents = j_file.read()
    j_file.close()

    start_offset = j_contents.find('<section id="postingbody">')
    end_offset = j_contents.find('</section>',start_offset)
    post_body = j_contents[start_offset:end_offset]
    post_body = post_body.replace('<section id="postingbody">',' ')
    post_body = post_body.decode('utf-8')

    train.append((post_body,'negative'))
    


os.chdir("../")
testing = glob.glob("*.html")
for i_file in testing:
    j_file = open(i_file,"r")
    j_contents = j_file.read()
    j_file.close()
    
    start_offset = j_contents.find('<section id="postingbody">')
    end_offset = j_contents.find('</section>',start_offset)
    post_body = j_contents[start_offset:end_offset]
    post_body = post_body.replace('<section id="postingbody">',' ')
    try:
        post_body = post_body.decode('utf-8')
    except UnicodeDecodeError:
        continue

    test.append([post_body,i_file])
    

Bayes = NaiveBayesClassifier(train)

print os.getcwd()

pos = []
neg = []
for body in test:
    
    judge = Bayes.classify(body[0])
    if judge == "positive":
        call(['mv', "./"+body[1], "john/"])
        os.getcwd()
    if judge == "negative":
        call(['mv', "./"+body[1],"non_john/"])

os.mkdir("hard_to_classify")    
remaining = glob.glob("*.html")
for doc in remaining:

    call(['mv', "./"+doc, "hard_to_classify/"])

#print Bayes.accuracy(test)
print Bayes.show_informative_features(10)

# #advanced feature extraction - slang and misspellings

