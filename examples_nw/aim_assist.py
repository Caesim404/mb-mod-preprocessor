#
# Reduces size of reticle
#
#   j - turn on
#

from pp import *

triggers = [
    (0, 0, 0, [
        (key_clicked, key_j),
    ], [
        (call_script, "script_client_get_my_agent"),
        (agent_is_active, reg0),
        
        (display_message, "@Changing accuracy"),
        (agent_set_accuracy_modifier, reg0, 1000)
    ]),
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
