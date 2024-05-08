import pdfkit

# how convert html to pdf in beautiful way


pdfkit.from_file('test.html', 'out4.pdf' , options = {'page-size': 'A4', 'margin-top': '0.75in', 'margin-right': '0.75in', 'margin-bottom': '0.75in', 'margin-left': '0.75in' , 'encoding': "UTF-8" , 'no-outline': None  , 'dpi': '300' , 'image-dpi': '300' , 'image-quality': '100' })
