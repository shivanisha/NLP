# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:58:54 2021

@author: Shivani Sharma
"""

import nltk
# nltk.download('punkt')
#nltk.download('stopwords')
text ="Marry had a little lamb. Her fleece was white as snow"
from nltk.tokenize import word_tokenize, sent_tokenize

sents=sent_tokenize(text)
# print(sents) # sentences has been break

words = [word_tokenize(sent) for sent in sents]
print(words)

from nltk.corpus import stopwords
from string import punctuation
customStopWords = set(stopwords.words('english')+list(punctuation))

wordsWOStopwords =[word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)

from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
print(sorted(finder.ngram_fd.items()) )