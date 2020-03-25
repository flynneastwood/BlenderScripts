import bpy

C = bpy.context 
D = bpy.data


bpy.ops.object.select_grouped(type='TYPE')


lights = C.selected_objects
sel = C.active_object


for ob in lights:
    if ob.type != "LIGHT":
        print("Something else than a light is selected")
        bpy.ops.object.select_all(action='DESELECT')
        break
    elif ob != sel:
        ob.hide_set(True)
