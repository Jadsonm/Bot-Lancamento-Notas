from time import sleep
import pyautogui
import keyboard
pyautogui.PAUSE = 0.9



def move(location):
    x,y= pyautogui.center(location)
    pyautogui.moveTo(x,y, duration=0.6)

def move_and_click(location):
    move(location)
    pyautogui.click()

def move_and_double_click(location):
     move(location)
     pyautogui.doubleClick()



keyboard.wait('s')
# --> VERIFICANDO SE A TELA DE LANÇAMENTO ESTÁ ABERTA
verificar_tela = pyautogui.locateOnScreen('images/verificar_tela.png', confidence=0.8)
sleep(1)
if verificar_tela == None:
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('g')
    sleep(0.6)      
    pyautogui.write('Nota de Compra servicos gerais')
    sleep(1.5)
    pyautogui.press('enter')


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

        

        ## --> VERIFICANDO SE A TELA JÁ CARREGOU TOTALMENTE
        verificar_top = pyautogui.locateOnScreen('images/verificar_top.png', confidence=0.8)
        while verificar_top == None:
            sleep(0.5)
            verificar_top = pyautogui.locateOnScreen('images/verificar_top.png', confidence=0.8)

        empresa = pyautogui.locateOnScreen('images/empresa.png', confidence=0.8)
        move_and_click(empresa)

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

        ## --> VERIFICANDO SE JÁ APARECEU O NUMERO UNICO PARA DAR CONTINUIDADE
        numero_unico = pyautogui.locateOnScreen('images/numero_unico.png', confidence=0.8)
        while numero_unico != None:
            sleep(0.5)
            numero_unico = pyautogui.locateOnScreen('images/numero_unico.png', confidence=0.8)


        ## --> SE A TELA ESTIVER NO MODO FORMULARIO É PARA TROCAR
        modo_formulario = pyautogui.locateOnScreen('images/modo_formulario.png', confidence=0.8)
        sleep(1)
        if modo_formulario != None:
            move_and_click(modo_formulario)

        sleep(1)
        pyautogui.write(cod_produto)
        pyautogui.press('tab')
        sleep(1.5)
        ## --> LOCALIZANDO O ERRO QUE APARECE NA TELA
        ok_error = pyautogui.locateOnScreen('images/ok_entrada.png', confidence=0.8)
        #verificando se a imagem apareceu na tela
        while ok_error == None:
         sleep(1)
         ok_error = pyautogui.locateOnScreen('images/ok_entrada.png', confidence=0.8)

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

        ## --> VERIFICANDO SE CARREGOU TUDO CORRETAMENTE
        sem_local = pyautogui.locateOnScreen('images/sem_local.png', confidence=0.8)
        while sem_local == None:
            sleep(0.5)
            sem_local = pyautogui.locateOnScreen('images/sem_local.png', confidence=0.8)

        opcoes = pyautogui.locateOnScreen('images/opcoes.png', confidence=0.8)
        move_and_click(opcoes)
        sleep(0.6)
        anexar = pyautogui.locateOnScreen('images/anexar.png', confidence=0.8)
        move_and_click(anexar)
        sleep(0.5)


        adicionar_anexo = pyautogui.locateOnScreen('images/adicionar_anexo.png', confidence=0.8)
        while adicionar_anexo == None:
            sleep(0.5)
            adicionar_anexo = pyautogui.locateOnScreen('images/adicionar_anexo.png', confidence=0.8)
        move_and_click(adicionar_anexo)    


        verificar_anexo = pyautogui.locateOnScreen('images/verificar_anexo.png', confidence=0.8)
        while verificar_anexo == None:
            sleep(0.5)
            verificar_anexo = pyautogui.locateOnScreen('images/verificar_anexo.png', confidence=0.8)

        sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('NF')
        pyautogui.press('tab')
        pyautogui.press('enter')


        salvar_anexo = pyautogui.locateOnScreen('images/salvar_anexo.png', confidence=0.8)
        while salvar_anexo == None:
            sleep(0.5)
            salvar_anexo = pyautogui.locateOnScreen('images/salvar_anexo.png', confidence=0.8)


        pyautogui.write(nro_nota)
        pyautogui.press('down')
        pyautogui.press('enter')
        sleep(0.5)
        salvar = pyautogui.locateOnScreen('images/salvar.png', confidence=0.8)
        move_and_click(salvar)
        sleep(0.5)
        ok_anexo = pyautogui.locateOnScreen('images/ok_anexo.png', confidence=0.8)
        move_and_click(ok_anexo)        

        confirmar = pyautogui.locateOnScreen('images/confirmar.png', confidence=0.8)
        move_and_click(confirmar)

        definir_liberador = pyautogui.locateOnScreen('images/definir_liberador.png', confidence=0.8)
        while definir_liberador == None:
            sleep(0.5)
            definir_liberador = pyautogui.locateOnScreen('images/definir_liberador.png', confidence=0.8)

        sleep(0.6)
        pyautogui.write(primeiro_aprovador)
        pyautogui.press('enter')
        move_and_click(definir_liberador)
        sleep(1)
        pyautogui.press('esc')
        sleep(1)
        adicionar_nota = pyautogui.locateOnScreen('images/adicionar_nota.png', confidence=0.8)
        move_and_click(adicionar_nota)
        sleep(3)
