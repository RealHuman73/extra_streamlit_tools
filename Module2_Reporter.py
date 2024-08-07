
import streamlit as st
from PIL import Image
import io
import os
import base64
import pandas as pd



def upload_files():
    """Handle file uploads and return list of uploaded files."""
    return st.file_uploader("Upload CSV/Excel files", type=['csv', 'xlsx', 'xls'], accept_multiple_files=True, key = "mod2")

def process_excel_file(uploaded_file):
    """Process an Excel file and return DataFrame and sheet names."""
    excel_file = pd.ExcelFile(uploaded_file)
    sheet_names = excel_file.sheet_names
    return excel_file, sheet_names

def remove_extension(file_name):
    """Remove the extension from a file name."""
    return os.path.splitext(file_name)[0]

def display_tables(tables):
    """Display tables and their content in Streamlit."""
    for table_name, df in tables.items():
        st.subheader(table_name)
        st.dataframe(df)  # Use st.dataframe for better display of DataFrames

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
                color: #0000FF; /* Blue */
            }
            h3 {
                color: #0033A0; /* Cerulean Blue */
            }
            p {
                margin-bottom: 10px;
                line-height: 1.6;
                padding-left: 2em; /* Indent all text paragraphs */
            }
            .table-container {
                max-height: 400px; /* Adjust the height as needed */
                overflow-y: auto;
                margin-bottom: 20px;
                border: 1px solid #ddd;
                padding: 10px;
                border-radius: 5px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
    """
    
    # Add tables to HTML content
    for table_name, df in tables.items():
        html_content += f"<h2>{table_name}</h2>"
        html_content += '<div class="table-container">'
        html_content += df.to_html(index=False, classes='table')
        html_content += '</div>'
    
    html_content += "</body></html>"
    return html_content

def generate_table_names(tables):
    """Generate a list of table names."""
    return list(tables.keys())

