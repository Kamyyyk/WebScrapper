import requests
from bs4 import BeautifulSoup

URL = 'https://www.olx.pl/noclegi/'


# OLX
div_ogloszenia = 'offer-wrapper'
stopka_ogloszenia = 'bottom-cell'
nazwa_ogloszenia = 'title-cell'
miejsce = 'breadcrumb'
cena = 'price'


# Iteracja po strukturze strony
def page_parser(num):
    f = open(f'Strona{num}.txt', 'w')
    f.write(f'Strona {num}:\n')
    page_olx = requests.get(f'{URL}?page={num}')
    bs = BeautifulSoup(page_olx.content, 'html.parser')
    for offer in bs.find_all('div', div_ogloszenia):
        footer = offer.find('td', stopka_ogloszenia)
        place = footer.find('small', miejsce).get_text().strip()
        name = offer.find('strong').get_text().strip()
        price = offer.find('p', cena).get_text().strip()
        link = offer.find('a')
        f.write(f'{name} Miejscowosc: {place} Cena: {price}\n')
        f.write(f'{link["href"]}\n')


if __name__ == '__main__':
    for page_num in range(1, 5):
        page_parser(page_num)


