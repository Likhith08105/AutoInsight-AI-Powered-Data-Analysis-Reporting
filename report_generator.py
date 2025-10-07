import pandas as pd
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

def generate_report(dataframe):
    # Load environment variables
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    # Initialize Groq API client
    chat_groq = ChatGroq(
        temperature=0,
        groq_api_key=groq_api_key,
        model_name="llama-3.1-70b-versatile"
    )

    # Prepare a prompt template
    prompt_template = PromptTemplate(
        input_variables=["data_summary", "data_sample"],
        template="""
        ### DATA ANALYSIS REQUEST:
        You are an expert data analyst. Analyze the following data and generate a comprehensive report, including insights, trends, and statistical summaries.

        ### DATA SUMMARY:
        {data_summary}

        ### DATA SAMPLE:
        {data_sample}

        ### INSTRUCTIONS:
        Provide a structured, professional report with headings, bullet points, and a conclusion.
        """
    )

    # Summarize data
    data_summary = dataframe.describe(include='all').to_json()
    data_sample = dataframe.head().to_json()

    # Create prompt and get response
    prompt = prompt_template.format(
        data_summary=data_summary,
        data_sample=data_sample
    )

    response = chat_groq.invoke(prompt)
    report = getattr(response, "content", "No report generated.")
    return report