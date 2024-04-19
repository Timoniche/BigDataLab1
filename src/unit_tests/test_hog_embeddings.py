import os
import pathlib
import sys
import unittest

import numpy as np

sys.path.insert(1, os.path.join(os.getcwd(), "src"))

from images_dataset import hog_embedding  # noqa: E402


class TestHogEmbeddings(unittest.TestCase):

    def setUp(self) -> None:
        images_dir = str(pathlib.Path(__file__).resolve().parent.parent.parent)
        print('images dir ', images_dir)
        self.img_path = images_dir + '/client_images/' + '000001.jpg'

        gt = '/Users/timoniche/Documents/BigData/mle-template/client_images/000001.jpg'
        assert '/Users/timoniche/Documents/BigData/mle-template/client_images/000001.jpg' == self.img_path, f'{gt} and {self.img_path}'
        print(self.img_path)

    def test_hog_embeddings(self):
        hog_embs = hog_embedding(self.img_path)

        cur_dir = str(pathlib.Path(__file__).resolve().parent)
        print('EEEE ', cur_dir)
        with open(f'{cur_dir}/ground_truth/hog_embeddings.txt', 'r') as f:
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
