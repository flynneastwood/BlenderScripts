import bpy

bpy.context.selected_objects

bpy.context.object.hide_render = True
bpy.context.object.cycles_visibility.camera = False
bpy.context.object.cycles_visibility.transmission = False
bpy.context.object.cycles_visibility.diffuse = False
bpy.context.object.cycles_visibility.scatter = False
bpy.context.object.cycles_visibility.glossy = False
bpy.context.object.cycles_visibility.shadow = False

bpy.context.object.display_type = 'WIRE'
