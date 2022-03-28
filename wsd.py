# Author: Ankur Patel
# Course: CMSC-416-001-SP2022 Natural Language Processing
# Instructor: Bridgette Mckinnes

# A Python script which implements a Decision List classifier to 
#   perform word-sense disambiguation on given text. 
# The script will be tested against training files disambiguating
#   the term 'line' 
# Usage: python3 wsd.py training.txt test.txt model.txt > answers.txt
from html.parser import HTMLParser
from signal import default_int_handler

import sys
from typing import DefaultDict
import pandas as pd
import re

# Helper class for parsing input text
def parse_text(corpus_string):
    sense_tagger = re.compile(r'(senseid=")(\S+)("/>)')
    head_tagger = re.compile(r'(<head>)(\S+)(</head>)')
    context_tagger = re.compile(r'(<context>\n)(.*)(\n</context>)')
    
    tag_cleaner = re.compile(r'<\?s>')
    
    # Remove non-context tags and words
    corpus_string = tag_cleaner.sub(" ", corpus_string)
    corpus_string = head_tagger.sub(" ", corpus_string)
    
    # Create dictionary of phone sense words
    phone_senser = DefaultDict()
    # Create dictionary of product sense words
    product_senser = DefaultDict()
    
    # Extract contextual words 
    context_lines = context_tagger.findall(corpus_string)
    
    # Extract sense data per line 
    sense_lines = sense_tagger.findall(corpus_string)
    
    
    
    # Extract each line
        # Extract each sense 
        # Extract the head, 
        # Extract each surrounding word and add it to count
    # Produce log probabilities
    pass

# Create sense model using separated text
# 
def learn_model(prod_sense, phone_sense):
    # Extract each head and associate it with its sense
    sense_data = ""
    current_head = ""

    # Associate each context word with its sense 
    phone_dict = ""
    product_dict = ""
    
    # Get count of each sense
    
    
        
    # Create dictionary of each word and its raw count 
    for word in sense_data:
        pass
    
    # for sense, word in context, sense:
    #   
    
    
    # Calculate log-likeluhood for each context word
    
    # Associate each head with either thing 

    # Sort each head into its corresponding sense 
    # Add each context word to the head structure
    # Calculate probabilities for each context word 
    
    # Extract words surrounding head and count their overall frequency

# Read input file, extract each head and disambiguate it
# For each <head> word, generate log probability 
def apply_model():
    # for word in context
    #  if word in phone_sense:
        #   calculate probability
    #  if word in product_sense:
        #  calculate probability
    # compare probs of each sense
    pass


if __name__ == "__main__":
    print('Welcome to wsd.py!')
    training_file = sys.argv[1]
    training_corpus_string = ""
    
    with open(training_file) as file:
        training_corpus_string = file.read()
    
    parse_text(training_corpus_string)
    
    # Attempt to create html parser 
    # parser = WordSenseParser()
    # parser.feed(training_corpus_string)
        
        
