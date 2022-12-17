import aspose.words as aw
import sys
import os

docs_folder = sys.argv[1]
pdf_folder = sys.argv[2]
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)
for filename in os.listdir(docs_folder):
    doc = aw.Document(f'{docs_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    doc.save(f'{pdf_folder}{clean_name}.pdf')
    print("Done !")
