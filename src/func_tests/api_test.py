import pathlib

from server import app
from fastapi.testclient import TestClient


class FunctionalApiTest:

    def __init__(
            self,
            client: TestClient,
    ) -> None:
        self.client = client

    def test_upload_photo(self):
        images_dir = str(pathlib.Path(__file__).resolve().parent.parent.parent)
        print(images_dir)
        img_path = images_dir + '/client_images/' + '000003.jpg'

        files = {
            'file': open(img_path, 'rb')
        }
        response = self.client.post(
            url='http://localhost:8000/upload/',
            files=files,
        )

        print(response)
        json = response.content.decode()
        print(json)

        assert response.status_code == 200
        ground_truth = '{"filename":"000003.jpg","is_male":"male"}'

        assert json == ground_truth, f'Expected {ground_truth}, got {json}'

        print('Test passed')


if __name__ == '__main__':
    mock_client = TestClient(app)
    api_test = FunctionalApiTest(mock_client)

    api_test.test_upload_photo()
