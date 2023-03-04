from time import sleep
import pyautogui


def move(location):
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x, y, duration=0.6)


def move_and_click(location):
    move(location)
    pyautogui.click()


def move_and_double_click(location):
    move(location)
    pyautogui.doubleClick()


def verificando_tela_aberta():
    verificar_tela = pyautogui.locateOnScreen(
        'images/verificar_tela.png', confidence=0.8)
    sleep(1)
    if verificar_tela == None:
        with pyautogui.hold('ctrlleft'):
            pyautogui.press('g')
        sleep(0.6)
        pyautogui.write('Nota de Compra servicos gerais')
        sleep(1.5)
        pyautogui.press('enter')


def aguardando_tela_carregar():
    verificar_top = pyautogui.locateOnScreen(
        'images/verificar_top.png', confidence=0.8)
    while verificar_top == None:
        sleep(0.5)
        verificar_top = pyautogui.locateOnScreen(
            'images/verificar_top.png', confidence=0.8)

    empresa = pyautogui.locateOnScreen('images/empresa.png', confidence=0.8)
    move_and_click(empresa)


def aguardando_nro_unico():
    numero_unico = pyautogui.locateOnScreen(
        'images/numero_unico.png', confidence=0.8)
    while numero_unico != None:
        sleep(0.5)
        numero_unico = pyautogui.locateOnScreen(
            'images/numero_unico.png', confidence=0.8)


def verificando_modo_tela():
    modo_formulario = pyautogui.locateOnScreen(
        'images/modo_formulario.png', confidence=0.8)
    sleep(1)
    if modo_formulario != None:
        move_and_click(modo_formulario)


def error():
    ok_error = pyautogui.locateOnScreen(
        'images/ok_entrada.png', confidence=0.8)
    while ok_error == None:
        sleep(1)
        ok_error = pyautogui.locateOnScreen(
            'images/ok_entrada.png', confidence=0.8)


def aguardando_salvar_item():
    sem_local = pyautogui.locateOnScreen(
        'images/sem_local.png', confidence=0.8)
    while sem_local == None:
        sleep(0.5)
        sem_local = pyautogui.locateOnScreen(
            'images/sem_local.png', confidence=0.8)


def add_anexo():
    opcoes = pyautogui.locateOnScreen('images/opcoes.png', confidence=0.8)
    move_and_click(opcoes)
    sleep(0.6)
    anexar = pyautogui.locateOnScreen('images/anexar.png', confidence=0.8)
    move_and_click(anexar)
    sleep(0.5)

    adicionar_anexo = pyautogui.locateOnScreen(
        'images/adicionar_anexo.png', confidence=0.8)
    while adicionar_anexo == None:
        sleep(0.5)
        adicionar_anexo = pyautogui.locateOnScreen(
            'images/adicionar_anexo.png', confidence=0.8)
    move_and_click(adicionar_anexo)

    verificar_anexo = pyautogui.locateOnScreen(
        'images/verificar_anexo.png', confidence=0.8)
    while verificar_anexo == None:
        sleep(0.5)
        verificar_anexo = pyautogui.locateOnScreen(
            'images/verificar_anexo.png', confidence=0.8)

    sleep(0.5)
    pyautogui.press('tab')
    pyautogui.write('NF')
    pyautogui.press('tab')
    pyautogui.press('enter')

    salvar_anexo = pyautogui.locateOnScreen(
        'images/salvar_anexo.png', confidence=0.8)
    while salvar_anexo == None:
        sleep(0.5)
        salvar_anexo = pyautogui.locateOnScreen(
            'images/salvar_anexo.png', confidence=0.8)


def salvar_confimar_nota():
    salvar = pyautogui.locateOnScreen('images/salvar.png', confidence=0.8)
    move_and_click(salvar)
    sleep(0.5)
    ok_anexo = pyautogui.locateOnScreen('images/ok_anexo.png', confidence=0.8)
    move_and_click(ok_anexo)

    confirmar = pyautogui.locateOnScreen(
        'images/confirmar.png', confidence=0.8)
    move_and_click(confirmar)

    

def verificando_liberador():
    verificando_liberador = pyautogui.locateOnScreen(
        'images/definir_liberador.png', confidence=0.8)
    while verificando_liberador == None:
        sleep(0.5)
        verificando_liberador = pyautogui.locateOnScreen(
            'images/definir_liberador.png', confidence=0.8)
        
def confirmando_liberador():
    definir_liberador = pyautogui.locateOnScreen(
        'images/definir_liberador.png', confidence=0.8)     
    move_and_click(definir_liberador)
    sleep(0.5)
    pyautogui.press('esc')
           

def finalizar_e_adicionar_outra_nota():
    sleep(0.5)
    adicionar_nota = pyautogui.locateOnScreen(
        'images/adicionar_nota.png', confidence=0.8)
    move_and_click(adicionar_nota)
    sleep(2)
