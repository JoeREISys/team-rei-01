# Project Title

Transforming EIA with Knowledge Graphs and NLP  
## Project Overview

This project involves scraping EIA to gather all HTML files, PDFs, and other publicly available data. Once the data is collected, it undergoes extensive processing to extract valuable information.

### Table of Contents

- [Data Collection and Processing](#data-collection-and-processing)
- [Knowledge Graph Creation](#knowledge-graph-creation)
- [RDF Store Population](#rdf-store-population)
- [Querying and Response Generation](#querying-and-response-generation)
- [Summary](#summary)

## Data Collection and Processing

### Web Scraping
The website is thoroughly scraped to retrieve all HTML files, PDFs, and other relevant documents.

### Data Processing
The collected data is processed to extract useful information. This involves:
- **HTML Parsing**: Unnecessary HTML tags are removed, and table tags are converted into natural language text using advanced language models such as ChatGPT.
- **Text Cleaning**: The text is cleaned by removing stop words, trimming extra lines, and eliminating non-ASCII characters.

## Knowledge Graph Creation

Each webpage undergoes the above processing steps to distill useful information. This information is then converted into a knowledge graph by leveraging a language model and predefined ontologies. The language model categorizes the extracted text into a structured knowledge graph format, which is subsequently converted into Turtle files.

## RDF Store Population

The generated Turtle files are sent to an endpoint that ingests them and populates an RDF store. This RDF store comprises various entities and their relationships, adhering to the triple statements format.

## Querying and Response Generation

When a user submits a query in natural language:
1. **Query Conversion**: The natural language query is converted into a SPARQL query using ChatGPT, based on the predefined ontologies.
2. **Data Retrieval**: The SPARQL query is executed against the RDF database to retrieve the relevant data.
3. **Response Generation**: The retrieved data is transformed into natural language text, making it understandable for users. This transformation is performed by ChatGPT.

## Summary

This project streamlines the process of converting web data into a structured knowledge graph and provides an efficient way to query this data using natural language. It leverages cutting-edge language models to ensure the extracted and queried information is accurate and easily comprehensible.

## Getting Started

### Dependencies

* Python
* SparQL
* fitz  # PyMuPDF
* BeautifulSoup
* requests
* chardet
* re
* spacy
* knowledge_graph_maker
* os
* lambda labs
* 
### Installing

* pip install them
* Any modifications needed to be made to files/folders


### Resources

* https://platform.openai.com/docs/guides/text-generation
* https://towardsdatascience.com/text-to-knowledge-graph-made-easy-with-graph-maker-f3f890c0dbe8
* https://towardsdatascience.com/how-to-convert-any-text-into-a-graph-of-concepts-110844f22a1a
* NoIp
* Lambda CLoud
* AWS EC2


### URLs:

* https://ec2-34-222-196-161.us-west-2.compute.amazonaws.com:9999/blazegraph/
* https://eiagovkb.hopto.org/retrieve




