# Author: Ankur Patel
# Course: Natural Language Processing
#   CMSC-416-001-SP2022
#   Instructor: Dr. Bridget McInnes
# 
# Helper program for grading output of algorithm against 
#   a supplied key. 
#   IN: my_answers.txt 
#       - text file containing algorithm output
#   OUT:
#       - Overall accuracy with confusion matrix

import sys
import pandas as pd
from sklearn import metrics

def clean_text():
    pass

def confusion_stats(actual: list, predicted: list):
    actual_series = pd.Series(actual, name="Actual")
    predicted_series = pd.Series(predicted, name="Predicted")
    sys.stdout.write("Accuracy Score: " + str(metrics.accuracy_score(actual_series, predicted_series, "\n")))
    sys.stdout.write("Confusion Matrix\n" + str(pd.crosstab(actual_series, predicted_series)))
def regular_exp_parser():
    pass

if __name__ == '__main__':
    print("Welcome to scorer.py!")
    my_answer_file = sys.argv[1]
    answer_key_file = sys.argv[2]
    
    my_answer_string = ""
    answer_key_string = ""

    with open(my_answer_file) as file:
        file_string = file.read()
        my_answer_string = clean_text(file_string)
    

    with open(answer_key_file) as file:
        file_string = file.read()
        answer_key_string = clean_text(file_string)
    


