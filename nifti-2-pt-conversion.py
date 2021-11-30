import nibabel as nib
import torch


if __name__ == '__main__':
    
    # define the paths to the images.
    file_path = ""
    mask_path = ""
    save_path = ""

    # loading the image
    img = nib.load(file_path)
    # extract the img.
    img = img.get_fdata()
    img = img.transpose(2, 0, 1)

    # loading the mask
    if mask is not "":
        mask = nib.load(mask_path)
        # extracting the mask. Mostly contains a volume with classes encoded as integer.
        # So e.g. 0 is Background and 1 is target.
        mask = mask.get_fdata()
        mask = mask.transpose(2, 0, 1)

    # convert the numpy array to tensor.
    image = torch.from_numpy(image)

    # change to fp16 to reduce the size. 
    # This step is not necessary and can be also removed, 
    # but could help with training on machines with not alot of VRAM.
    image = image.to(torch.float16)

    # create the path and name for the file to save.
    path = os.path.join(save_path , file_path.split("/")[-1].split(".")[0]  + ".pt")


    # save the volumes as torch files.
    if mask is not "":
        # applying the save processing to the images.
        mask = torch.from_numpy(mask)
        mask = mask.to(torch.int16)
        # saving the image with mask and it at the specified path.
        torch.save({"vol": image, "mask": mask, "id": 1}, path)
    else:
        # saving the image with mask and it at the specified path.
        torch.save({"vol": image, "id": 1}, path)
