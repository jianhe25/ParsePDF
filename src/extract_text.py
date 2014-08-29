from subprocess import call
call(["java", "-jar", "venders/pdfbox-app-1.8.6.jar", "ExtractText", "../pdf_data/ENR_4_1.pdf", "../text_data/ENR_4_1"])

