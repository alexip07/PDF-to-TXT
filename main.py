import PyPDF2 as pdf
import os


def convert_all_pdfs(fisier_pdf, fisier_txt):
    # Iterates through all the PDFs in a folder(input_folder)
    for filename in os.listdir(fisier_pdf):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(fisier_pdf, filename)

            # Names the output file
            output_filename = os.path.splitext(filename)[0] + '.txt'
            output_path = os.path.join(fisier_txt, output_filename)

            # From PDF to TXT
            pdf_to_text(pdf_path, output_path)


def pdf_to_text(path_pdf, path_txt):
  """ Takes the info from the PDFS and then it writes to a new file"""
    with open(path_pdf, 'rb') as pdf_file:
        pdf_reader = pdf.PdfReader(pdf_file)
        text_content = ""

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text_content += page.extract_text()

        with open(path_txt, 'w', encoding='utf-8') as text_file:
            text_file.write(text_content)
          
# Replace the path_folder_pdf with the path to your folder and do the same for the txt
# This script will do all the files in a folder
# For special characters that need to be re[placed check the file reformat.py / but keep in mind that all the modification will be made ONLY to the TXT file

convert_all_pdfs(r'path_folder_pdf', r'path_folder_txt')
