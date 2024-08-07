import streamlit as st
from PIL import Image
import io
import os
import base64
import pandas as pd

def upload_files():
    """Handle file uploads and return list of uploaded files."""
    return st.file_uploader("Upload Image files", type=['png', 'jpg', 'jpeg', 'svg', 'tif', 'tiff'], accept_multiple_files=True, key = "mod3")

def process_image(image_file):
    """Process image and convert it to PNG format."""
    image = Image.open(image_file)
    with io.BytesIO() as buffer:
        image.save(buffer, format='PNG')
        return buffer.getvalue()

def remove_extension(file_name):
    """Remove the extension from a file name."""
    return os.path.splitext(file_name)[0]

def display_images(images):
    """Display images in Streamlit."""
    for image_name, image_data in images.items():
        st.subheader(image_name)
        st.image(image_data, use_column_width=True)

def generate_html_report(images):
    """Generate an HTML report from the images."""
    html_content = """
    <html>
    <head>
        <title>Dynamic Image Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin-left: 1in;
                margin-right: 1in;
            }
            h2 {
                color: #0000FF; /* Blue */
            }
            .image-container {
                max-width: 80%;
                margin-bottom: 80px;
            }
            img {
                max-width: 80%;
                height: auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
    """
    
    # Add images to HTML content
    for image_name, image_data in images.items():
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        html_content += f'<h2>{image_name}</h2>'
        html_content += f'<div class="image-container">'
        html_content += f'<img src="data:image/png;base64,{image_base64}" alt="{image_name}">'
        html_content += '</div>'
    
    html_content += "</body></html>"
    return html_content
