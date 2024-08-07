import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
# Example usage
pdf_file = 'test2.pdf'
text_to_find = 'Register No'
page_numbers = []
with open(pdf_file, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()      
        if text_to_find in text:
            roll=text[66:78]
            page_numbers.append(page_num)  
    page_numbers.append(len(reader.pages))
    ini=0
    fin=1
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        x=page_numbers[ini]
        y=page_numbers[fin]
        for page in range(x,y):
            print(page_numbers[ini],page_numbers[fin])
            reader = PdfReader(file)
            writer.add_page(reader.pages[page])
            with open(f'{roll}{fin}.pdf', 'wb') as outfile: 
                writer.write(outfile)
        ini=ini+1
        fin=fin+1