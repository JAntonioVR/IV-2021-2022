import pandas as pd

import sys
sys.path.append('./resenia')
import resenia, conjunto_resenias, aspectos

import os

cwd = os.getcwd() + "/data"
dataset = pd.read_csv(cwd + "/Restaurant_Reviews.tsv", delimiter='\t')

list_reviews = []

for index, row in dataset.iterrows():
    current_review = resenia.Resenia(row['Review'], row['Restaurant_ID'], row['Stars'], None)
    list_reviews.append(current_review)


review_set = conjunto_resenias.ConjuntoResenias(list_reviews)

