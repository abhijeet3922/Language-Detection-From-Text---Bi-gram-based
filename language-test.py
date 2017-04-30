# -*- coding: utf-8 -*-

from nltk.collocations import BigramCollocationFinder
import re
import codecs
import numpy as np
import string
        
def test_language(path,language,total):
    ep = 0
    gp = 0
    fp = 0
    ip = 0
    dp = 0
    sp = 0
    cd = 0
    lang_name = ["english","german","french","italian","dutch","spanish"]
    root = "C:\\Users\\Charlie\\Desktop\\language-id-text\\lid-scratch\\language_models\\gram-based\\"
    model = [np.load(root+lang+".npy") for lang in lang_name]
    
    with codecs.open(path,"r","utf-8") as filep:
        translate_table = dict((ord(char), None) for char in string.punctuation)
        for l,line in enumerate(filep):
            
            line = " ".join(line.split()[1:])
            line = line.lower()
            line = re.sub(r"\d+", "", line)
            line = line.translate(translate_table)
            #print line
            #words = nltk.word_tokenize(line)
            
            finder = BigramCollocationFinder.from_words(line)
                        
            freq_sum = np.zeros(6)
                        
            for k,v in finder.ngram_fd.items():
                #print k,v 
                isthere = 0
                for i,lang in enumerate(lang_name):
                    
                    for key,f in model[i]:
                        if k == key:                            
                            freq_sum[i] = freq_sum[i] + (f*10000)/total[i]
                            isthere = 1
                            break
                    if isthere == 0:
                        freq_sum[i] = freq_sum[i] + 1
                                
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
            
    
    
if __name__ == "__main__":
    root = "C:\\Users\\Charlie\\Desktop\\language-id-text\\lid-scratch\\data\\test\\"
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
    
    
    
    train_lang_path = ["eng_news_2015_10K\\eng_news_2015_10K-sentences.txt","deu_news_2015_10K\\deu_news_2015_10K-sentences.txt","fra_news_2010_10K-text\\fra_news_2010_10K-sentences.txt","ita_news_2010_10K-text\\ita_news_2010_10K-sentences.txt","nld_wikipedia_2016_10K\\nld_wikipedia_2016_10K-sentences.txt","spa_news_2011_10K\\spa_news_2011_10K-sentences.txt"]
    for i,p in enumerate(train_lang_path):
        print "Testing of ",lang_name[i]
        test_language(root+p,lang_name[i],no_of_bigms)
        
        
   