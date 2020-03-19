import bpy

selection_names = []
for obj in bpy.context.selected_objects:
    selection_names.append(obj.name)

if len(selection_names) <= 1:
    print('You need two objects to make it work')
elif len(selection_names) >= 3:
    print('More than two objects selected')  
else:
    print('You are good')
   
    activeOb = bpy.context.active_object
    BoolOb = bpy.context.selected_objects[0]


    bpy.ops.object.modifier_add(type='BOOLEAN')
    activeOb.modifiers["Boolean"].object = BoolOb
    BoolOb.display_type = 'WIRE'

    #bpy.context.selected_objects[0]

    BoolOb.hide_render = True
    BoolOb.cycles_visibility.camera = False
    BoolOb.cycles_visibility.transmission = False
    BoolOb.cycles_visibility.diffuse = False
    BoolOb.cycles_visibility.scatter = False
    BoolOb.cycles_visibility.glossy = False
    BoolOb.cycles_visibility.shadow = False
