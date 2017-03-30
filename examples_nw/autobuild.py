#
# Allows autobuilding sapper props
#
#   / - toggles build spam
#   * - changes prop to spam
#

from pp import *

triggers = [
    (0, 0, ti_once, [], [
        (assign, "$caesim_autobuild", 0),
        (assign, "$caesim_buildpoints_sent", 0),
        (assign, "$caesim_build_prop", "spr_mm_stakes_construct"),
    ]),
    
    (0, 0, 0, [
        (key_clicked, key_numpad_slash),
    ], [
        (try_begin),
            (eq, "$caesim_autobuild", 1),
            (display_message, "str_autobuild_off"),
            (assign, "$caesim_autobuild", 0),
        (else_try),
            (display_message, "str_autobuild_on"),
            (assign, "$caesim_autobuild", 1),
        (try_end),
    ]),

    (0, 0, 0, [
        (key_clicked, key_numpad_multiply),
    ], [
        (try_begin),
            (eq, "$caesim_build_prop", "spr_crate_explosive"),
            (assign, "$caesim_build_prop", "spr_mm_stakes_construct"),
        (else_try),
            (val_add, "$caesim_build_prop", 1),
        (try_end),
        
        (str_clear, s0),
        (try_begin),
            (eq, "$caesim_build_prop", "spr_mm_stakes_construct"),
            (str_store_string, s0, "str_mm_stakes_construct"),# "@Chevaux de Frise"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_mm_stakes2_construct"),
            (str_store_string, s0, "str_mm_stakes2_construct"),#"@Stakes"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_sandbags_construct"),
            (str_store_string, s0, "str_sandbags_construct"),#"@Sandbags"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_chevaux_de_frise_tri_construct"),
            (str_store_string, s0, "str_chevaux_de_frise_tri_construct"),#"@Chevaux de Frise Small"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_gabiondeploy_construct"),
            (str_store_string, s0, "str_gabion_construct"),#"@Gabion"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_mm_fence1d"),
            (str_store_string, s0, "str_fence_construct"),#"@Fence"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_plank_construct_dummy"),
            (str_store_string, s0, "str_plank_construct"),#"@Plank"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_earthwork1_construct_dummy"),
            (str_store_string, s0, "str_earthwork1_construct"),#"@Earthwork"),
        (else_try),
            (eq, "$caesim_build_prop", "spr_crate_explosive"),
            (str_store_string, s0, "str_explosives_construct"),#"@Explosives"),
        (try_end),
        (display_message, "str_switching_to_s0"),
    ]),

    (0.01, 0, 0, [
        (eq, "$caesim_autobuild", 1),
    ], [
        (call_script, "script_client_get_my_agent"),
        (agent_is_active, reg0),
        (agent_get_team,":team_no",reg0),
        
        (try_begin),
            (eq,":team_no",0),
            (assign,":team_build_points","$g_team_1_build_points"),
        (else_try),
            (assign,":team_build_points","$g_team_2_build_points"),
        (try_end),
        
        (store_add, ":cost_index", construct_costs_offset, "$caesim_build_prop"),
        (troop_get_slot, ":cost", "trp_track_select_dummy", ":cost_index"),
        
        (try_begin),
            (gt, ":team_build_points", ":cost"),
            (multiplayer_send_int_to_server, multiplayer_event_player_build_prop, "$caesim_build_prop"),
            (assign, "$caesim_buildpoints_sent", 0),
        (else_try),
            (eq, "$caesim_buildpoints_sent", 0),
            (try_begin),
                (eq,":team_no",0),
                (multiplayer_send_2_int_to_server, multiplayer_event_admin_set_mod_variable, mod_variable_build_points_1, 0),
                (multiplayer_send_2_int_to_server, multiplayer_event_admin_set_mod_variable, mod_variable_build_points_1, 1000),
            (else_try),
                (multiplayer_send_2_int_to_server, multiplayer_event_admin_set_mod_variable, mod_variable_build_points_2, 0),
                (multiplayer_send_2_int_to_server, multiplayer_event_admin_set_mod_variable, mod_variable_build_points_2, 1000),
            (try_end),
            (assign, "$caesim_buildpoints_sent", 1),
        (try_end),
    ]),
]

strings += [
    ("switching_to_s0", "Switching to {s0}"),
    ("autobuild_on", "Autobuild ON"),
    ("autobuild_off", "Autobuild OFF"),
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
