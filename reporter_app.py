import streamlit as st
from PIL import Image
import io
import os
import base64
import pandas as pd

import Module1_Reporter as mone
import Module2_Reporter as mtwo
import Module3_Reporter as mthree


def col_to_section():
    st.title("Import Table to Create Vertical Report")

    # Upload files
    uploaded_files = mone.upload_files()

    tables = {}
    sheet_options = {}

    if uploaded_files:
        # Process each uploaded file
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name
            base_name = mone.remove_extension(file_name)  # Remove extension for table names
            
            if file_name.endswith(('xlsx', 'xls')):
                excel_file, sheet_names = mone.process_excel_file(uploaded_file)
                sheet_options[file_name] = sheet_names
                
                # Display Excel file sheets
                selected_sheets = st.multiselect("Select sheets for " + file_name, options=sheet_names)
                for sheet in selected_sheets:
                    df = pd.read_excel(uploaded_file, sheet_name=sheet)
                    table_name = f"{base_name} - {sheet}"
                    tables[table_name] = df
            
            elif file_name.endswith('csv'):
                df = pd.read_csv(uploaded_file)
                table_name = base_name
                tables[table_name] = df

        # Display all tables
        mone.display_tables_asprose(tables)

        # Optional: Display the list of table names
        st.header("Main Report")
        table_names = mone.generate_table_names(tables)
        st.text('\n'.join(table_names))

        # Generate and provide download link for the HTML report
        html_report = mone.generate_html_report(tables)
        return html_report


def table_to_table():
    st.title("Dynamic Table Importer")

    # Upload files
    uploaded_files = mtwo.upload_files()

    tables = {}
    sheet_options = {}

    if uploaded_files:
        # Process each uploaded file
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name
            base_name = mtwo.remove_extension(file_name)  # Remove extension for table names
            
            if file_name.endswith(('xlsx', 'xls')):
                excel_file, sheet_names = mtwo.process_excel_file(uploaded_file)
                sheet_options[file_name] = sheet_names
                
                # Display Excel file sheets
                selected_sheets = st.multiselect("Select sheets for " + file_name, options=sheet_names)
                for sheet in selected_sheets:
                    df = pd.read_excel(uploaded_file, sheet_name=sheet)
                    table_name = f"{base_name} - {sheet}"
                    tables[table_name] = df
            
            elif file_name.endswith('csv'):
                df = pd.read_csv(uploaded_file)
                table_name = base_name
                tables[table_name] = df

        # Display all tables
        mtwo.display_tables(tables)

        # Optional: Display the list of table names
        st.header("Table Names")
        table_names = mtwo.generate_table_names(tables)
        st.text('\n'.join(table_names))

        # Generate and provide download link for the HTML report
        html_report = mtwo.generate_html_report(tables)
        return html_report




def image_to_image():
    st.title("Add Image(s) to Report")

    # Upload files
    uploaded_files = mthree.upload_files()

    images = {}

    if uploaded_files:
        # Process each uploaded file
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name
            base_name = mthree.remove_extension(file_name)  # Remove extension for image names

            # Read the image and convert to PNG
            image_data = mthree.process_image(uploaded_file)
            images[base_name] = image_data

        # Display all images
        mthree.display_images(images)

        # Generate and provide download link for the HTML report
        html_report = mthree.generate_html_report(images)
        return(html_report)


A = col_to_section()
B = table_to_table()
C = image_to_image()


# Combine reports if they exist
html_report = ""
if A:
    html_report += A + "\n"
if B:
    html_report += B + "\n"
if C:
    html_report += C + "\n"

if not html_report:
    html_report = "Report Empty"

st.download_button(
    label="Download HTML Report",
    data=html_report,
    file_name="report.html",
    mime="text/html"
)
