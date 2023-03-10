from urllib.error import URLError
import urllib.request
url = 'http://pudim.com.br'

try:
    status_code = urllib.request.urlopen(url).getcode()
    print(f'O site Pudim está funcionando.')
except URLError:
    print(f'O site Pudim não está funcionando.')