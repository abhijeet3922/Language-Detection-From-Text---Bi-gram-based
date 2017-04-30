# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 15:29:17 2017

@author: Abhijeet Kumar
"""

import os

from nltk.collocations import BigramCollocationFinder
import re
import numpy as np
import codecs

dirname = "C:\\Users\\Charlie\\Desktop\\language-id-text\\LIGA_Benelearn11_dataset\\nl_NL"

lang_name = ["english","german","french","italian","dutch","spanish"]

no_of_bigms = []
for i,lang in enumerate(lang_name):
    root_path = "C:\\Users\\Charlie\\Desktop\\language-id-text\\lid-scratch\\language_models\\gram-based\\"
    model = np.load(root_path+lang+".npy")
    total = 0
    for key,v in model:            
        total = total + v
    no_of_bigms.append(total) 
    print total


root = "C:\\Users\\Charlie\\Desktop\\language-id-text\\lid-scratch\\language_models\\gram-based\\"
model = [np.load(root+lang+".npy") for lang in lang_name]


files = [os.path.join(dirname, f) for f in os.listdir(dirname)]

ep = 0
gp = 0
fp = 0
ip = 0
dp = 0
sp = 0
cd = 0

for f in files:
    
    with codecs.open(f,"r","utf-8") as filep:
        for i,line in enumerate(filep):

            line = re.sub(r"\d+", "", line)
            
            #words = nltk.word_tokenize(line)
            
            finder = BigramCollocationFinder.from_words(line)
                        
            freq_sum = np.zeros(6)
                        
            for k,v in finder.ngram_fd.items():
                 
                isthere = 0
                for i,lang in enumerate(lang_name):
                    
                    for key,f in model[i]:
                        
                        if k == key:                            
                            freq_sum[i] = freq_sum[i] + (f*10000)/no_of_bigms[i]
                            isthere = 1
                            break
                    if isthere == 0:
                        freq_sum[i] = freq_sum[i] + 1/no_of_bigms[i]
                #print k, freq_sum                
            max_val = freq_sum.max()
            index= freq_sum.argmax()
            #print l,lang_name[index],freq_sum
            if max_val != 0:                
                if lang_name[index] == lang_name[0]:
                    ep = ep + 1
                elif lang_name[index] == lang_name[1]:
                    gp = gp + 1
                elif lang_name[index] == lang_name[2]:
                    fp = fp + 1
                elif lang_name[index] == lang_name[3]:
                    ip = ip + 1
                elif lang_name[index] == lang_name[4]:
                    dp = dp + 1
                elif lang_name[index] == lang_name[5]:
                    sp = sp + 1
            else:
                cd = cd + 1
            #print "tp = ",tp,"fp = ",fp,"cd = ",cd, freq_sum
print ep," ",gp," ",fp," ",ip," ",dp," ",sp          








#identifier.set_languages(['en','it','hi'])

