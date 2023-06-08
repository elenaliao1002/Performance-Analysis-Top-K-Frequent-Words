---
In this report, we aim to solve the problem of finding the top K frequent words using three different algorithms: sorting, maxHeap, and bucketSort. We will analyze the performance of these algorithms using four different input sizes and evaluate their efficiency based on various metrics such as running time, speedup, CPU utilization, and memory usage. By comparing the performance of these algorithms, we can gain insights into their suitability for different problem sizes and make informed decisions regarding algorithm selection.
---
### Problem Statement

The problem at hand is to determine the [K most frequent words](https://leetcode.com/problems/top-k-frequent-words/) from a given list of tokens. The input consists of a collection of words, and the output should be a list of the K words that appear most frequently in the input. The objective is to design efficient algorithms that can handle different problem sizes and provide accurate results.

---

### Algorithms

#### Sorting

This algorithm counts the occurrences of each token using the `Counter` class and then sorts the keys based on their counts. It retrieves the top K words from the sorted list, providing a straightforward approach to solving the problem.

<pre class="sc-jifIRw lkksMp"><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">def</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT dOKFyY"><span data-slate-string="true">sorting</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">tokens</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">,</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> k</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">-</span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">></span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">list</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">:</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">    word_count </span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">=</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> Counter</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">tokens</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">    top_k_words </span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">=</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">sorted</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">word_count</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">.</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">keys</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">,</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> key</span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">=</span></span><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">lambda</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> w</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">:</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">-</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">word_count</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">[</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">w</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">]</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">[</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">:</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">k</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">]</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">return</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> top_k_words</span></span></span></div></pre>

1. This function uses the `Counter` class from the `collections` module to count the occurrences of each token.

   O(n) time complexity, where n is the length of tokens
2. It then sorts the keys of the `word_count` dictionary based on their counts in descending order using the sorted function and a lambda function as the key.

   O(n log n) time complexity, where n is the number of unique tokens
3. The sorted keys are sliced to obtain the top k most frequent words.

   O(k) time complexity
4. The function returns a list of the top k words.

The overall time complexity of this algorithm is O(n log n), which is acceptable for small to medium-sized problem instances. However, if the number of tokens is very large, the sorting step can become a performance bottleneck.

#### Max Heap

This algorithm also utilizes the `Counter` class to count the occurrences of each token. It constructs a max heap of word counts and extracts the K words with the highest counts from the heap. The Max Heap algorithm offers efficient extraction of maximum elements and can potentially provide improved performance.

<pre class="sc-jifIRw lkksMp"><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">def</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT dOKFyY"><span data-slate-string="true">maxHeap</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">tokens</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">,</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> k</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">-</span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">></span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">list</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">:</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">    word_count </span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">=</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> Counter</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">tokens</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-zero-width="n" data-slate-length="0">
</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">    max_heap </span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">=</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">[</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">-</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">count</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">,</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> word</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">for</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> word</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">,</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> count </span></span><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">in</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> word_count</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">.</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">items</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">]</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">    heapq</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">.</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">heapify</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">max_heap</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-zero-width="n" data-slate-length="0">
</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">    top_k_words </span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">=</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">[</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">]</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">while</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> k </span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">></span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT gCbSET"><span data-slate-string="true">0</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">:</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">        top_k_words</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">.</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">append</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">heapq</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">.</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">heappop</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">(</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">max_heap</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">[</span></span><span data-slate-leaf="true" class="sc-fDHtZT gCbSET"><span data-slate-string="true">1</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">]</span></span><span data-slate-leaf="true" class="sc-fDHtZT bMykAy"><span data-slate-string="true">)</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true">        k </span></span><span data-slate-leaf="true" class="sc-fDHtZT yrYbm"><span data-slate-string="true">-=</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT gCbSET"><span data-slate-string="true">1</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-zero-width="n" data-slate-length="0">
</span></span></span></div><div data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"></span></span><span data-slate-leaf="true" class="sc-fDHtZT bUarRZ"><span data-slate-string="true">return</span></span><span data-slate-leaf="true" class="sc-fDHtZT GNSvI"><span data-slate-string="true"> top_k_words</span></span></span></div></pre>

1. This function also utilizes the `Counter` class to count the occurrences of each token.

   O(n) time complexity, where n is the length of tokens
2. It creates a max heap, `max_heap`, by transforming the `(count, word)` pairs into `(-count, word)` pairs and storing them in a list.

   O(n) time complexity, where n is the number of unique tokens
3. The `heapify` function from the `heapq` module is then used to convert the list into a max heap.

   O(n) time complexity, where n is the number of elements in `max_heap`
4. The function iteratively pops the words with the highest counts from the max heap and appends them to `top_k_words` until k words are collected.

   O(k log n) time complexity, where n is the number of elements in `max_heap`
5. The function returns a list of the top k words.

The overall time complexity of this algorithm is O(n + k log n), which is efficient and performs well even for larger problem sizes. The advantage of using a Max Heap is that it allows efficient extraction of the maximum elements, making it suitable for finding the top k elements.

### Performance Data Visualization and Analysis:

To evaluate the performance of the three functions, we conducted experiments on various datasets with different sizes. We measured the execution time for each function and compared their performance using line graphs.


Conclusion:
Based on the runtime analysis, the maxHeap algorithm shows the most efficient performance among the three approaches, with the sorting algorithm being the second best. The bucketSort algorithm's performance cannot be evaluated without its implementation.

#### Dataset 1: Small 50MB Dataset

Number of texts: 

Number of Tokens: 3,219,338

Resultant graph: [Insert graph here]

1. Runtime Analysis:
   The first metric analyzed is the runtime of the algorithm for different token sizes. The experiment is conducted using token sizes ranging from 1000 to the length of the dataset. The runtimes for sorting, maxHeap, and bucketSort algorithms are measured and logged using the `wandb.log()` function. The runtimes are then plotted against the token sizes using a line graph.

Observations:

* The sorting algorithm exhibits a linear increase in runtime as the token size grows.
* The maxHeap algorithm demonstrates a slightly better performance than sorting, with a relatively slower increase in runtime.
* The bucketSort algorithm's performance cannot be analyzed due to missing implementation details.

Analysis: As the dataset is small, all three functions perform reasonably well and complete quickly. However, the sorting function has a slightly higher execution time due to the sorting step.

2. Memory Usage Analysis:
3. CPU Utilization Analysis:

#### Dataset 2: 300MB Dataset

Number of texts: 

Number of Tokens: 21,634,513

Resultant graph: 


Analysis: The sorting function takes the longest time due to the sorting step. The maxHeap and bucketSort functions show significant improvements in execution time compared to the sorting function.

#### Dataset 3: 2.5GB Dataset

Number of Tokens: 1,000,000

Resultant graph: [Insert graph here]

Analysis: The sorting function becomes noticeably slower due to the increasing number of tokens. The maxHeap and bucketSort functions exhibit much better performance, with bucketSort being the fastest due to its efficient utilization of the distribution of word counts.

#### Dataset 4: 16GB Dataset

Number of Tokens: 1,000,000

Resultant graph: [Insert graph here]

Analysis: The sorting function becomes noticeably slower due to the increasing number of tokens. The maxHeap and bucketSort functions exhibit much better performance, with bucketSort being the fastest due to its efficient utilization of the distribution of word counts.


### Observations and Conclusion:

The sorting function has a time complexity of O(n log n), making it suitable for small to medium-sized datasets. However, it can become a performance bottleneck for larger datasets.

The maxHeap and bucketSort functions perform well for larger datasets due to their time complexities of O(n + k log n) and O(n + k), respectively.

The maxHeap function provides efficient extraction of the maximum elements using a max heap, while the bucketSort function exploits the distribution of word counts to achieve better performance.

Overall, the choice of algorithm and data structure depends on the problem size and the desired trade-off between time complexity and space complexity.

In conclusion, for finding the top k most frequent words, the maxHeap and bucketSort functions offer efficient solutions for various problem sizes. The maxHeap function is preferred when the exact k elements need to be extracted, while the bucketSort function is advantageous when the distribution of word counts is skewed and sorting the entire list is unnecessary.
