# -*- coding: utf-8 -*-
"""
Generate templates (template.md) for each box in LBB

@author: kampff
"""

# Import Libraries
import os
import glob

# Import modules
import LBB.Engine.config as Config

# Reload libraries and modules
import importlib
importlib.reload(Config)

# Generate templates
for box_name in Config.box_names:
    lessons_folder = f"{Config.boxes_root}/{box_name.lower()}/_lessons"
    lesson_paths = glob.glob(f"{lessons_folder}/*.md")
    template_path = f"{Config.boxes_root}/{box_name.lower()}/template.md"
    with open(template_path, "w") as file:
        file.write(f"# The Last Black Box : {box_name}\n")
        file.write(f"\n")
        file.write(f"## {box_name}{{11}}\n")
        file.write(f"\n")
        for lesson_path in lesson_paths:
            file.write(f"{{{os.path.basename(lesson_path)}}}\n")
        file.write(f"\n")
        file.write(f"---\n")
        file.write(f"\n")
        file.write(f"# Project\n")
        file.write(f"#### Name of the project\n")
        file.write(f"Project tasks listed here\n")
# FIN