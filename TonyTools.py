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


def quickBool():  # Select two objects and run. Boolean modifier goes to active object and put first selection as the bool operator.

    selection_names = []
    for obj in bpy.context.selected_objects:
        selection_names.append(obj.name)

    if len(selection_names) <= 1:  #Testing selection
        print('You need two objects to make it work')
    elif len(selection_names) >= 3:
        print('More than two objects selected')  
    else:
        print('You are good')
       
        activeOb = bpy.context.active_object
        BoolOb = bpy.context.selected_objects[0]


        bpy.ops.object.modifier_add(type='BOOLEAN')  #Add the bool modifier to active and set the operator from first selection.
        activeOb.modifiers["Boolean"].object = BoolOb
        BoolOb.display_type = 'WIRE'
        renderBool()

def renderBool():        # Disable render properties for bool operators.
    BoolOb = bpy.context.selected_objects[0]
    BoolOb.hide_render = True
    BoolOb.cycles_visibility.camera = False
    BoolOb.cycles_visibility.transmission = False
    BoolOb.cycles_visibility.diffuse = False
    BoolOb.cycles_visibility.scatter = False
    BoolOb.cycles_visibility.glossy = False
    BoolOb.cycles_visibility.shadow = False

    
class renderBool(bpy.types.Operator):
    '''Tooltip'''
    bl_idname= 'myops.render_bool'
    bl_label = 'RenderBool'
    
    
    def execute(self, context):
        renderBool()
        return {"FINISHED"}

class quickBool(bpy.types.Operator):
    '''Tooltip'''
    bl_idname= 'myops.quick_bool'
    bl_label = 'QuickBool'
    
    
    def execute(self, context):
        quickBool()
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
        
        row = layout.row()
        row.operator("myops.quick_bool")
        
        return {"FINISHED"}
    
def register():
    bpy.utils.register_class(quickBool)
    bpy.utils.register_class(renderBool)
    bpy.utils.register_class(TonyTools_Panel)

def unregister():
    bpy.utils.unregister_class(quickBool)
    bpy.utils.unregister_class(renderBool)
    bpy.utils.unregister_class(TonyTools_Panel)
    
    
if __name__ == "__main__":
    register()
  



    
