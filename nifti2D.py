import nibabel as nib
import numpy as np
from batchviewer import view_batch

from PIL import Image
from pathlib import Path
# use this if you want to normalize or denormalize the images.
def interval_mapping(image, from_min, from_max, to_min, to_max):
    # map values from [from_min, from_max] to [to_min, to_max]
    # image: input array
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled = np.array((image - from_min) / float(from_range), dtype=float)
    return to_min + (scaled * to_range)


if __name__ == '__main__':
    Path("2D").mkdir(parents=False, exist_ok=True)
    Path("2D/img").mkdir(parents=False, exist_ok=True)
    Path("2D/mask").mkdir(parents=False, exist_ok=True)
    
    # define the paths to the images.
    file_path = "img.nii.gz"
    mask_path = "mask.nii.gz"

    # loading the mask
    if mask_path != "":
        mask = nib.load(mask_path)
        # this takes the pixel data.
        mask = mask.get_fdata()
        mask = mask.transpose(2, 0, 1)
   
    # loading the image
    img = nib.load(file_path)

    # extract the img.
    img = img.get_fdata()
    img = img.transpose(2, 0, 1)

    # loop over z axis.
    for i in range(img.shape[0]):
        # convert to image.
        tmp_img = img[i]
        tmp_mask = mask[i]

        # do interval scaling to avoid artifacts.
        tmp_img = interval_mapping(tmp_img, tmp_img.min(), tmp_img.max(),0,255)
        tmp_img = tmp_img.astype(np.uint8)
        tmp_mask = tmp_mask.astype(np.uint8)
        # convert 1 to 255 to make the mask visible.
        print(tmp_mask.min(), tmp_mask.max())
        
        tmp_mask[tmp_mask == 1] = 255

        
        tmp_img = Image.fromarray(tmp_img)

        tmp_img.save("2D/img" + "/"+ str(i) + ".png")
        if tmp_mask.max() == 255:
            tmp_mask = Image.fromarray(tmp_mask)
            tmp_mask.save("2D/mask" + "/"+ str(i) + ".png")