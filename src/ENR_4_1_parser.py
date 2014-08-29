from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import  TextConverter # , XMLConverter, HTMLConverter
import urllib2
from urllib2 import Request
import datetime
import re

# Define a PDF parser function
def parsePDF(pdf_file):

    pdf_file = open(pdf_file, "r").read()

    
    # Cast to StringIO object
    from StringIO import StringIO
    memory_file = StringIO(pdf_file)

    # Create a PDF parser object associated with the StringIO object
    parser = PDFParser(memory_file)

    # Create a PDF document object that stores the document structure
    document = PDFDocument(parser)

    # Define parameters to the PDF device objet 
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    codec = 'utf-8'

    # Create a PDF device object
    device = TextConverter(rsrcmgr, retstr, codec = codec, laparams = laparams)
    
    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        data = retstr.getvalue()
        print data
        break

def is_empty_line(line):
    for c in line:
        if c != ' ' and c != '\n' and c != '\r':
            return False
    return True

def main():
    parsePDF("../pdf_data/ENR_4_1.pdf")
    # with open('../text_data/ENR_4_1', 'r') as f:
    #     lines = []
    #     for line in f:
    #         line = line.strip()
    #         if not is_empty_line(line):
    #             lines.append(line)

    #     pos_station = next(i for i in range(len(lines)) if lines[i] == "Station")
    #     for i in range(pos_station, pos_station+10):
    #         print lines[i]

if __name__ == "__main__":
    main()
    