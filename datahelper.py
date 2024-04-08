import pandas as pd
from langchain_experimental.agents.agent_toolkits.pandas.base import (create_pandas_dataframe_agent, )
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatCohere
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai=os.getenv("openai_apikey")
my_key_anthropic=os.getenv("anthropic_apikey")
my_key_google=os.getenv("google_apikey")
my_key_cohere=os.getenv("cohere_apikey")

llm_gpt=ChatOpenAI(api_key=my_key_openai,model="gpt-3.5-turbo",temperature=0)
llm_claude_opus=ChatAnthropic(anthropic_api_key=my_key_anthropic,model_name="claude-3-opus-20240229",temperature=0)
llm_claude_haiku=ChatAnthropic(anthropic_api_key=my_key_anthropic,model_name="claude-3-haiku-20240307",temperature=0)
llm_claude=ChatAnthropic(anthropic_api_key=my_key_anthropic,model_name="claude-2.1",temperature=0)
llm_gemini=ChatGoogleGenerativeAI(google_api_key=my_key_google,temperature=0,model="gemini-pro")
llm_command=ChatCohere(cohere_api_key=my_key_cohere,temperature=0,model_name="command")

selected_llm=llm_gpt

# summarize data

def summarize_data(data_file):

    file_name = data_file.name
    file_extension = os.path.splitext(file_name)[1][1:].lower()

    if file_extension == 'csv':
        df = pd.read_csv(data_file, low_memory=True)
    elif file_extension in ['xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods','odt']:
        df = pd.read_excel(data_file,)
    else:
        print("Unsupported file format")


    pandas_agent=create_pandas_dataframe_agent(selected_llm,df,verbose=True,agent_executor_kwargs={"handle_parsing_errors":"True"})

    data_summary={}

    data_summary["initial_data_sample"]=df.head()

    data_summary["column_descriptions"]=pandas_agent.run("Make a table containing the columns in the data. The table should include the names of the columns and a brief explanation of the information they contain.Export this as a table.")

    data_summary["column_types"]=pandas_agent.run("Determine the dtypes of the variables. If the number of unique classes in a categorical or object variable type is greater than 10,except for variables containing id,title, message and data type timestamp, convert this variables to int or float data type. Make these changes permanently in the dataframe and export the final types of the variables as a table.")

    data_summary["missing_values"]=df.isnull().sum()
    #data_summary["missing_values"]=pandas_agent.run("Are there any missing values in this dataset? If so, how many are there? Answer with 'There are x missing values in this dataset'")

    data_summary["duplicate_values"]=pandas_agent.run("Are there any duplicate values in this dataset? If so, how many are there? Answer with 'There are x duplicate values in this dataset'")

    data_summary["outlier_values"]=pandas_agent.run("Are there any outlier values in this dataset? If so, how many are there? Answer with 'There are x outlier values in this dataset'")

    data_summary["essential_metrics"]=df.describe()

    return data_summary

# get dataframe

def get_dataframe(data_file):

    file_name = data_file.name
    file_extension = os.path.splitext(file_name)[1][1:].lower()

    if file_extension == 'csv':
        df = pd.read_csv(data_file, low_memory=True)
    elif file_extension in ['xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods','odt']:
        df = pd.read_excel(data_file)
    else:
        print("Unsupported file format")

    return df

# analyze graph

def analyze_graph(data_file,variable_of_interest):

    file_name = data_file.name
    file_extension = os.path.splitext(file_name)[1][1:].lower()

    if file_extension == 'csv':
        df = pd.read_csv(data_file, low_memory=True)
    elif file_extension in ['xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods','odt']:
        df = pd.read_excel(data_file)
    else:
        print("Unsupported file format")

    pandas_agent=create_pandas_dataframe_agent(selected_llm,df,verbose=True,agent_executor_kwargs={"handle_parsing_errors":"True"})

    graph_response=pandas_agent.run(f"Interpret the following variable in the data set with a graph suitable for the data type: {variable_of_interest} Don't refuse to interpret. You can comment by looking at the lines in the data.")

    return graph_response

# ask question

def ask_question(data_file,question):

    file_name = data_file.name
    file_extension = os.path.splitext(file_name)[1][1:].lower()

    if file_extension == 'csv':
        df = pd.read_csv(data_file, low_memory=True)
    elif file_extension in ['xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods','odt']:
        df = pd.read_excel(data_file)
    else:
        print("Unsupported file format")

    pandas_agent=create_pandas_dataframe_agent(selected_llm,df,verbose=True,agent_executor_kwargs={"handle_parsing_errors":"True"})

    AI_Response=pandas_agent.run(f"{question} answer the question in the asked language")

    return AI_Response














