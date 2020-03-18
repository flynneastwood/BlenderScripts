bl_info = {
    "name": "TonyTools",
    "author": "Antoine Flynn",
    "version": (1, 0),
    "blender": (2, 82, 0),
    "location": "View3D > Tab > Tony Tools",
    "description": "Workflow enhancer",
    "warning": "",
    "wiki_url": "",
    "category": "Tools",
}

import bpy


def main():

    bpy.context.selected_objects

    bpy.context.object.hide_render = True
    bpy.context.object.cycles_visibility.camera = False
    bpy.context.object.cycles_visibility.transmission = False
    bpy.context.object.cycles_visibility.diffuse = False
    bpy.context.object.cycles_visibility.scatter = False
    bpy.context.object.cycles_visibility.glossy = False
    bpy.context.object.cycles_visibility.shadow = False

    bpy.context.object.display_type = 'WIRE'
    
class RenderBool(bpy.types.Operator):
    '''Tooltip'''
    bl_idname= 'myops.render_bool'
    bl_label = 'Set Bool Render'
    
    
    def execute(self, context):
        main()
        return {"FINISHED"}

class TonyTools_Panel(bpy.types.Panel):
    """Creates a Panel in the Tool shelf"""
    bl_label = "Time Savers"
    bl_idname = "OBJECT_PT_RenderBool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tony Tools'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("myops.render_bool")
        return {"FINISHED"}
    
def register():
    bpy.utils.register_class(RenderBool)
    bpy.utils.register_class(TonyTools_Panel)

def unregister():
    bpy.utils.unregister_class(RenderBool)
    bpy.utils.unregister_class(TonyTools_Panel)
    
    
if __name__ == "__main__":
    register()
  
