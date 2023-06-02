import PySimpleGUI as sg
from PIL import Image

sg.theme('DarkAmber')
# Cria o layout com a imagem de fundo e os outros elementos da tela de login
layout = [
    [sg.Image(filename='######', pad=((56, 0), (10, 0)))],
    [sg.Text('Usuário', pad=((10,0),(10,20))), sg.Input(key='-USER-', size=(50,50))],
    [sg.Text('Senha', pad=((10,0),(10,20))), sg.Input(key='-PASS-', password_char='*', size=(20,50))],
    [sg.Text('')],
    [sg.Button('Entrar', size=(10, 2)), sg.Button('Cancelar', size=(10, 2))]
]


# Cria a janela
window = sg.Window('Bem Vindo ao Python', layout, element_justification='c', size=(500, 400))


# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event == 'Entrar':
        # Verifica se as credenciais de login estão corretas
        if values['-USER-'] == 'vagner@yahoo.com' and values['-PASS-'] == 'star':
            sg.popup('Login realizado com sucesso!')
            break
        else:
            sg.popup('Usuário ou senha incorretos')

# Fecha a janela
window.close()