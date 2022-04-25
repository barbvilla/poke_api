import webbrowser
import os
import time


def show_pics(html, nombre):
    with open(f'{nombre}.html','w',encoding = 'utf-8') as f:
        f.write(html)
    print('Las fotos se mostrarán en tu Navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')
    