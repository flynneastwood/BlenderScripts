import bpy
import os
from bpy.types import Operator

class ExportSTL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.export_stl"
    bl_label = "Exporting to STL"

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

        stl_path = os.path.join(basedir, "STL") 
        if not os.path.exists(stl_path):
            os.makedirs(stl_path)
            
        #Export as STl
        bpy.ops.export_mesh.stl(filepath=fn + ".stl", use_selection=True, use_mesh_modifiers=True)

        #Set model nack to initial location
        selection.location.xyz = initialLocation
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportSTL)


def unregister():
    bpy.utils.unregister_class(ExportSTL)


if __name__ == "__main__":
    register()
