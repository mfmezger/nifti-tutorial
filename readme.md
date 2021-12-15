# Nifti Data Handeling Tutorial for PyTorch 

Nifti Dataending is .nii or .nii.gz.

## Installation on Linux

Download the repository.

`git clone https://github.com/mfmezger/nifti-tutorial.git`

Install the requirements.txt.

```
cd nifti-tutorial  
pip install -r requirements.txt
```

## Nifti Inspector
You can use the Nifti Inspector to visualize the Nifti Files with the Batchviewer Libary. (https://github.com/FabianIsensee/BatchViewer)

### Installation of Batch Viewer

```
git clone https://github.com/FabianIsensee/BatchViewer.git
cd BatchViewer
pip install . 
```

## Visualize niftis using Fiji

It is also possible to inspect the images using Fiji. 

`https://imagej.net/software/fiji/`

Just install Fiji, then you can open the images easily by choosing File -> Open. If you want to open Dicom Images you have to open it as File -> Import -> Image Sequence.

## Nifti to Pytorch File Converter

You can use this script to convert a nifti image with or without mask to a pytorch file (.pt). Just run: 
```python nifti-2-pt-conversion.py```


## Torch inspector

This script allows to visualize the data that was created with the  
```python nifti-2-pt-conversion.py```.


## Nifti2D

This script converts a 3D Volume in 2D slices and from there into PNG Images. 
```python nifti2D.py```

