import os
from batchviewer import view_batch

import numpy as np
import torch
from scipy.ndimage.filters import gaussian_filter
from torch.utils.data import Dataset


class TorchDataSet(Dataset):
    """
    Loading the Datasets
    """

    def __init__(self, directory):
        self.directory = directory
        self.images = os.listdir(directory)

    def __len__(self):
        return len(self.directory)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # load the image and the groundtruth
        name = self.images[idx]
        file = torch.load(os.path.join(self.directory, name))

        image = file["vol"]
        mask = file["mask"]

        # change the datatype to float32 if you do not use FP16.
        image = image.to(torch.float32)
        mask = mask.to(torch.float32)

        return image, mask


if __name__ == '__main__':
    dataset = TorchDataSet(directory="data/")
    img, mask = dataset[0]
    print(img.shape)

    view_batch(img, mask,  height=512, width=512)