# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 14:41:07 2017

@author: Chirravuri
"""

from nltk.util import ngrams
from collections import Counter
import string
import re
import codecs
sum_count=[]
l=[]
f= codecs.open("Open the required file",'r','utf-8' )

translate_table = dict((ord(char), None) for char in string.punctuation)  #Translation table
print "Creating ========> File" 
for line in f:                            #Pre-processing steps
    line=line.replace('\t','')            #Removing the tab space
    line = line.strip()                   # Dividing the sentences
    line=line.translate(translate_table)         
    line=re.sub(r"\d+", "", line)           #Removing numbers/digits
    line = line.lower()                    #Making everything into lowercase
    l.append(line)                    #Adding every line from the text
    line_all = ''.join(l)          #joining everything in list
    
line_all=re.sub(' +',' ',line_all)     #Replacing consecutive spaces with single space
line_all=re.sub("'",'',line_all)       #Removing the " ' "
text = list(line_all)
                              #Printing the total lines character-wise
ngrams = ngrams(text,'n')        #Using nltk for ngrams => for bigrams replace 'n' with '2'

ngram_model=Counter(ngrams)[()]    # Counter is an object
print ngram_model
