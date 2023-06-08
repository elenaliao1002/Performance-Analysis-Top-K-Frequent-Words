import string
import tracemalloc
from multiprocessing import Pool
from collections import Counter


def get_stopwords(stopwords_file) -> list:
    stopwords = []
    with open(stopwords_file, "r") as f:
        for line in f:
            stopwords.append(line.replace("\n", ""))
    return stopwords


def process_line(line, stopwords):
    line = line.strip().lower()
    words = line.split(" ")
    words = [w for w in words if w not in stopwords and w.isalpha()]
    return words


def tokenize_parallel_multiprocessing(file_name, stopwords, num_processes=4):
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, remove stop words,
    strip digits.
    """
    with open(file_name, "r") as f:
        lines = f.readlines()

    with Pool(processes=num_processes) as pool:
        results = pool.starmap(process_line, [(line, stopwords) for line in lines])

    tokens = [token for words in results for token in words]
    return tokens
