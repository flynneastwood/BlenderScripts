import bpy
import os
from bpy.types import Operator

class ExportGLTF(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.export_gltf"
    bl_label = "Exporting to GLTF"

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

        gltf_path = os.path.join(basedir, "GLTF") 
        if not os.path.exists(gltf_path):
            os.makedirs(gltf_path)
            
        #Export as GlTF
        bpy.ops.export_scene.gltf(filepath=fn + ".gltf", use_selection=True)

        #Set model nack to initial location
        selection.location.xyz = initialLocation
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportGLTF)


def unregister():
    bpy.utils.unregister_class(ExportGLTF)


if __name__ == "__main__":
    register()
