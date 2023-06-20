bl_info = {
    "name": "Sago",
    "author": "Jacob",
    "description": "Quick access tools to speed up workflows",
    "location": "3d View > Tool shelf",
    "version": (0, 5, 4),
    "blender": (2, 93, 0),
    "support": "COMMUNITY",
    "category": "Generic"
}


import importlib
from .  ui import operators
from .  ui import panels
import bpy




files = [
    operators,
    panels
]

def register():
    for file in files:
        importlib.reload(file)
        file.register()

def unregister():
    for file in files:
        file.unregister()

if __name__ == "__main__":
    register()

