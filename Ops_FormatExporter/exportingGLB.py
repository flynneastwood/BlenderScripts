import bpy
import os
from bpy.types import Operator

class ExportGLB(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.export_glb"
    bl_label = "Exporting to GLB"

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

        glb_path = os.path.join(basedir, "GLB") 
        if not os.path.exists(glb_path):
            os.makedirs(glb_path)
            
        #Export as GlTF
        bpy.ops.export_scene.gltf(filepath=fn + ".glb", use_selection=True)

        #Set model nack to initial location
        selection.location.xyz = initialLocation
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportGLB)


def unregister():
    bpy.utils.unregister_class(ExportGLB)


if __name__ == "__main__":
    register()
