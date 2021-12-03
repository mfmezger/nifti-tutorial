import numpy as np
from batchviewer import view_batch
import torch

if __name__ == '__main__':
    file_path = "data/img.pt"

    file = torch.load(file_path)

    img = file["vol"].numpy()
    mask = file["mask"].numpy()
    

    view_batch(img, mask, width=512, height=512)
