#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
import re

# def get_hidden_files(base_url):
#     session = requests.Session()
#     def recursive_search(url):
#         try:
#             response = session.get(url)
#             soup = BeautifulSoup(response.text, 'html.parser')

#             dir_links = [link['href'] for link in soup.find_all('a', href=True) if link['href'].endswith('/')]

#             readme_link = next((link for link in soup.find_all('a') if link.text.lower() == 'readme'))
#             if readme_link:
#                 readme_url = url.rstrip('/') + '/' + readme_link['href']
#                 readme_response = session.get(readme_url)
#                 if readme_response.status_code == 200:
#                     print(readme_response.text)
#                     print("\n--\n")
#             for dir_link in dir_links:
#                 full_dir_url = url.rstrip('/') + '/' + dir_link.lstrip('/')
#                 recursive_search(full_dir_url)
#             time.sleep(1)
#         except Exception as e:
#             print(f"Error accessing {url}: {str(e)}")
    
#     recursive_search(base_url)
def normalize_url(base_url, rel_url):
    """Normalize URL by joining base URL and relative URL"""
    return urljoin(base_url, rel_url)

def is_absolute(url):
    """Check if URL is absolute"""
    return bool(urlparse(url).netloc)

def get_hidden_files(base_url, max_depth=10):
    session = requests.Session()
    
    def recursive_search(url, current_depth=0):
        try:
            
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            readme_link = next((link for link in soup.find_all('a') if link.text.lower() == 'readme'), None)
            if readme_link:
                readme_url = normalize_url(url, readme_link['href'])
                
                readme_response = session.get(readme_url)
                if readme_response.status_code == 200:
                    try:
                        readme_contents = readme_response.text
                        digit_lines = [line.strip() for line in readme_contents.split('\n') if re.search(r'\d', line)]
                        
                        if digit_lines:
                            print(f"README contents:\n{readme_response.text}\n")
                            for line in digit_lines:
                                print(f"> {line}")
                    except Exception as e:
                        print(f"Error parsing README contents: {str(e)}")
            
            dir_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.endswith('/') and not is_absolute(href):
                    dir_links.append(normalize_url(url, href))
            
            if current_depth < max_depth:
                for dir_link in set(dir_links):
                    recursive_search(dir_link, current_depth + 1)
            
            time.sleep(1)
            
        except Exception as e:
            print(f"Error accessing {str(e)}")
    
    recursive_search(base_url)

if __name__ == '__main__':
    base_url = "http://192.168.56.3/.hidden/"
    get_hidden_files(base_url)