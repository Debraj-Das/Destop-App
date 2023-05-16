from pypdf import PdfWriter
import os , glob

# for change the directory
l = glob.glob('*.pdf')
merger = PdfWriter()

for pdf in l:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()
