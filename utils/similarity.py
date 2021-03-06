import math
import numpy as np
from scipy import spatial
from nltk.corpus import wordnet as wn
from nltk.metrics import edit_distance


def cosine(v1, v2):
    """
            v1 and v2 are two vectors (can be list of numbers) of the same dimensions. Function returns the cosine distance between those
            which is the ratio of the dot product of the vectors over their RS.
    """
    v1 = np.array(v1)
    v2 = np.array(v2)

    return np.dot(v1, v2) / (np.sqrt(np.sum(v1**2)) * np.sqrt(np.sum(v2**2)))


def path(set1, set2):
    return wn.path_similarity(set1, set2)


def wup(set1, set2):
    return wn.wup_similarity(set1, set2)


def edit(word1, word2):
    if float(edit_distance(word1, word2)) == 0.0:
        return 0.0
    return 1.0 / float(edit_distance(word1, word2))

if __name__ == '__main__':
    from random import randint
    v1 = [randint(500, 1000) for i in range(1, 10)]
    v2 = [randint(1, 10) for i in range(1, randint(1, 10))]
    result = 1 - spatial.distance.cosine(v1, v2)
    print v1, v2
    print cosine(v1, v2)
    print result
