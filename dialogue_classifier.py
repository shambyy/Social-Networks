import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import os
import json
import datetime
import csv
import numpy as np
import time
import string

def main():
    
    #stemmer = LancasterStemmer()
    # raw_training_data = get_raw_training_data('dialogue_data.csv')
    # print(stemmer.stem("swimming")) # >> swim
    #print(stemmer.stem("red")) # >> run

    raw_training_data = get_raw_training_data('dialogue_data.csv')
    #words = ['red', 'pink', 'running']
    #preprocess_words(words, stemmer=LancasterStemmer())

    with open('dialogue_data.csv', 'r') as fi:
        data = json.load(fi)
    list_tokens = []
    for sentence in data['sentence']:
        single_dict = {sentence['person']: sent_tokenize(sentence['sentence'])}
        print(single_dict)
  

def get_raw_training_data(filename):
    # open a CSV file and extract its data into list ds

    file = open(filename, 'r')
    training_data = []
    
    for line in file:
        line = line.lower()
        k, v = line.strip().split('","')
        mini_d = {}
        mini_d["person"] = k
        mini_d["sentence"] = v
        training_data.append(mini_d)
    
    return training_data

def organize_raw_training_data(raw_training_data, stemmer):
    # iterate through each element of training_data list (fun() above)


    """tok_sents = [word_tokenize(el) for el in raw_training_data]
    for el in tok_sents:
        print(el)"""
    pass

def preprocess_words(words, stemmer):
    # takes in list of words
    stemmer = LancasterStemmer()
    #words = ['red', 'pink.', '?pink', 'running', '!!']
    stemmed_words = []

    for word in words:
        stemmed_word = stemmer.stem(word)
        stemmed_words.append(stemmed_word)

    # remove unwanted tokens like ?
    no_pun = []
    
    for word in stemmed_words:
        for char in word:
            if char in string.punctuation:
                word = word.replace(char, "")
        no_pun.append(word)

    #singles_only = list(set(no_pun))
    singles_only = [i for n, i in enumerate(no_pun) if i not in no_pun[:n]]
    #this could cause an issue - maybe don't just do a ist of set
    # could result in dif outputs
    #!!!! do list comp and enumeration

    # will leave '' in the list if only punctuation  

    return singles_only
     
if __name__ == "__main__":
    main()