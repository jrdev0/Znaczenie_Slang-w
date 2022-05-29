import requests
from bs4 import BeautifulSoup


def pobranie_strony(co_to):

    headers = {'User_Agent': 'your user agent'}
    wyszukaj = f'https://www.miejski.pl/slowo-{co_to}'
    r = requests.get(wyszukaj, headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup


def slang(soup):
    lista = []
    opis = soup.find_all('main')
    for op in opis:
        # mayby to use in future...

        slowo = op.find('h1').text
    #     try:
    #         ocena = str(op.find('span', class_='rating').text).replace('  ', '').replace("'", "")
    #     except AttributeError:
    #         ocena = ''
        rezultat = str(op.p.text).replace('  ', '').replace('\r\n', '').replace('\n', '').replace("'", "")
        try:
            przyklad = str(op.find('blockquote').text).replace('\r\n', '').replace('\n', '').replace('  ', '').replace('!2', '. Przykład 2').replace('"', '').replace('***', '')
        except AttributeError:
            przyklad = ''
        if 'której szukasz' in rezultat:
            lol = str({rezultat})
            lol = lol.replace('{', ' ').replace("}", ' ').replace('[', '').replace("[", "").replace('Strona, której szukasz nie istnieje', 'Brak znaczenia tego słowa bazie danych')
        else:
            lol = {
                ' ': slowo,
                '': rezultat,
                'przykład ': przyklad

            }
        lista.append(lol)
    list2 = str(lista).replace("{", "").replace("}", "").replace("'", "")

    return list2


def slang_wykonanie(slowo):

    x = pobranie_strony(slowo)
    rezult = slang(x)

    return str(rezult)
