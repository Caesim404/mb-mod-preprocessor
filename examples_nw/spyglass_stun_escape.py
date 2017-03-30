#
# Helps escape stuns
#
#     numpad 8 - toggle
#

from pp import *

triggers = [
    (0, 0, 0, [
        (key_clicked, key_numpad_8),
    ], [
        (try_begin),
            (eq, "$caesim_spyglass_stun_esc", 1),
            (assign, "$caesim_spyglass_stun_esc", 0),
            (display_message, "@Stun esc OFF"),
        (else_try),
            (assign, "$caesim_spyglass_stun_esc", 1),
            (display_message, "@Stun esc ON"),
        (try_end),
    ]),
    (0, 0, 0, [], [
        (call_script, "script_client_get_my_agent"),
        (agent_is_active, reg0),
        (agent_get_animation, ":anim", reg0, 1),
        
        (try_begin),
            (eq, "$caesim_parry_esc_initiated", 1),
            (eq, ":anim", "anim_spyglass"),
            (multiplayer_send_2_int_to_server,multiplayer_event_send_player_action,player_action_spyglass,spyglass_type_stop),
            (assign, "$caesim_parry_esc_initiated", 0),
        (else_try),
            (eq, "$caesim_spyglass_stun_esc", 1),
            (this_or_next|eq, ":anim", "anim_blocked_swingright_fist"),
            (this_or_next|eq, ":anim", "anim_parried_swingright_fist"),
            (this_or_next|eq, ":anim", "anim_blocked_swingleft_fist"),
            (this_or_next|eq, ":anim", "anim_parried_swingleft_fist"),
            (this_or_next|eq, ":anim", "anim_blocked_direct_fist"),
            (this_or_next|eq, ":anim", "anim_parried_direct_fist"),
            (this_or_next|eq, ":anim", "anim_blocked_uppercut_fist"),
            (this_or_next|eq, ":anim", "anim_parried_uppercut_fist"),
            (this_or_next|eq, ":anim", "anim_blocked_slashright_twohanded"),
            (this_or_next|eq, ":anim", "anim_parried_slashright_twohanded"),
            (this_or_next|eq, ":anim", "anim_blocked_slashleft_twohanded"),
            (this_or_next|eq, ":anim", "anim_parried_slashleft_twohanded"),
            (this_or_next|eq, ":anim", "anim_blocked_thrust_twohanded"),
            (this_or_next|eq, ":anim", "anim_parried_thrust_twohanded"),
            (this_or_next|eq, ":anim", "anim_blocked_overswing_twohanded"),
            (this_or_next|eq, ":anim", "anim_parried_overswing_twohanded"),
            (this_or_next|eq, ":anim", "anim_blocked_thrust_onehanded"),
            (this_or_next|eq, ":anim", "anim_parried_thrust_onehanded"),
            (this_or_next|eq, ":anim", "anim_blocked_thrust_onehanded_horseback"),
            (this_or_next|eq, ":anim", "anim_parried_thrust_onehanded_horseback"),
            (this_or_next|eq, ":anim", "anim_blocked_thrust_onehanded_lance"),
            (this_or_next|eq, ":anim", "anim_parried_thrust_onehanded_lance"),
            (this_or_next|eq, ":anim", "anim_blocked_slashright_onehanded"),
            (this_or_next|eq, ":anim", "anim_parried_slashright_onehanded"),
            (this_or_next|eq, ":anim", "anim_blocked_slashleft_onehanded"),
            (this_or_next|eq, ":anim", "anim_parried_slashleft_onehanded"),
            (this_or_next|eq, ":anim", "anim_blocked_overswing_onehanded"),
            (this_or_next|eq, ":anim", "anim_parried_overswing_onehanded"),
            (this_or_next|eq, ":anim", "anim_blocked_slash_horseback_right"),
            (this_or_next|eq, ":anim", "anim_parried_slash_horseback_right"),
            (this_or_next|eq, ":anim", "anim_blocked_slash_horseback_left"),
            (this_or_next|eq, ":anim", "anim_parried_slash_horseback_left"),
            (this_or_next|eq, ":anim", "anim_blocked_slash_horseback_polearm_right"),
            (this_or_next|eq, ":anim", "anim_parried_slash_horseback_polearm_right"),
            (this_or_next|eq, ":anim", "anim_blocked_slash_horseback_polearm_left"),
            (this_or_next|eq, ":anim", "anim_parried_slash_horseback_polearm_left"),
            (this_or_next|eq, ":anim", "anim_blocked_overswing_staff"),
            (this_or_next|eq, ":anim", "anim_parried_overswing_staff"),
            (this_or_next|eq, ":anim", "anim_blocked_thrust_staff"),
            (this_or_next|eq, ":anim", "anim_parried_thrust_staff"),
            (this_or_next|eq, ":anim", "anim_blocked_slashleft_staff"),
            (this_or_next|eq, ":anim", "anim_parried_slashleft_staff"),
            (this_or_next|eq, ":anim", "anim_blocked_slashright_staff"),
            (this_or_next|eq, ":anim", "anim_parried_slashright_staff"),
            (this_or_next|eq, ":anim", "anim_blocked_overswing_spear"),
            (this_or_next|eq, ":anim", "anim_parried_overswing_spear"),
            (this_or_next|eq, ":anim", "anim_blocked_overswing_musket"),
            (this_or_next|eq, ":anim", "anim_parried_overswing_musket"),
            (this_or_next|eq, ":anim", "anim_blocked_thrust_musket"),
            (eq, ":anim", "anim_parried_thrust_musket"),
            (multiplayer_send_2_int_to_server,multiplayer_event_send_player_action,player_action_spyglass,spyglass_type_start),
            (assign, "$caesim_parry_esc_initiated", 1),
        (try_end),
    ])
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
