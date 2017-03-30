#
# Allows spyglass animation with any weapn
#
#   numpad 6 - toggle spyglass anumation
#


from pp import *

triggers = [
    (0, 0, 0, [
        (key_clicked, key_numpad_6),
    ], [
        (try_begin),
            (call_script, "script_client_get_my_agent"),
            (agent_is_active, reg0),
            (agent_get_animation, ":anim", reg0, 1),
            (eq, ":anim", "anim_spyglass"),
            (multiplayer_send_2_int_to_server,multiplayer_event_send_player_action,player_action_spyglass,spyglass_type_stop),
        (else_try),
            (multiplayer_send_2_int_to_server,multiplayer_event_send_player_action,player_action_spyglass,spyglass_type_start),
        (try_end),
    ]),
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
