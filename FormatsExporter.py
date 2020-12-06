import bpy
import os

#Get the blender file directory
basedir = os.path.dirname(bpy.data.filepath)

#Get initial location and resets it before export
selection =  bpy.context.active_object
initialLocation = selection.location.copy()
selection.location.xyz = 0

#Set the selection name as file name
name = bpy.path.clean_name(selection.name)
fn = os.path.join(basedir, name)


#Export as COLLADA
bpy.ops.wm.collada_export(filepath=fn)
#Export as FBX
bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)
#Export as OBJ
bpy.ops.export_scene.obj(filepath=fn + ".obj", use_selection=True)
#Export as STl
bpy.ops.export_mesh.stl(filepath=fn + ".stl", use_selection=True)
#Export as GlTF
bpy.ops.export_scene.gltf(filepath=fn + ".gltf", use_selection=True)



#Set model nack to initial location
selection.location.xyz = initialLocation


