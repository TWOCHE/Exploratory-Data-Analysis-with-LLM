import streamlit as st
import datahelper

if "dataload" not in st.session_state:
    st.session_state.dataload = False

def activate_dataload():
    st.session_state.dataload = True


st.set_page_config(page_title="🦜 LangChain: Chat with Pandas DataFrame", layout="wide" ,page_icon="🦜")
st.image(image="./img/stats_v1.jpg",use_column_width=True)
st.title("EDA: Exploratory Data Analysis with LLM 🕵️‍♀️")
st.divider()

st.sidebar.subheader("upload your file")
st.sidebar.divider()

loaded_file= st.sidebar.file_uploader("Select the file to upload",type=["csv","xlsx",'xls'])

load_data_btn= st.sidebar.button(label="Upload", on_click=activate_dataload, use_container_width=True)

col_prework, col_dummy,col_interaction=st.columns([7,1,6])

if st.session_state.dataload:
    @st.cache_data
    def summarize():
        loaded_file.seek(0)
        data_summary=datahelper.summarize_data(data_file=loaded_file)
        return data_summary
    
    data_summary=summarize()

    with col_prework:
        st.info("Data summary")
        st.subheader("head of data:")
        st.write(data_summary["initial_data_sample"])
        st.divider()
        st.subheader("columns of data:")
        st.write(data_summary["column_descriptions"])
        st.divider()
        st.subheader("columns of data types:")
        st.write(data_summary["column_types"])
        st.divider()
        st.subheader("missing values of data:")
        st.write(data_summary["missing_values"])
        st.divider()
        st.subheader("duplicated values of data:")
        st.write(data_summary["duplicate_values"])
        st.divider()
        st.subheader("outlier values of data:")
        st.write(data_summary["outlier_values"])
        st.divider()
        st.subheader("description of data:")
        st.write(data_summary["essential_metrics"])
        st.divider()

    with col_dummy:
        st.empty()

    with col_interaction:
        st.info("interaction with data")
        variable_of_interest=st.text_input(label="Which variable do you want to analyze?")
        examine_btn=st.button(label="Examine")
        st.divider()

        @st.cache_data
        def explore_variable(data_file, variable_of_interest):

            data_file.seek(0)
            dataframe=datahelper.get_dataframe(data_file=data_file)
            st.bar_chart(data=dataframe,y=[variable_of_interest])
            st.divider()
            data_file.seek(0)
            graph_response=datahelper.analyze_graph(data_file=loaded_file,variable_of_interest=variable_of_interest)
            st.success(graph_response)
            return


        if variable_of_interest or examine_btn:
            explore_variable(data_file=loaded_file,variable_of_interest=variable_of_interest)

        free_question=st.text_input(label="What do you want to know about the dataset?")
        ask_btn=st.button(label="Ask")
        st.divider()

        @st.cache_data
        def answer_question(data_file, question):
            data_file.seek(0)
            AI_Response=datahelper.ask_question(data_file=loaded_file,question=free_question)
            st.success(AI_Response)
            return
        
        if free_question or ask_btn:
            answer_question(data_file=loaded_file,question=free_question)

