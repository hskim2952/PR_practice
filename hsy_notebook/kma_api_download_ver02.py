import requests


def download_file(file_url, save_path):
    with open(save_path, 'wb') as f:
        response = requests.get(file_url)
        f.write(response.content)


url = "https://apihub.kma.go.kr/api/file?authKey=YOUR_AUTH_KEY"
save_file_path = "output_file.zip"

download_file(url, save_file_path)
