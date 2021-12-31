bl_info = {
    "name": "Add-on Template",
    "description": "",
    "author": "p2or",
    "version": (0, 0, 3),
    "blender": (2, 80, 0),
    "location": "3D View > Tools",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

import os
import time
import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )



class TestPanel(Panel):



    bl_label = "test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mix'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Add object", icon= "CUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon="MESH_UVSPHERE")
        row = layout.row()
        row.operator("mesh.monkey_grid", icon="MONKEY")

        layout.separator()
        row.operator("mesh.subdivide", icon="MESH_GRID")

class ExtraRender(TestPanel, Panel):
    bl_idname = "TestPanel"
    bl_label = "Extra render settings"
  


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        row = layout.row()
        row.prop(mytool, "close_blender")
        row = layout.row()
        row.prop(mytool, "shutdown_computer")

        if (mytool.close_blender == True):
            bpy.app.handlers.render_complete.append(some_other_function)  
        
        if (mytool.shutdown_computer == True):
            bpy.app.handlers.render_complete.append(some_function)  



def some_other_function(dummy):
    print("Render complete")
    bpy.ops.wm.save_mainfile()
    bpy.ops.wm.quit_blender()


def some_function(dummy):
    print("Render complete")
    bpy.ops.wm.save_mainfile()
    time.sleep(2)
    os.system("shutdown /s /t 1")



 





def some_other_function(dummy):
    print("Render complete")
    bpy.ops.wm.save_mainfile()
    bpy.ops.wm.quit_blender()


def some_function(dummy):
    print("Render complete")
    bpy.ops.wm.save_mainfile()
    time.sleep(2)
    os.system("shutdown /s /t 1")

    
            



class MyProperties(PropertyGroup):

    close_blender: BoolProperty(
        name="close blender",
        description="A bool property",
        default = False
        )
        
    shutdown_computer: BoolProperty(
        name="Shut down computer",
        description="A bool property",
        default = False
        )



classes = (
MyProperties,
TestPanel,
ExtraRender,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()