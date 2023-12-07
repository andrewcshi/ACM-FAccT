# Academic Paper Analysis Tool

## Project Overview
This tool is designed to automate the extraction and analysis of academic papers, specifically from the 2023 ACM FAccT conference. It categorizes papers based on keywords related to four categories: transparency & explainability, fairness & bias, privacy & data governance, and security. The tool extracts the paper title, abstract, relevant keywords, authors, and affiliations from each paper and compiles this data into a CSV file.

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- `requests`
- `beautifulsoup4`
- `lxml`

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage

To run the tool, execute the `main.py` script:

```bash
python main.py
```