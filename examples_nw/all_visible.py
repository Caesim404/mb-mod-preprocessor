#
# Makes all invisible object visible
#

from pp import *

i = 0
for scene_prop in scene_props:
    if scene_prop[1] & sokf_invisible == sokf_invisible:
        scene_props[i] = (scene_prop[0], scene_prop[1] ^ sokf_invisible) + scene_prop[2:]
    i += 1
