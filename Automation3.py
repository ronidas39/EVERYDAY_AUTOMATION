#read pdf file using pdfplumber package

import pdfplumber
with pdfplumber.open("samplereport.pdf")as f1:
    #getting the metadata
    file_metadata=f1.metadata
    print(file_metadata)
    #how to get the total number of pages
    pages=f1.pages
    print(type(pages))
    print(len(pages))
    #how to get text from pages
    for page in pages:
        print(page.extract_text())
    
    
    
        
    
