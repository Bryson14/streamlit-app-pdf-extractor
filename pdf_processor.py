import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io
import re


def split_pdf(file):
    reader = PdfReader(file)
    for page in range(len(reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(reader.pages[page])
        output = io.BytesIO()
        pdf_writer.write(output)
        output.seek(0)
        yield output, page

def find_ein(pdf_page):
    text = pdf_page.extractText()
    ein_match = re.search(r'EIN:\s(\d{9})', text)
    if ein_match:
        return ein_match.group(1)
    return None

def main():
    st.title("PDF Processor")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        for output, page_number in split_pdf(uploaded_file):
            ein = find_ein(output)
            if ein:
                st.write(f"Page {page_number + 1} EIN: {ein}")
                # Here you can save the file with the new name based on the EIN
                # For example, you can save it to the local filesystem or upload it to a cloud storage
                # For demonstration, let's just print the EIN
            else:
                st.write(f"Page {page_number + 1} does not contain an EIN")

if __name__ == "__main__":
    main()
