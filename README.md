# Language-Detection-From-Text---Bi-gram-based

It uses Bi-gram language model and bi-gram frequency addition classifier for language identification task.

Trained over 6 languages namely German, English, Spanish, French, Italian and Dutch.

The original source of the text corpus is wortschatz leipzig corpora. Both the train and test corpus were taken from this corpora.
The training corpus consists of 30000 sentences from news/web domain. Test corpus 10000 unseen sentences from news/web domain.

Also, the chosen six languages were such that the same languages are present in the LIGA twitter dataset which consists of 9066 tweets.

Note : Directory path used for train and test corpus in code language-test.py, language-train.py and liga_test.py needs to be properly set accordingly.

# Installation 

You only need to install these (tested): 

1. Install Anaconda 64 bit Python 2.7 version. (https://www.continuum.io/downloads)
2. Install NLTK data using interactive installer (http://www.nltk.org/data.html)


Best thing would be to follow my blog-post for implementation and evaluation results. The description about the steps to build a text language detector from scratch can be read from the blog:

https://appliedmachinelearning.wordpress.com/2017/04/30/language-identification-from-texts-using-bi-gram-model-pythonnltk/
