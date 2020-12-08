import bpy

for ob in bpy.context.selectable_objects:
    print(ob.name)
