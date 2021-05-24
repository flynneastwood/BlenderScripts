import bpy
from bpy.props import*



class GenLodOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.generate_lods"
    bl_label = "Generate LODs"
    bl_options = {"REGISTER", "UNDO"}

    
    lods_numbers : IntProperty(
        name = "Number of LODs",
        description = "Number of LODs to generate",
        default = 3,
        min = 1,
        max = 6    
    )
    
    def execute(self, context):
        sel = bpy.context.active_object

        lodNumbers = self.lods_numbers

        for i in range(lodNumbers):
    
            new_obj = sel.copy()
            
            #Add decimate modifier
            decimateModifier = new_obj.modifiers.new(name="Decimate", type='DECIMATE')
            decimateModifier.ratio = 0.5 / (i + 1)
            
            #Offsets the position
            new_obj.location.y = 5 * (i + 1)

            #Change the name of the new object
            rename = new_obj.name.replace(".00", "")
            suffix = "_LOD" + str(i + 1)
            new_obj.name = rename + suffix
            
            #Add the result to scene
            bpy.data.collections["Collection"].objects.link(new_obj)        
        
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(GenLodOperator)


def unregister():
    bpy.utils.unregister_class(GenLodOperator)


if __name__ == "__main__":
    register()


