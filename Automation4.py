#how to read password protected pdf file using python

import pdfplumber
import io
with io.open("password.txt") as f2:
    pwd=f2.read()
    f2.close()

with pdfplumber.open("protected.pdf",password=pwd) as f1:
    #get metadata
    meta_data=f1.metadata
    print(meta_data)
    
    #get the page count
    pages=f1.pages
    print(len(pages))
    
    #get the text data from every page
    for page in pages:
        print(page.extract_text())
