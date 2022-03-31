# Author: Ankur Patel
# Course: CMSC-416-001-SP2022 Natural Language Processing
# Instructor: Bridgette Mckinnes

# A Python script which implements a Decision List classifier to 
#   perform word-sense disambiguation on given text. 
# The script will be tested against training files disambiguating
#   the term 'line' 
# Usage: python3 wsd.py training.txt test.txt model.txt > answers.txt

from cmath import log
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
    return cleaned_corpus

def get_context(corpus_string):
    context_lines = []
    # Extract each line of context 
    context_match = context_tagger.findall(corpus_string)
    for tup in context_match:
        context_lines.append(tup[1])
    return context_lines

# IN: one dictionary per sense, containing each unique word and its count
def train_model(corpus_string, model_file): 
    # dictionary containing word with determined sense and discriminator score
    log_dict = dict(float)
    
    # dictionary containing all unique words
    feature_list = list()
    
    model_dict = defaultdict(float)
    
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
        log_dict[feature] = math.abs(composite_log)
        if composite_log > 0:
            sense_dict[feature] = "phone"
        else:
            sense_dict[feature] = "product"
    
    # sort log dictionary by descending order of discrimination
    sorted_logs = dict(sorted(log_dict.items(), key= lambda x: x[1], reverse=True))
    
    # write model to file
    with open(model_file) as file:
        for feature in sorted_logs:
            file.write(feature, ": ", log_dict[feature], ", ", sense_dict[feature])
            
            
    

# Function to execute analysis on text file using trained model
def test_model(log_dict, sense_dict, test_string):
    clean_test = clean_text(test_string)
    test_lines = get_context(clean_test)
                    
    for i in range(len(test_lines)):
        line_list = test_lines[i].split()
        for line_word in line_list:
            for log_word in log_dict:
                if line_word == log_word:
                    sys.stdout.write("senseid= ", sense_dict[log_word])
                    break
                else:
                    continue
            break

if __name__ == "__main__":
    print('Welcome to wsd.py!')
    training_file = sys.argv[1]
    test_file = sys.argv[2]
    model_file = sys.argv[3]
    training_corpus_string = ""
    test_corpus_string = ""
    
    with open(training_file) as file:
        training_corpus_string = file.read()
    
    
    with open(test_file) as file:
        test_corpus_string = file.read()
