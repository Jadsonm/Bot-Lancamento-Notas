from time import sleep
import pyautogui
import keyboard
import functions
pyautogui.PAUSE = 0.9







keyboard.wait('s')

functions.verificando_tela_aberta()


with open ('dados.txt','r') as file:
    for linha in file:
        dados = linha.split(',')
        cod_empresa = dados[0]
        nro_nota = dados[1]
        data_emissao = dados[2]
        data_vencimento = dados[3]
        cod_parceiro = dados[4]
        tipo_negociacao = dados[5]
        primeiro_aprovador = dados[6]
        segundo_aprovador = dados[7]
        observacao = dados[8]
        cod_produto = dados[9]
        quantidade = dados[10]
        valor = dados[11]
        projeto = dados[12]
        centro_resultado = dados[13]
        natureza = dados[14]

        
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
