

# Converts multipage pdf to individual jpg files



from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
print('starting process')
#poppler_path = r'C:/Program Files/poppler/poppler-21.10.0/Library/bin'
# Store Pdf with convert_from_path function
images = convert_from_path("K:/Reporting/GirlingPDFs/All_Docs.pdf",single_file=False)
#images = convert_from_path('K:/Reporting/PDFtoJPG/DOC100721-10072021170930 (1).pdf')
for i in range(len(images)):

# Save pages as images in the pdf
    images[i].save('K:/Reporting/GirlingPDFs/jpgs/page'+ str(i) +'.jpg', 'JPEG')

