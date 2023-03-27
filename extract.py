from pypdf import PdfReader
import re
from datetime import datetime, timedelta


pdf_reader = PdfReader('teste.pdf')

conteudo = {}

for index, pdf_pag in enumerate(pdf_reader.pages):
    conteudo[index + 1] = pdf_pag.extract_text()


conteudo_splitado = re.split(r'\n|=|\|', conteudo[1])


def get_value(text, ignore_text = None):
    for index, item in enumerate(conteudo_splitado):
        if text.lower() in item.lower():
            conteudo_encontrado = conteudo_splitado[index + 1].strip()
            if ignore_text == None or ignore_text not in conteudo_encontrado:
                return conteudo_encontrado


print(get_value('Nota'))
emissao = get_value('emissão')[0:10]
emissao_date = datetime.strptime(emissao, '%d/%m/%Y')
vencimento_date = emissao_date + timedelta(days=28)
vencimento_string = vencimento_date.strftime('%d/%m/%Y')

print(emissao)
print(vencimento_string)
print(get_value('valor'))
cnpj = get_value('cnpj', '69.258.911')
cnpj_numerico = re.sub(r'\D', '', cnpj)
print(cnpj_numerico)
