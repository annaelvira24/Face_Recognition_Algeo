from differ import *
import os

images_path = "PINS"
dirs = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
files = [os.path.join(dirs[i], os.listdir(dirs[i])[0]) for i in range(len(dirs))]

for i in range(len(files)):
	open("TC/test"+str(i)+".jpg","wb").write(open(files[i],"rb").read())
d = Differ('TC/','huhu.pck')
d.findUselessVector()