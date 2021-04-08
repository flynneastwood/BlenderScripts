import os

path = os.getcwd()
elements = []

def sortElements():
	with os.scandir(path) as listOfEntries:
	    for entry in listOfEntries:
	        # print all entries that are files
	        if not entry.name.endswith(".fbx"):
	            continue
	        else:
	        	elements.append(entry)

sortElements()
newlist = str(elements)
newlist.strip("DirEntry")
print(newlist)
