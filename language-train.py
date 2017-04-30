# -*- coding: utf-8 -*-

from nltk.collocations import BigramCollocationFinder
import re
import codecs
import numpy as np
import string

def train_language(path,lang_name):
    words_all = []
    translate_table = dict((ord(char), None) for char in string.punctuation)
    with codecs.open(path,"r","utf-8") as filep:
         
        for i,line in enumerate(filep):            
                     
            line = " ".join(line.split()[1:])
            line = line.lower()           
            line = re.sub(r"\d+", "", line)
            
            if len(line) != 0:
                line = line.translate(translate_table)
                words_all += line
                words_all.append(" ")

    all_str = ''.join(words_all)
    all_str = re.sub(' +',' ',all_str)
    seq_all = [i for i in all_str]
    
    finder = BigramCollocationFinder.from_words(seq_all)
    finder.apply_freq_filter(5)
    bigram_model = finder.ngram_fd.viewitems()
    bigram_model = sorted(finder.ngram_fd.viewitems(), key=lambda item: item[1],reverse=True)
    print len(bigram_model)
    
    np.save(lang_name+".npy",bigram_model)
     
if __name__ == "__main__":
    root = "train\\"
    lang_name = ["french","english","german","italian","dutch","spanish"]
    train_lang_path = ["fra_news_2010_30K-text\\fra_news_2010_30K-sentences.txt","eng_news_2015_30K\\eng_news_2015_30K-sentences.txt","deu_news_2015_30K\\deu_news_2015_30K-sentences.txt","ita_news_2010_30K-text\\ita_news_2010_30K-sentences.txt","nld_wikipedia_2016_30K\\nld_wikipedia_2016_30K-sentences.txt","spa_news_2011_30K\\spa_news_2011_30K-sentences.txt"]
    for i,p in enumerate(train_lang_path):
        train_language(root+p,lang_name[i])
        
        
        
    
