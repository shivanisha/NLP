# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:54:50 2021

@author: Shivani Sharma
"""

# Auto summarising 
# downloading the article 
import urllib.request as urllib2

from bs4 import BeautifulSoup

articleURL  = "https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/"

page = urllib2.urlopen(articleURL).read().decode('utf8','ignore')
soup = BeautifulSoup(page,'lxml')

# print(soup)

# print(soup.find("article").text)

text = ''.join(map(lambda p: p.text , soup.find_all('article')))

text.replace("?", " ").encode('ascii', errors='replace')

# download the article 
def getTextWaPo(url):
    page = urllib2.urlopen(articleURL).read().decode('utf8','ignore')
    soup = BeautifulSoup(page,'lxml')
    text = ''.join(map(lambda p: p.text , soup.find_all('article')))
    return text.encode('ascii' , errors= 'replace' ).replace(b"?", b' ')

# preprocessing the text 

# text = getTextWaPo(articleURL)
#======================================================
# preprocess downloaded text 
#======================================================
import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize

sents = sent_tokenize(text)
word_sent = word_tokenize(text.lower()) 
#print(word_sents)
_stopwords = set(stopwords.words('english')+ list(punctuation))
# print(_stopwords)

word_sents=[word for word in word_sent]