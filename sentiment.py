from __future__ import division
#import urllib
#import csv
from string import punctuation


files=['-ve.txt','+ve.txt','file3.txt']


senti = open("file3.txt").read()
senti_list = senti.split('\n')

pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]


for senti in senti_list:
    positive_counter=0
    negative_counter=0
    
    senti_processed=senti.lower()
    
    
    for p in list(punctuation):
        senti_processed=senti_processed.replace(p,'')

    words=senti_processed.split(' ')
    
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
            positive_counts.append(positive_counter)
        
        elif word in negative_words:
            negative_counter=negative_counter+1
            negative_counts.append(negative_counter)
        
#print len(positive_counts)
#print len(negative_counts)

a = len(positive_counts)-len(negative_counts)

if a > 0 and a < 7:
   print "average product"
elif len(positive_counts)==len(negative_counts):
    print "Buy at your own risk"
elif a > 6:
    print "Good Product to buy"
 
else:
    print "don't buy"


