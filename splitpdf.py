import os
from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_file_path = "K:/Reporting/HCS TimeSheets/20211004-1.pdf" #Pdf file source
file_base_name = pdf_file_path.replace(".pdf", '')
output_folder_path = os.path.join(os.getcwd(), 'output') #output location of pdf
print(output_folder_path)
pdf = PdfFileReader(pdf_file_path)

for page_num in range(pdf.numPages):
    pdfWriter = PdfFileWriter()
    pdfWriter.addPage(pdf.getPage(page_num))

    with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
        pdfWriter.write(f)
        f.close()
