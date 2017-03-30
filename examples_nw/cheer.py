#
# Adds cheering
#
#   numpad 9 - cheer
#


from pp import *

triggers = [
    (0, 0, 0, [
        (key_clicked, key_numpad_9),
    ], [
        (try_for_range, reg0, 0, 100),
            (multiplayer_send_string_to_server, 0, "str_music_calls"),
        (try_end),
    ]),
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
