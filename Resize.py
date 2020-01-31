
## To Start, All you have to do is place this file in a location where you have all the screenshots for the resize. 
## Next, Navagate to location where this file is located in cmd. 
## Then run py Resize.py and wait a few seconds and boom. All the screenshots have been resized and added to a folder. 
## I hope this makes mass resizing quicker!!!
## Feel free to edit and rework the code for better use

## Delete All Created Folders from this proccess to start over. 

from PIL import Image
from resizeimage import resizeimage
import os
import shutil, os


##Create List of All Files
filelist = os.listdir()
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
print(filelist)

##Can Change file name or add to list
folderNames = ['IPhone6.5','Iphone5.5','Ipad3rdGen','Ipad2ndGen']
##Can Change Picture Diameters here, must have the same number of 
possibleSizes = [(1242 ,2688),(1242 ,2208),(2048,2732),(2048,2732)]
con = 0
# Possible Sizes https://help.apple.com/app-store-connect/#/devd274dd925
for p in folderNames:
   

    try:
        os.makedirs(p)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    for i in filelist:
        #read the image
        im = Image.open(i)

        #image size
        size=possibleSizes[con]
        out = im.resize(size)
        out.save(i)
        shutil.copy(i, p)
    con+=1
