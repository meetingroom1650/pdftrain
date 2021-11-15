# Converts multipage pdf to individual jpg files
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
print('starting process')

#Dom Dev Poppler Path
#poppler_path = r'C:/Program Files/poppler/poppler-21.10.0/Library/bin'

#Jeff Dev Poppler Path
#poppler_path=r'\\ghcnyfs01\users\JTom\Downloads\Release-21.11.0-0 (2)\poppler-21.11.0\Library\bin'
# Store Pdf with convert_from_path function
images = convert_from_path("K:/Reporting/HCS TimeSheets/20211004-1.pdf",single_file=False, poppler_path=r'\\ghcnyfs01\users\JTom\Downloads\Release-21.11.0-0 (2)\poppler-21.11.0\Library\bin')
#images = convert_from_path('K:/Reporting/PDFtoJPG/DOC100721-10072021170930 (1).pdf')
for i in range(len(images)):

# Save pages as images in the pdf
   images[i].save('K:/Reporting/HCS TimeSheets/Timesheetsjpgs/page'+ str(i) +'.jpg', 'JPEG')

