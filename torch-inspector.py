import numpy as np
from batchviewer import view_batch
import torch

if __name__ == '__main__':
    file_path = "data/img.pt"

    file = torch.load(file_path)

    img = file["vol"].numpy()
    mask = file["mask"].numpy()

    # print min and max values.
    print("max:", np.max(img))
    print("min:", np.min(img))
    

    view_batch(img, mask, width=512, height=512)
