import bpy




class OBJECT_OT_EzSmoother(bpy.types.Operator):
    """Toggles on the EzSmoother"""
    bl_label = "EzSmooth"
    bl_idname = "object.ez_smoother"

    bl_options = {'REGISTER', 'UNDO'}
    
    smoothnessAngle = bpy.props. FloatProperty(
        name = "Smoothness",
        default = 0.7853,
        description = "Smoothing angle"
        )
     
     
    def execute(self, context):
            
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = self.smoothnessAngle

                
        return{'FINISHED'}
    
    
#class smooth_monkey_panel

def add_object_button(self, context):
    self.layout.operator(
    OBJECT_OT_EzSmoother.bl_idname,
    icon = "MESH_MONKEY"
    )

#registration

def register():
    bpy.utils.register_class(OBJECT_OT_EzSmoother)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_EzSmoother)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)

if __name__ == "__main__":
    register()
