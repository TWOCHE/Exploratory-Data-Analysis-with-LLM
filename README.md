# Exploratory-Data-Analysis Toolkit using Language Models
Chat with Pandas DataFrame via 🦜LangChain using multiple models and data formats..
This repository contains an application built with Streamlit that utilizes language models to perform Exploratory Data Analysis (EDA) on datasets. The application allows users to upload their datasets and interactively explore the data using various language models.


## Summary of the repository

1-	Upload Data: Users can upload their dataset files (in CSV, Excel, or other supported formats) using the sidebar.

2-	Data Summary: After uploading the dataset, the application provides a summary of the data including:
•	Initial data sample
•	Column descriptions
•	Column types
•	Missing values
•	Duplicate values
•	Outlier values
•	Descriptive metrics (e.g., mean, median, min, max)

3-	Data Visualization: Users can select a variable of interest and examine it through visualizations such as bar charts.

4-	Ask Questions: Users can ask questions about the dataset, and the language model will provide answers based on the data.

## Installation
To use the scripts in this repository, you'll need to install the required dependencies. You can install them using pip:
pip install -r requirements.txt

## Usage
Summarize Data
The summarize_data function provides a summary of the dataset, including an initial data sample, column descriptions, column types, missing values, duplicate values, outlier values, and essential metrics.
from data_analysis_toolkit import summarize_data
data_summary = summarize_data(data_file)

## Get DataFrame
The get_dataframe function retrieves the dataset as a Pandas DataFrame.
from data_analysis_toolkit import get_dataframe
df = get_dataframe(data_file)

## Analyze Graph
The analyze_graph function generates a graph for a specified variable in the dataset.
from data_analysis_toolkit import analyze_graph
graph_response = analyze_graph(data_file, variable_of_interest)

## Ask Question
The ask_question function allows you to ask a question about the dataset, and the language model will provide an answer.
from data_analysis_toolkit import ask_question
AI_Response = ask_question(data_file, question)

## Supported File Formats
•	CSV
•	Excel (XLS, XLSX, XLSM, XLSB, ODF, ODS, ODT)

## Language Models
The scripts utilize various language models for data analysis tasks:
•	OpenAI's GPT-3.5
•	Anthropic's Claude
•	Google's Generative AI
•	Cohere's Chat Models

## Run the Streamlit application
streamlit run app.py

## Configuration
Before using the scripts, make sure to set up your API keys for the language models by creating a .env file and adding the following variables:

## makefile
•	openai_apikey=YOUR_OPENAI_API_KEY
•	anthropic_apikey=YOUR_ANTHROPIC_API_KEY
•	google_apikey=YOUR_GOOGLE_API_KEY
•	cohere_apikey=YOUR_COHERE_API_KEY

## License
This project is licensed under the MIT License - see the LICENSE file for details.



