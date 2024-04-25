import time
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_page_content(url):
    headers = {
        'User-Agent': 'my_crawler (brandon.loorits@ut.ee) / for_study_purpose',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Päring lehele {url} ebaõnnestus. Staatuskood: {response.status_code}')
        return None
    

main_url = 'https://nasdaqbaltic.com/statistics/et/shares'
shares = []

# Kogume kokku kõik url-id
print(f'Külastan lehte: {main_url}')
time.sleep(5)  # Viiteaeg, et ei ummistaks lehte
page_content = get_page_content(main_url)
if page_content:
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find('table')  # Leiame tabeli ID alusel
    if table:
        links = [a['href'] for a in table.find_all('a', href=True, class_="text16 compname") if a['href'].startswith('/statistics/et/instrument')]
        shares.append({'url': main_url, 'links': links})
    else:
        print('Ei leitud tabelit ID-ga "tablesaw-3709".')
else:
    print('Algse lehe külastamine ebaõnnestus.')
    
print(len(shares[0]['links']))
#print(soup.find('form'))

# Külastame leitud linke
for link in visited_pages[0]['links']:
    absolute_link = f'https://et.wikipedia.org{link}'
    print(f'Külastan lehte: {absolute_link}')
    time.sleep(5)  # Wait for 5 seconds before the next request
    page_content = get_page_content(absolute_link)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        images = []
        for figure in soup.find_all('figure'):
            if figure.find('img'):
                images.append(figure.find('img')['src'])
        found_images[absolute_link] = images
    else:
        print(f'Lehe külastamine ebaõnnestus: {absolute_link}')
print(found_images)


#response = requests.get('https://nasdaqbaltic.com/statistics/et/shares')
