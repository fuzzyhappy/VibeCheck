import os
import urllib.parse
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import string
import re

def process(s):
    # converts to lowercase
    s = s.lower()
    # removes URLs
    s = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", s).split())
    # removes punctuation
    s = re.sub(r'[^\w\s]', '', s)
    # removes stop words
    s = " ".join([word for word in nltk.tokenize.word_tokenize(s) if not word in stopwords.words("english")])
    # converts words to root words (stemming)
    porter = PorterStemmer()
    s = " ".join([porter.stem(word) for word in nltk.tokenize.word_tokenize(s)])
    # removes usernames
    s = " ".join(word for word in nltk.tokenize.word_tokenize(s) if not word.startswith("@") and len(word) > 1)
    # removes three-char repitions
    s = re.compile(r"(.)\1{2,}").sub(r"\1\1", s)
    return s
