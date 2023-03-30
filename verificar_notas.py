from pypdf import PdfReader
import re
from datetime import datetime, timedelta
import os


path = "C:\\Users\\Jadson Matheus\\python\\bot_lancamento_notas\\notas_lancamento"
file = os.listdir(path)


for file_name in file:
    if file_name.endswith('.pdf'):
        pdf_file = open(os.path.join(path, file_name), 'rb')

        pdf_reader = PdfReader(pdf_file)

        conteudo = {}

        for index, pdf_pag in enumerate(pdf_reader.pages):
            conteudo[index + 1] = pdf_pag.extract_text()

        print(conteudo)

        pdf_file.close()    