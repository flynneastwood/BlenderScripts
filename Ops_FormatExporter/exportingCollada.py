import bpy
import os
from bpy.types import Operator

class ExportCollada(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.export_collada"
    bl_label = "Exporting to COLLADA"

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

        dae_path = os.path.join(basedir, "DAE") 
        if not os.path.exists(dae_path):
            os.makedirs(dae_path)
            
        #Export as COLLADA
        bpy.ops.wm.collada_export(filepath=fn, apply_modifiers=True)

        #Set model nack to initial location
        selection.location.xyz = initialLocation
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportCollada)


def unregister():
    bpy.utils.unregister_class(ExportCollada)


if __name__ == "__main__":
    register()
