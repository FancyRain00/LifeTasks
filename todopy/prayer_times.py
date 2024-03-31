import datetime
import PyPDF2
import requests
from bs4 import BeautifulSoup
import re
import io

def helsinki():
    # Fetch the webpage
    url = 'https://www.rukousajat.fi/main.a1581e653a86a0bd.js'
    response = requests.get(url)
    html_content = response.text
    
    # Regular expression pattern to match the data
    #         {date:"3009",fajr:"5:02",sunrise:"7:21",zuhur:"13:12",asr:"16:01",maghrib:"18:58",isha:"21:08"}
    pattern = r'\{date:"\d{4}",fajr:"\d{1,2}:\d{2}",sunrise:"\d{1,2}:\d{2}",zuhur:"\d{1,2}:\d{2}",asr:"\d{1,2}:\d{2}",maghrib:"\d{1,2}:\d{2}",isha:"\d{1,2}:\d{2}"\}'

    # Extract data using regular expression
    matches = re.findall(pattern, html_content)

    # Process extracted data
    for match in matches:
        print(match)

def turku():
    # URL of the PDF file
    pdf_url = "https://tisy.fi/wp-content/uploads/wplhc/1/lunar-hijri-calendar.pdf"

    # Fetch PDF content directly
    response = requests.get(pdf_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BytesIO object from the response content
        pdf_stream = io.BytesIO(response.content)
        
        # Create a PDF reader object from the BytesIO object
        pdf_reader = PyPDF2.PdfReader(pdf_stream)
        
        # Get the number of pages
        num_pages = len(pdf_reader.pages)
        
        # Loop through each page and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            
            # Print the text from the current page
            print(text)
    else:
        print("Failed to fetch the PDF content.")


def Tampere():
    month_nmr = 4
    month_str = "Huhtikuu"

    # URL of the PDF file
    pdf_url = f"http://islamtampere.com/wp-content/uploads/2024/01/{month_nmr}.-{month_str}-2024.pdf"

    # Fetch PDF content directly
    response = requests.get(pdf_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BytesIO object from the response content
        pdf_stream = io.BytesIO(response.content)
        
        # Create a PDF reader object from the BytesIO object
        pdf_reader = PyPDF2.PdfReader(pdf_stream)
        
        # Get the number of pages
        num_pages = len(pdf_reader.pages)
        
        # Loop through each page and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            
            # Print the text from the current page
            print(text)
    else:
        print("Failed to fetch the PDF content.")
