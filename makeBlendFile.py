import bpy
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


def makeBlendFile(elements):
	
	filepath = bpy.data.filepath
	basedir = os.path.dirname(bpy.data.filepath)
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete(use_global=False)

	bpy.ops.import_scene.fbx(filepath=basedir + "/" + str(elements).strip("DirEntry "))

	selection = bpy.context.selectable_objects[0]
	prefix = "SM_"

	#Set the selection name as file name
	name = bpy.path.clean_name(prefix + selection.name)
	fn = os.path.join(basedir, name)

	bpy.ops.wm.save_as_mainfile(filepath=fn)

sortElements()
makeBlendFile(elements)