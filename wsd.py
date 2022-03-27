# Author: Ankur Patel
# Course: CMSC-416-001-SP2022 Natural Language Processing
# Instructor: Bridgette Mckinnes

# A Python script which implements a Decision List classifier to 
#   perform word-sense disambiguation
# Usage: python3 wsd.py training.txt test.txt model.txt > answers.txt
from html.parser import HTMLParser

import sys
import pandas as pd
import xml.etree.ElementTree as ET
import re

# Helper class for parsing input text
def parse_text(corpus_string):
    sense_tagger = re.compile(r'(senseid=")(\S+)("/>)')
    head_tagger = re.compile(r'(<head>)(\S+)(</head>)')
    context_tagger = re.compile(r'(<context>\n)(.*)(\n</context>)')
    # Extract each line
        # Extract each sense 
        # Extract the head, 
        # Extract each surrounding word and add it to count
    # Produce log probabilities
    pass

def learn_model():
    # Extract each head and associate it with its sense
    # Extract words surrounding head and count their overall frequency
    pass

# Read input file, extract each head and disambiguate it
# For each <head> word, generate log probability 
def apply_model():
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
        
        
