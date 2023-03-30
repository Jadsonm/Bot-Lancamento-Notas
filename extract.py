from pypdf import PdfReader
import re
from datetime import datetime, timedelta
import os
import pyautogui
import functions
from time import sleep
import keyboard



path = "C:\\Users\\Jadson Matheus\\python\\bot_lancamento_notas\\notas_lancamento"
file = os.listdir(path)

def get_value(text, ignore_text=None):
    for index, item in enumerate(conteudo_splitado):
        if text.lower() in item.lower():
            conteudo_encontrado = conteudo_splitado[index + 1].strip()
            if ignore_text == None or ignore_text not in conteudo_encontrado:
                return conteudo_encontrado

keyboard.wait('s')

for file_name in file:
    if file_name.endswith('.pdf'):
        pdf_file = open(os.path.join(path, file_name), 'rb')

        pdf_reader = PdfReader(pdf_file)

        conteudo = {}

        for index, pdf_pag in enumerate(pdf_reader.pages):
            conteudo[index + 1] = pdf_pag.extract_text()

        conteudo_splitado = re.split(r'\n|=|\|', conteudo[1])
        cnpj = get_value('cnpj', '69.258.911')
        cnpj_numerico = re.sub(r'\D', '', cnpj)
        print(cnpj_numerico)
        

        if cnpj_numerico == '07891128000131':
            cod_empresa = '4'    
            #nota = get_value('Nota')
            nota = '1322'
            emissao = get_value('emissão')[0:10]
            emissao_date = datetime.strptime(emissao, '%d/%m/%Y')
            vencimento_date = emissao_date + timedelta(days=28)
            vencimento_string = vencimento_date.strftime('%d/%m/%Y')
            tipo_negociacao = '68'
            primeiro_aprovador = '17'
            segundo_aprovador = '1'
            observacao = get_value('DESCRIÇÃO DO SERVIÇO')
            cod_produto = '10739'
            quantidade = '1'
            valor = get_value('valor')
            projeto = '90001000'
            centro_resultado = '1020500'
            natureza = '3020500'



        if cnpj_numerico == '66715723000185':
            cod_empresa = '4'    
            nota_com_zeros = get_value('Nota')
            pattern = "[0]+"
            repl = ""
            nota = re.sub(pattern, repl,nota_com_zeros)
            emissao = get_value('emissão')[0:10]
            emissao_date = datetime.strptime(emissao, '%d/%m/%Y')
            vencimento_date = emissao_date + timedelta(days=28)
            vencimento_string = vencimento_date.strftime('%d/%m/%Y')
            tipo_negociacao = '68'
            primeiro_aprovador = '181'
            segundo_aprovador = '194'
            observacao = get_value('DESCRIÇÃO DO SERVIÇO')
            cod_produto = '10739'
            quantidade = '1'
            valor = get_value('valor')
            projeto = '90001000'
            centro_resultado = '1010601'
            natureza = '3020302'

        functions.aguardando_tela_carregar()

        pyautogui.write('4') 
        pyautogui.press('tab')
        sleep(0.3)
        pyautogui.write(nota) 
        pyautogui.press('tab')
        pyautogui.write('0')
        pyautogui.press('tab')
        pyautogui.write(emissao) 
        pyautogui.press('tab')
        pyautogui.write(vencimento_string) 
        pyautogui.press('tab', presses=5)
        pyautogui.press('enter')
        functions.verificar_cnpj()
        pyautogui.write(cnpj_numerico)
        pyautogui.press('enter')
        functions.escolhendo_cnpj()
        sleep(0.8)
        pyautogui.press('tab')
        pyautogui.write(tipo_negociacao) 
        pyautogui.press('tab')
        pyautogui.write(primeiro_aprovador) 
        pyautogui.press('tab')
        pyautogui.write(segundo_aprovador) 
        pyautogui.press('tab')
        pyautogui.write(observacao)
        sleep(1)
        pyautogui.press('f7')

        functions.aguardando_nro_unico()

        functions.verificando_modo_tela()

        sleep(1)
        pyautogui.write(cod_produto)
        pyautogui.press('tab')
        sleep(1.5)

        functions.error()
        
        pyautogui.press('enter')
        #pyautogui.press('tab')
        pyautogui.write(quantidade)
        pyautogui.press('tab')
        pyautogui.write(valor)
        pyautogui.press('tab')
        pyautogui.write(projeto)
        pyautogui.press('tab')
        pyautogui.write(centro_resultado)
        pyautogui.press('tab')
        pyautogui.write(natureza)
        pyautogui.press('tab')
        sleep(0.6)
        pyautogui.press('f7')

        functions.aguardando_salvar_item()

        functions.add_anexo()

        pyautogui.write(nota)
        pyautogui.press('down')
        pyautogui.press('enter')
        sleep(0.5)

        functions.salvar_confimar_nota()

        functions.verificando_liberador()
        sleep(0.6)
        pyautogui.write(primeiro_aprovador)
        pyautogui.press('enter')

        functions.confirmando_liberador()

        functions.finalizar_e_adicionar_outra_nota()

        pdf_file.close()
