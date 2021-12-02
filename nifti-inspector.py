import nibabel as nib
import numpy as np
from batchviewer import view_batch


if __name__ == '__main__':
    
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

    # print shape and pixel dimension.
    print(img.shape)
    print(img.header["pixdim"][1:4])
    
    # extract the img.
    img = img.get_fdata()
    img = img.transpose(2, 0, 1)

    # visualize the volumes with the batch viewer.
    if mask_path != "":
        view_batch(img, mask, width=512, height=512)
    else:
        view_batch(img, width=512, height=512)
