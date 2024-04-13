# **Exploratory-Data-Analysis Toolkit using Language Models**
Chat with Pandas DataFrame via 🦜LangChain using multiple models and data formats.. <br/>
This repository contains an application built with Streamlit that utilizes language models to perform Exploratory Data Analysis (EDA) on datasets. <br/>
The application allows users to upload their datasets and interactively explore the data using various language models.


## Summary of the repository

1-	Upload Data: Users can upload their dataset files (in CSV, Excel, or other supported formats) using the sidebar.

2-	Data Summary: After uploading the dataset, the application provides a summary of the data including: <br/>
•	Initial data sample <br/>
•	Column descriptions <br/>
•	Column types <br/>
•	Missing values <br/>
•	Duplicate values <br/>
•	Outlier values <br/>
•	Descriptive metrics (e.g., mean, median, min, max) <br/>

3-	Data Visualization: Users can select a variable of interest and examine it through visualizations such as bar charts.

4-	Ask Questions: Users can ask questions about the dataset, and the language model will provide answers based on the data.

## Installation
To use the scripts in this repository, you'll need to install the required dependencies. <br/>
You can install them using pip: <br/>
pip install -r requirements.txt

## Usage
Summarize Data
The summarize_data function provides a summary of the dataset, including an initial data sample, column descriptions, column types, missing values, duplicate values, outlier values, and essential metrics. <br/>
from data_analysis_toolkit import summarize_data <br/>
data_summary = summarize_data(data_file)

## Get DataFrame
The get_dataframe function retrieves the dataset as a Pandas DataFrame.<br/>
from data_analysis_toolkit import get_dataframe <br/>
df = get_dataframe(data_file)

## Analyze Graph
The analyze_graph function generates a graph for a specified variable in the dataset. <br/>
from data_analysis_toolkit import analyze_graph <br/>
graph_response = analyze_graph(data_file, variable_of_interest)

## Ask Question
The ask_question function allows you to ask a question about the dataset, and the language model will provide an answer. <br/>
from data_analysis_toolkit import ask_question <br/>
AI_Response = ask_question(data_file, question)

## Supported File Formats
-	CSV <br/>
-	Excel (XLS, XLSX, XLSM, XLSB, ODF, ODS, ODT)

## Language Models
The scripts utilize various language models for data analysis tasks:<br/>
•	OpenAI's GPT-3.5 <br/>
•	Anthropic's Claude <br/>
•	Google's Generative AI <br/>
•	Cohere's Chat Models <br/>

## Run the Streamlit application
streamlit run app.py

## Configuration
Before using the scripts, make sure to set up your API keys for the language models by creating a .env file and adding the following variables:

## makefile
-	openai_apikey=YOUR_OPENAI_API_KEY <br/>
-	anthropic_apikey=YOUR_ANTHROPIC_API_KEY <br/>
-	google_apikey=YOUR_GOOGLE_API_KEY <br/>
-	cohere_apikey=YOUR_COHERE_API_KEY

## License
This project is licensed under the MIT License - see the LICENSE file for details.



