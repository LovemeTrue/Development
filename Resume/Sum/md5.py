from scr import *
import json

md5_hash = md5_dir("Sum/md")
print(md5_hash)

with open("Sum/changes.json", "r") as file:
    try:
        dataZ = json.load(file)
    except:
        dataZ = []
   
with open("Sum/changes.json","w") as file:
        dataZ.append(md5_hash)
        json.dump(dataZ, file)


# with open("Sum/changes.json", "r") as file:
#    try:
#        dataZ = json.load(file)
#    except:
#        dataZ = []
#    
#with open("Sum/changes.json","w") as file:
#    dataZ.append(hashDirs)
#    json.dump(dataZ, file)