# Author: Ankur Patel
# Course: CMSC-416-001-SP2022 Natural Language Processing
# Instructor: Bridgette Mckinnes

# A Python script which implements a Decision List classifier to 
#   perform word-sense disambiguation
# Usage: python3 wsd.py training.txt test.txt model.txt > answers.txt

import sys
import pandas as pd
import xml.etree.ElementTree as ET
import re

def parse_text(corpus_string):
    corpus_string = re.sub(r'<@>', ' ', corpus_string)
    corpus_tree = ET.ElementTree(corpus_string)
    print(corpus_tree)

def learn_model():
    # Extract each head and associate it with its sense
    # Extract words surrounding head and count their overall frequency
    pass

if __name__ == "__main__":
    print('Welcome to wsd.py!')
    training_file = sys.argv[1]
    training_corpus_string = ""
    
    with open(training_file) as file:
        training_corpus_string = file.read()
        
    parse_text(training_corpus_string)
        
