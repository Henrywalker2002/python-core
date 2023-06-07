import PyPDF2

# Open the PDF file
with open('report.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    infor = pdf_reader.metadata
    print(num_pages, infor)
    first = pdf_reader.pages[0]
    
    writer = PyPDF2.PdfWriter()
    writer.add_page(first)
    writer.write("first.pdf")
    writer.close()
    # Iterate over each page and extract text
    # for page in pdf_reader.pages:
    #     text = page.extract_text()
    #     print(text)

    

