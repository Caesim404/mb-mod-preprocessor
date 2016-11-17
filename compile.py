#!/bin/python2

import sys, os, imp, string

SCRIPT_DIR = "scripts"

def template(vars, code):
    result = []
    for i in range(len(vars.values()[0])):
        for line in code:
            line2 = ()
            if type(line) == tuple:
                for exp in line:
                    if type(exp) == str:
                        if exp[0:1] == "~":
                            exp = eval(string.Template(exp[1:]).safe_substitute({var: vars[var][i] for var in vars}))
                        else:
                            exp = string.Template(exp).safe_substitute({var: vars[var][i] for var in vars})
                    line2 += (exp,)
            else:
                line2 = line
            result.append(line2)
    return result

variables = {"template": template}

print "Importing modules ..."
for file in os.listdir('.'):
    if (file.startswith("module_") or file.startswith("header_") or file.startswith("ID_")) and file.endswith(".py"):
        variables.update(vars(__import__(file[:-3])))

interface = imp.new_module("pp")
vars(interface).update(variables)
sys.modules["pp"] = interface

sys.path.insert(0, SCRIPT_DIR)

for file in os.listdir(SCRIPT_DIR):
    if file.endswith(".py"):
        print "Processing", file, "..."
        __import__(file[:-3])


import process_init
import process_global_variables
import process_strings
import process_skills
import process_music
# Animation processing ruins the animation list  :/
animation_names = [x[0] for x in sys.modules["module_animations"].animations]
import process_animations
i = 0
for animation in sys.modules["module_animations"].animations:
    animation[0] = animation_names[i]
    i += 1
import process_meshes
import process_sounds
import process_skins
import process_map_icons
import process_factions
import process_items
import process_scenes
import process_troops
import process_particle_sys
import process_scene_props
import process_tableau_materials
import process_presentations
import process_party_tmps
import process_parties
import process_quests
import process_info_pages
import process_scripts
import process_mission_tmps
import process_game_menus
import process_simple_triggers
import process_dialogs
import process_global_variables_unused
import process_postfx