#
# Spams kicked for cheating message
#
#   end - activate
#


from pp import *

triggers = [
    (0, 0, ti_once, [], [
        (assign, "$caesim_cheat_msg_spam", 0),
    ]),
    (0, 0, 0, [
        (key_clicked, key_end),
    ], [
        (assign, "$caesim_cheat_msg_spam", 1),
        (display_message, "@Cheating..."),
    ]),
    (0, 0, 0, [
        (eq, "$caesim_cheat_msg_spam", 1),
    ], [
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
        (multiplayer_send_int_to_server, multiplayer_event_send_player_action, player_action_has_cheat),
    ]),
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
