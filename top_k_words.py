import sys
import heapq
from collections import Counter

from preprocess import *


def sorting(tokens, k) -> list:
    word_count = Counter(tokens)

    top_k_words = sorted(word_count.keys(), key=lambda w: -word_count[w])[:k]

    return top_k_words


def maxHeap(tokens, k) -> list:
    word_count = Counter(tokens)

    max_heap = [(-count, word) for word, count in word_count.items()]
    heapq.heapify(max_heap)

    top_k_words = []
    for i in range(k):
        top_k_words.append(heapq.heappop(max_heap)[1])

    return top_k_words


def bucketSort(tokens, k) -> list:
    word_count = Counter(tokens)
    
    max_count = max(word_count.values())

    bucket = [[] for _ in range(max_count + 1)]
    for word, count in word_count.items():
        bucket[count].append(word)

    top_k_words = []
    for i in range(max_count, 0, -1):
        top_k_words.extend(bucket[i][: k - len(top_k_words)])
        if len(top_k_words) >= 10:
            break

    return top_k_words


if __name__ == "__main__":
    file_name = sys.argv[1]
    
    stopwords_file = 'stopwords.txt'
    stopwords = get_stopwords(stopwords_file)

    k = 10
    
    tokens = tokenize_parallel_multiprocessing(file_name, stopwords, num_processes=36)
    
    algo = sys.argv[2]
    
    if algo == "sorting":
        sorting(tokens, k)
    elif algo == "maxHeap":
        maxHeap(tokens, k)
    elif algo == "bucketSort":
        bucketSort(tokens, k)
    else:
        raise Exception("Please choose an algo: sorting, maxHeap, bucketSort")