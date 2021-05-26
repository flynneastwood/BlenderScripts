import bpy
import os
from bpy.types import Operator

class ExportFBX(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.export_fbx"
    bl_label = "Exporting to FBX"

    def execute(self, context):
        #Get the blender file directory
        basedir = os.path.dirname(bpy.data.filepath)


        #Get initial location and resets it before export
        selection =  bpy.context.active_object
        initialLocation = selection.location.copy()
        selection.location.xyz = 0

        #Set the selection name as file name
        name = bpy.path.clean_name(selection.name)
        fn = os.path.join(basedir, name)

        fbx_path = os.path.join(basedir, "FBX") 
        if not os.path.exists(fbx_path):
            os.makedirs(fbx_path)
            
        #Export as FBX
        bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)

        #Set model nack to initial location
        selection.location.xyz = initialLocation
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportFBX)


def unregister():
    bpy.utils.unregister_class(ExportFBX)


if __name__ == "__main__":
    register()
