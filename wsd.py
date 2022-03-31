# Author: Ankur Patel
# Course: CMSC-416-001-SP2022 Natural Language Processing
# Instructor: Bridgette Mckinnes

# A Python script which implements a Decision List classifier to 
#   perform word-sense disambiguation on given text. 
# The script will be tested against training files disambiguating
#   the term 'line' 
# Usage: python3 wsd.py training.txt test.txt model.txt > answers.txt

import math
from multiprocessing import context
import sys
from collections import defaultdict
from numpy import double
import pandas as pd
import re

sense_tagger = re.compile(r'(senseid=")(.*)("/>)')
head_tagger = re.compile(r'(<head>)(\S+)(</head>)')
context_tagger = re.compile(r'(<context>\n)(.*)(\n</context>)')

# Helper function for generating counts of each unique word
#  from a sentence-length string
# IN: 
#   corpus_line: single line of text
#   corpus_dict: dictionary to be updated
# OUT: dictionary of form {word, sense: count}
def count_words_sense(corpus_line, corpus_dict):
    line_data = corpus_line.split()
    for word in line_data:
        if word not in corpus_dict:
            corpus_dict[word] = 1.0
        else:
            corpus_dict[word] += 1.0
    return corpus_dict

def count_words(corpus_line, corpus_list):
    line_data = corpus_line.split()
    for word in line_data:
        if word not in corpus_list:
            corpus_list.append(word)

# Helper function for removing extraneous data from input texts
# In: raw string from file
# Out: list of lines
def clean_text(corpus_string):
    cleaned_corpus = re.sub(r'<s>|</s>|<p>|<@>|</p>', " ", corpus_string)

def get_sense(corpus_string):
    pass

def get_context(corpus_string):
    context_lines = []
    # Extract each line of context 
    context_match = context_tagger.findall(corpus_string)
    for tup in context_match:
        context_lines.append(tup[1])
    return context_lines

# Helper class for parsing input text
def parse_text(corpus_string, model_file):
        
    tag_cleaner = re.compile(r'<s>|</s>|<p>|<@>|</p>')
    
    # Remove non-context tags and words
    corpus_string = tag_cleaner.sub(" ", corpus_string)
    # corpus_string = head_tagger.sub(" ", corpus_string)
    
    # Create dictionary of phone sense words
    phone_senser = defaultdict(int)
    phone_count = 0
    # Create dictionary of product sense words
    product_senser = defaultdict(int)
    product_count = 0
    # Extract sense data per line 
    sense_lines = sense_tagger.findall(corpus_string)
    sense_words = []
    for tup in sense_lines:
        sense_words.append(tup[1])
        
    # Remove <head> words from context data
    corpus_string = head_tagger.sub(" ", corpus_string)
        
    context_lines = []
    # Extract each line of context 
    context_match = context_tagger.findall(corpus_string)
    for tup in context_match:
        context_lines.append(tup[1])
            
    # Iterate over sense data and context lines to 
    #  create each 'bag of words'
    for i in range(len(sense_lines)):
        if sense_words[i] == "product":
            product_count += 1
            count_words_sense(context_lines[i], product_senser)
        elif sense_words[i] == "phone":
            phone_count += 1
            count_words_sense(context_lines[i], phone_senser)
        
    learn_model(product_senser, product_count, phone_senser, phone_count, model_file)
    

# IN: one dictionary per sense, containing each unique word and its count
def train_model(corpus_string, model_file):
    #  dictionary containing each word, its sense, and count
    model_dict = defaultdict(double)
    
    # dictionary containing word with determined sense and discriminator score
    log_dict = defaultdict(double)
    
    # dictionary containing all unique words
    feature_list = list()
    
    # separate dictionaries for each sense
    phone_sense = defaultdict(int)
    product_sense = defaultdict(int)
    
    # dictionary containing each word and its determined sense
    sense_dict = dict()
    
    # Total counts for each sense
    product_count = 0.0
    phone_count = 0.0
    
    # Create a list for sense and context for each line
    sense_list = []
    context_list = []
    
    # Pull each sense word
    sense_matches = sense_tagger.findall(corpus_string)
    for tup in sense_matches:
        sense_list.append(tup[1])
    # Remove <head>s from context
    context_string = head_tagger.sub(" ", corpus_string)
    # Split corpus along each <context> line
    context_matches = context_tagger.findall(context_string)
    for tup in context_matches:
        context_list.append(tup[1])
        
    # Generate counts for each word for each given sense
    for i in range(len(sense_list)):
        # count_words_sense(context_list[i], model_dict, sense_list[i])
        if sense_list[i] == "product":
            product_count += 1.0
            count_words_sense(context_list[i], product_sense)
        elif sense_list[i] == "phone":
            phone_count += 1.0
            count_words_sense(context_list[i], phone_sense)
        count_words(context_list[i], feature_list)
        
    # Calculate log-likelihood of each word and assign it a sense 
    for feature in feature_list:
        if feature in product_sense:
            product_likelihood = product_sense[feature]/product_count
        else:
        # if feature is only in phone sense 
            product_likelihood = 1.0/product_count
        if feature in phone_sense:
            phone_likelihood = phone_sense[feature]/phone_count
        else:
            # if feature is only in product sense
            phone_likelihood = 1.0/phone_count
           
        composite_log = math.log(product_likelihood/phone_likelihood) 
        log_dict[feature] = composite_log
        if composite_log > 0:
            sense_dict[feature] = "phone"
        else:
            sense_dict[feature] = "product"
    
            
    sorted_model_dict = sorted(model_dict, key=math.abs(model_dict.items()))


def test_model():
    pass

# Generate sense probabilities for each word and 
# 
def learn_model(prod_sense, prod_count, phone_sense, phone_count, model_file):

    # Associate each context word with its sense
    
    phone_prob = defaultdict(double)
    product_prob = defaultdict(double)
    
    # Calculate log-likelihood for each context word
    #  and record in model file
    with open(model_file) as file:
        for word in prod_sense:
            product_prob[word] = math.log(prod_sense[word])/math.log(prod_count)
            file.write(word + ": " + product_prob[word] + "\n")
        
        for word in phone_sense:
            phone_prob[word] = math.log(phone_sense[word])/math.log(phone_count)
            file.write(word + ": " + phone_prob[word] + "\n")
    
    # Calculate probabilities for each context word 
    
    # Extract words surrounding head and count their overall frequency

# Read input file, extract each head and disambiguate it
# For each <head> word, generate log probability 
def apply_model(product_log, phone_log, test_string):
    sense_output = []
    sense_count = 0
    
    phone_vector = 0
    product_vector = 0
    
    # Compare probability of each context word 
    for line in test_string:
        word_list = line.split()
        for word in word_list:
            if word in product_log:
                if word in phone_log:
                    if(product_log[word] < phone_log[word]):
                        phone_vector += 1
                    else:
                        product_vector += 1
            elif word in phone_log:
                phone_vector += 1
        if(phone_vector > product_vector):
            sense_output[sense_count] = "phone"
            sense_count += 1
        else:
            sense_output[sense_count] = "product"
            sense_count += 1



if __name__ == "__main__":
    print('Welcome to wsd.py!')
    training_file = sys.argv[1]
    test_file = sys.argv[2]
    model_file = sys.argv[3]
    training_corpus_string = ""
    test_corpus_string = ""
    
    with open(training_file) as file:
        training_corpus_string = file.read()
    
    parse_text(training_corpus_string)
    
    with open(test_file) as file:
        test_corpus_string = file.read()
    
    
    # Attempt to create html parser 
    # parser = WordSenseParser()
    # parser.feed(training_corpus_string)
        
        
