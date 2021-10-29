import pandas as pd

import os
import csv

cwd = os.getcwd() + "/test"  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''
with open(cwd + "/Restaurant_Reviews.tsv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''
dataset = pd.read_csv(cwd + "/Restaurant_Reviews.tsv", delimiter='\t')
print(dataset.head())