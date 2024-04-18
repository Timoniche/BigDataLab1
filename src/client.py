import requests

from utils.common_utils import parent_dir


def main():
    img_path = parent_dir() + '/client_images/' + '000001.jpg'

    files = {
        'file': open(img_path, 'rb')
    }
    requests.post(
        url='http://localhost:8000/upload/',
        files=files,
    )


if __name__ == '__main__':
    main()
