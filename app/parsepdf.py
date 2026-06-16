# import PyPDF2 as pypdf2

# def parse_pdf(file) -> str:
#     """
#     Function to read a PDF file and extract text using PyPDf2.
#     """
#     print('Parseing PDF file')
    
#     try:
#         reader = pypdf2.PdfFileReader(file)
#         text = ''
#         for page in reader.pages:
#             text += page.extract_text() + '\n'
            
#         return text.strip()
#     except Exception as e:
#         return str(e)

from PyPDF2 import PdfReader

def parse_pdf(file):
    print("Parsing PDF file")

    pdf_reader = PdfReader(file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text