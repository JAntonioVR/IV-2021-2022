import sys

sys.path.append('./resenia')
import resenia, conjunto_resenias, aspectos
import os

dataset = os.getcwd() + "/data/Restaurant_Reviews.tsv"
review_set = conjunto_resenias.ConjuntoResenias(None)
review_set.carga_datos(dataset)


