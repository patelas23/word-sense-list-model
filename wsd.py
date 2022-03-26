# Author: Ankur Patel
# Course: CMSC-416-001-SP2022 Natural Language Processing
# Instructor: Bridgette Mckinnes

# A Python script which implements a Decision List classifier to 
#   perform word-sense disambiguation
# Usage: python3 wsd.py training.txt test.txt model.txt > answers.txt

import sys
import xml.etree.ElementTree as ET
import pandas as pd

def parse_text(corpus_string):
    return pd.read_json(corpus_string)

def learn_model():
    pass

if __name__ == "__main__":
    print('Welcome to wsd.py!')
    training_file = sys.argv[1]
    training_corpus_string = ""
    
    with open(training_file) as file:
        training_corpus_string = file.read()
        
    print(parse_text(training_corpus_string))
