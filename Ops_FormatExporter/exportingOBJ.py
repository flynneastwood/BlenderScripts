import bpy
import os
from bpy.types import Operator

class ExportOBJ(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.export_obj"
    bl_label = "Exporting to OBJ"

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

        obj_path = os.path.join(basedir, "OBJ") 
        if not os.path.exists(obj_path):
            os.makedirs(obj_path)
            
        #Export as OBJ
        bpy.ops.export_scene.obj(filepath=fn + ".obj", use_selection=True, use_mesh_modifiers=True)

        #Set model nack to initial location
        selection.location.xyz = initialLocation
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportOBJ)


def unregister():
    bpy.utils.unregister_class(ExportOBJ)


if __name__ == "__main__":
    register()
