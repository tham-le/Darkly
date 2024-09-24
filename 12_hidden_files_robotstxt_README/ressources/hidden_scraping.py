import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin, urlparse
import re


def normalize_url(base_url, rel_url):
    return urljoin(base_url, rel_url)

def is_absolute(url):
    return bool(urlparse(url).netloc)

def save_readme_content(readme_text, filename):
    with open(filename, 'a') as f:
        f.write(readme_text)

def extract_flags(text):
    alphanum_pattern = re.compile(r'\b(?=\w*[0-9])\w+\b')
    return alphanum_pattern.findall(text)

def get_hidden_files(base_url, output_file='./all_readme.txt'):
    session = requests.Session()
    visited_urls = set()
    url_queue = deque([base_url])
    all_flags = []

    while url_queue:
        try:
            url = url_queue.popleft()
            if url in visited_urls:
                continue
            
            visited_urls.add(url)
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            
            readme_link = soup.find('a', string=lambda t: t and t.lower() == 'readme')
            if readme_link:
                readme_url = normalize_url(url, readme_link['href'])
                
                readme_response = session.get(readme_url)
                if readme_response.status_code == 200:
                    readme_text = readme_response.text
                    save_readme_content(readme_response.text, output_file)
                    flags = extract_flags(readme_text)
                    all_flags.extend(flags)
            
            dir_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.endswith('/') and not is_absolute(href):
                    dir_links.append(normalize_url(url, href))
            
            url_queue.extend(dir_links)
        except Exception as e:
            print(f"Error accessing {url}: {str(e)}")
    return all_flags    


if __name__ == '__main__':
    base_url = "http://192.168.56.3/.hidden/"
    output_file = './all_readme.txt'
    
    open(output_file, 'w').close()
    flag = get_hidden_files(base_url)
    print(flag)
