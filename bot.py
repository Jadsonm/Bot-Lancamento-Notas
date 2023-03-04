from time import sleep
import pyautogui
import keyboard
import functions
pyautogui.PAUSE = 0.9







keyboard.wait('s')

functions.verificando_tela_aberta()


with open ('dados.txt','r') as file:
    for linha in file:
        cod_empresa = linha.split(',')[0]
        nro_nota = linha.split(',')[1]
        data_emissao = linha.split(',')[2]
        data_vencimento = linha.split(',')[3]
        cod_parceiro = linha.split(',')[4]
        tipo_negociacao = linha.split(',')[5]    
        primeiro_aprovador = linha.split(',')[6]
        segundo_aprovador = linha.split(',')[7]
        observacao = linha.split(',')[8]
        cod_produto = linha.split(',')[9]
        quantidade = linha.split(',')[10]
        valor = linha.split(',')[11]
        projeto = linha.split(',')[12]
        centro_resultado = linha.split(',')[13]
        natureza = linha.split(',')[14]

        
        functions.aguardando_tela_carregar()

        pyautogui.write(cod_empresa) 
        pyautogui.press('tab')
        sleep(1)
        pyautogui.write(nro_nota) 
        pyautogui.press('tab')
        pyautogui.write('0')
        pyautogui.press('tab')
        pyautogui.write(data_emissao) 
        pyautogui.press('tab')
        pyautogui.write(data_vencimento) 
        pyautogui.press('tab', presses=5)
        pyautogui.write(cod_parceiro) 
        pyautogui.press('tab', presses=2)
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

        pyautogui.write(nro_nota)
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
