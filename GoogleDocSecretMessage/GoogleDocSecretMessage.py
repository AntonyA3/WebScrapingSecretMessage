
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_secret_message(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    rows = [[z.get_text() for z in v.findAll('td')] for v in soup.findAll('tr')]
    rows.pop(0)
    rows = [[int(item[0]), item[1].strip(), int(item[2])] for item in rows]
    max_x = max([item[0] for item in rows]) + 1;
    max_y = max([item[2] for item in rows]) + 1;
    output_array = [[' ' for x in range(max_x)] for y in range(max_y)]
    for row in rows:
        output_array[max_y - 1 - row[2]][row[0]] = row[1]
    message = '\n'.join([''.join(item) for item in output_array])
    print(message)


get_secret_message('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')