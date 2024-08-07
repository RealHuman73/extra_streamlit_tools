
import streamlit as st
from PIL import Image
import io
import os
import base64
import pandas as pd


def upload_files():
    """Handle file uploads and return list of uploaded files."""
    return st.file_uploader("Upload CSV/Excel files", type=['csv', 'xlsx', 'xls'], accept_multiple_files=True, key = "mod1")

def process_excel_file(uploaded_file):
    """Process an Excel file and return DataFrame and sheet names."""
    excel_file = pd.ExcelFile(uploaded_file)
    sheet_names = excel_file.sheet_names
    return excel_file, sheet_names

def remove_extension(file_name):
    """Remove the extension from a file name."""
    return os.path.splitext(file_name)[0]

def display_tables_asprose(tables):
    """Generate HTML for tables and their content."""
    html_content = ""
    for table_name, df in tables.items():
        html_content += f"<h2>{table_name}</h2>"  # Display table name as a section header
        
        # Iterate over each column in the dataframe
        for column in df.columns:
            html_content += f"<h3>{column}</h3>"  # Display column name as a section header
            
            # Convert column content to HTML list
            column_content = df[column].to_list()
            column_html = '<br>'.join(str(value) for value in column_content)
            html_content += f"<p>{column_html}</p>"  # Display the column content
            
    return html_content

def generate_table_names(tables):
    """Generate a list of table names."""
    return list(tables.keys())

def generate_html_report(tables):
    """Generate an HTML report from the tables with specific styles."""
    html_content = """
    <html>
    <head>
        <title>Dynamic Table Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin-left: 1in;
                margin-right: 1in;
            }
            h2 {
                color: #0033A0; /* Cerulean Blue */
            }
            h3 {
                color: #0033A0; /* Cerulean Blue */
            }
            p {
                margin-bottom: 10px;
                line-height: 1.6;
                padding-left: 2em; /* Indent all text paragraphs */
            }
        </style>
    </head>
    <body>
    """
    html_content += display_tables_asprose(tables)
    html_content += "</body></html>"
    return html_content

