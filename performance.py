import time
import random
import psutil
import tracemalloc

import wandb

from preprocess import *
from top_k_words import *


def measure_runtime(function, *args):
    start_time = time.time()
    function(*args)
    end_time = time.time()
    return end_time - start_time


def measure_cpu_usage(function, *args):
    process = psutil.Process()
    process.cpu_percent(interval=None)
    function(*args)
    time.sleep(1)
    cpu_usage = process.cpu_percent(interval=None)
    return cpu_usage


def measure_memory_usage(function, *args):
    tracemalloc.start()
    function(*args)
    _, memory_usage = tracemalloc.get_traced_memory()
    memory_usage *= 0.001024
    tracemalloc.stop()
    return memory_usage


def init_wanb_run(project_name, tokens, file_name):
    wandb.login()
    wandb.init(
        # set the wandb project where this run will be logged
        project=project_name,
        # track hyperparameters and run metadata
        config={"token size": f"{len(tokens)}", "dataset": file_name},
    )


def sorting_performance(tokens, k):
    token_tenth = int(round(len(tokens) / 10, 0))
    token_sizes = list(range(token_tenth, len(tokens), token_tenth))

    for size in token_sizes:
        tokens_subset = random.choices(
            tokens, k=size
        )  # Replace generate_tokens with your token generation code

        cpu_usage_sorting = measure_cpu_usage(sorting, tokens_subset, k)
        memory_usage_sorting = measure_memory_usage(sorting, tokens_subset, k)
        runtime_sorting = measure_runtime(sorting, tokens_subset, k)

        wandb.log(
            {
                "token size": size,
                "runtime_sorting": runtime_sorting,
                "cpu_usage_sorting": cpu_usage_sorting,
                "memory_usage_sorting": memory_usage_sorting,
            }
        )


def maxHeap_performance(tokens, k):
    token_tenth = int(round(len(tokens) / 10, 0))
    token_sizes = list(range(token_tenth, len(tokens), token_tenth))

    for size in token_sizes:
        tokens_subset = random.choices(
            tokens, k=size
        )  # Replace generate_tokens with your token generation code

        cpu_usage_maxHeap = measure_cpu_usage(maxHeap, tokens_subset, k)
        memory_usage_maxheap = measure_memory_usage(maxHeap, tokens_subset, k)
        runtime_maxheap = measure_runtime(maxHeap, tokens_subset, k)

        wandb.log(
            {
                "token size": size,
                "runtime_maxheap": runtime_maxheap,
                "cpu_usage_maxHeap": cpu_usage_maxHeap,
                "memory_usage_maxheap": memory_usage_maxheap,
            }
        )


def bucketSort_performance(tokens, k):
    token_tenth = int(round(len(tokens) / 10, 0))
    token_sizes = list(range(token_tenth, len(tokens), token_tenth))

    for size in token_sizes:
        tokens_subset = random.choices(
            tokens, k=size
        )  # Replace generate_tokens with your token generation code

        cpu_usage_bucketSort = measure_cpu_usage(bucketSort, tokens_subset, k)
        memory_usage_bucketsort = measure_memory_usage(bucketSort, tokens_subset, k)
        runtime_bucketSort = measure_runtime(bucketSort, tokens_subset, k)

        wandb.log(
            {
                "token size": size,
                "runtime_bucketSort": runtime_bucketSort,
                "cpu_usage_bucketSort": cpu_usage_bucketSort,
                "memory_usage_bucketsort": memory_usage_bucketsort,
            }
        )


if __name__ == "__main__":
    random.seed(1995)
    
    file_name = "dataset/data_2.5GB.txt"

    stopwords_file = "stopwords.txt"
    stopwords = get_stopwords(stopwords_file)

    k = 10

    tokens = tokenize_parallel_multiprocessing(file_name, stopwords, num_processes=36)

    init_wanb_run("data engineering", tokens, file_name)

    sorting_performance(tokens, k)
    maxHeap_performance(tokens, k)
    bucketSort_performance(tokens, k)
    
    wandb.finish()
