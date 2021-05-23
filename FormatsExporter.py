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

dae_path = os.path.join(basedir, "DAE") 
if not os.path.exists(dae_path):
    os.makedirs(dae_path)
    
fbx_path = os.path.join(basedir, "FBX") 
if not os.path.exists(fbx_path):
    os.makedirs(fbx_path)
    
gltf_path = os.path.join(basedir, "GLTF") 
if not os.path.exists(gltf_path):
    os.makedirs(gltf_path)
    
obj_path = os.path.join(basedir, "OBJ") 
if not os.path.exists(obj_path):
    os.makedirs(obj_path)
    
stl_path = os.path.join(basedir, "STL") 
if not os.path.exists(stl_path):
    os.makedirs(stl_path)
    
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
