import webbrowser
from urllib.error import URLError

try:
    webbrowser.open('https://pudim.com.br')
    print('O site esta acessivel')
except URLError:
    print('O site esta inacessivel')