import requests
from bs4 import  BeautifulSoup

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/59/vitoriadaconquista-ba").content

print(html)
soup = BeautifulSoup(html, 'html.parser')
Tempo_minimo = soup.find(id="min-temp-1")
print(f'A temperatura minima é: {Tempo_minimo.text}')

Tempo_minimo = soup.find(id="max-temp-1")
print(f'A temperatura máxima é: {Tempo_minimo.text}')

resumo = soup.find(class_='-gray -line-height-24 _center')
resumo_texto = resumo.text.replace('\n', ' ')
print(f'Meu resumo: {resumo_texto}')
