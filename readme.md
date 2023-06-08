# Text Processing Performance Measurement

This project measures the performance of different text processing algorithms such as sorting, maxHeap, and bucketSort. It provides insights into the runtime, CPU usage, and memory usage of these algorithms when applied to tokenizing and processing text data.

## Prerequisites

Make sure you have the following software installed on your system:

- Python 3.x
- `pip` package manager

## Setup

1. Clone the repository:

```bash
git clone [https://github.com/elenaliao1002/Performance-Analysis-Top-K-Frequent-Words](https://github.com/elenaliao1002/Performance-Analysis-Top-K-Frequent-Words)
cd Performance-Analysis-Top-K-Frequent-Words
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Download the required datasets and stopwords by running the `fetch_data.py` script:

```bash
python fetch_data.py
```

This script will download the necessary files and store them in the appropriate locations.

2. Preprocess the text data by running the `preprocess.py` script:

```bash
python preprocess.py
```

This script will tokenize the text data, remove stopwords and non-alphabetic characters, and generate a list of tokens.

3. Run the performance measurement by executing the `performance.py` script:

```bash
python performance.py
```

This script will measure the performance of sorting, maxHeap, and bucketSort algorithms on the tokenized data. It will log the runtime, CPU usage, and memory usage metrics using Weights & Biases (wandb) for analysis and visualization.

4. Monitor the performance metrics

During the execution of the `performance.py` script, the performance metrics will be logged to the Weights & Biases dashboard. You can access the dashboard by logging into your Weights & Biases account.

## Customization

You can customize the code according to your requirements:

- Modify the URLs in `fetch_data.py` to download your own datasets or stopwords.
- Adjust the number of processes in `preprocess.py` to parallelize the tokenization process.
- Modify the `k` value in `top_k_words.py` to change the number of top words to retrieve.
- Customize the performance measurement functions in `performance.py` to suit your needs.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to reach out if you have any questions or issues running the code.
