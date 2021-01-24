from PIL import Image
import glob
import os

lst_imgs = [i for i in glob.glob("*.jpg")]#add preferred image extension here 
 
# It creates a folder called ltl if does't exist
if not "Resized Folder" in os.listdir():
	os.mkdir("Resized Folder")
 
print(lst_imgs)
for i in lst_imgs:
	img = Image.open(i)
	img = img.resize((7632, 6480), Image.ANTIALIAS) #Add image dimensions here
	img.save("Resized folder\\" + i[:-4] + "_new.png")
 
 
print("Done")
os.startfile("Resized Folder")