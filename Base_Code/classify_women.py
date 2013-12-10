import glob
import os
from subprocess import *

#classifier comes from http://www.stevenloria.com/how-to-build-a-text-classification-system-with-python-and-textblob/

from textblob.classifiers import NaiveBayesClassifier

os.chdir("results/results_women/prostitutes")
pos_train_test_files = glob.glob("*.html")
train = []
test = []
categorize = []

positive_train_files = []
positive_test_files = []

pos_size_train = len(pos_train_test_files)
for i in pos_train_test_files[:pos_size_train/2]:
    positive_train_files.append(i)

for i in pos_train_test_files[pos_size_train/2:]:
    positive_test_files.append(i)

#train and test positive
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


    test.append((post_body,'positive'))
    
negative_train_files = []
negative_test_files = []

os.chdir("../non_prostitutes")
neg_train_test_files = glob.glob("*.html")
neg_size_train = len(neg_train_test_files)

for i in neg_train_test_files[:neg_size_train/2]:
    negative_train_files.append(i)

for i in neg_train_test_files[neg_size_train/2:]:
    negative_test_files.append(i)


#train and test positive
for i_file in negative_train_files:
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


    train.append((post_body,'negative'))

for i_file in negative_train_files:
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


    test.append((post_body,'negative'))



os.chdir("../")
classifying = glob.glob("*.html")
for i_file in classifying:
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

    categorize.append([post_body,i_file])

Bayes = NaiveBayesClassifier(train)

print os.getcwd()

print Bayes.accuracy(test)


pos = []
neg = []
for body in categorize:
    
    judge = Bayes.classify(body[0])
    if judge == "positive":
        call(['mv', "./"+body[1], "prostitutes/"])
        os.getcwd()
    if judge == "negative":
        call(['mv', "./"+body[1],"non_prostitutes/"])
try:
    os.mkdir("hard_to_classify")    
except OSError:
    pass
remaining = glob.glob("*.html")
for doc in remaining:

    call(['mv', "./"+doc, "hard_to_classify/"])

#print Bayes.accuracy(test)
print Bayes.show_informative_features(10)

#advanced feature extraction - slang and misspellings

