import pathlib
import unittest

import numpy as np

from images_dataset import hog_embedding


class TestHogEmbeddings(unittest.TestCase):

    def setUp(self) -> None:
        images_dir = str(pathlib.Path().resolve().parent.parent)
        self.img_path = images_dir + '/client_images/' + '000001.jpg'

    def test_hog_embeddings(self):
        hog_embs = hog_embedding(self.img_path)

        with open('./ground_truth/hog_embeddings.txt', 'r') as f:
            embs = f.readline()
            ground_truth = list(map(float, embs.split()))

        print(hog_embs[0])
        print(ground_truth[0])
        print(len(hog_embs), len(ground_truth))

        np.testing.assert_almost_equal(ground_truth, hog_embs, decimal=5)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
