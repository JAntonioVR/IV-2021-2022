import pandas as pd

import os

cwd = os.getcwd() + "/data"  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


dataset = pd.read_csv(cwd + "/Restaurant_Reviews.tsv", delimiter='\t')
print(dataset.head())