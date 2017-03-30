#
# Adds name tags to playes. Works with zoom.py
#
#   page up - toggle name tags
#   page down - toggle name tag distance limit
#

from pp import *

try_for_players = 17

triggers = [
    (0, 0, ti_once, [], [
        (assign, "$caesim_name_tags_on", 0),
        (assign, "$caesim_name_tags_distance_limit", 1),
    ]),
    
    (1, 0, 0, [
        (eq, "$caesim_name_tags_on", 1),
        (neg|is_presentation_active, "prsnt_caesim_name_tags"),
    ], [
        (start_presentation, "prsnt_caesim_name_tags"),
    ]),
    
    (0, 0, 0, [
        (key_clicked, key_page_up),
    ], [
        (try_begin),
            (eq, "$caesim_name_tags_on", 1),
            (display_message, "@Name tags OFF"),
            (assign, "$caesim_name_tags_on", 0),
        (else_try),
            (display_message, "@Name tags ON"),
            (assign, "$caesim_name_tags_on", 1),
        (try_end),
    ]),

    (0, 0, 0, [
        (key_clicked, key_page_down),
    ], [
        (try_begin),
            (eq, "$caesim_name_tags_distance_limit", 1),
            (display_message, "@Name tag distance limit OFF"),
            (assign, "$caesim_name_tags_distance_limit", 0),
        (else_try),
            (display_message, "@Name tag distance limit ON"),
            (assign, "$caesim_name_tags_distance_limit", 1),
        (try_end),
    ]),
]

presentations += [
    ("caesim_name_tags", prsntf_read_only|prsntf_manual_end_only, 0, [
        (ti_on_presentation_load, [
            (set_fixed_point_multiplier, 1000),
            (display_message, "@Starting overlay"),
            
            ] + template(dict(
                id = range(0, multiplayer_player_loops_end),
            ), [
                (create_text_overlay, "$caesim_name_tag_$id", s0),
                (overlay_set_color, "$caesim_name_tag_$id", 0xffffff),
                (overlay_set_display, "$caesim_name_tag_$id", 0),
                
                (position_set_x, pos0, 800),
                (position_set_y, pos0, 800),
                (overlay_set_size, "$caesim_name_tag_$id", pos0)
            ]) + [
            
            (presentation_set_duration, 999999),
        ]),
        (ti_on_presentation_run, [
            (set_fixed_point_multiplier, 1000),
            
            (try_begin),
                (neq, "$caesim_name_tags_on", 1),
                (presentation_set_duration, 0),
            (try_end),
            
            (init_position, pos0),
            (init_position, pos1),
            (init_position, pos2),
            (init_position, pos3),
            
            (call_script, "script_client_get_my_agent"),
            (assign, ":my_agent", reg0),
            
            (multiplayer_get_my_player, ":my_player"),
            (player_get_team_no,  ":my_team", ":my_player"),
            
            ] + template(dict(
                id = range(0, multiplayer_player_loops_end),
            ), [
                (try_begin),
                    (assign, ":player_no", "~$id"),
                    (player_is_active, ":player_no"),
                    (player_get_agent_id, ":agent_id", ":player_no"),
                    (neq, ":agent_id", ":my_agent"),
                    (agent_is_active, ":agent_id"),
                    (agent_is_alive, ":agent_id"),
                    
                    (agent_get_position, pos1, ":agent_id"),
                    (position_move_z, pos1, 200),
                    
                    (mission_cam_get_position, pos0),
                    (get_distance_between_positions_in_meters, ":distance", pos1, pos0),
                    
                    (this_or_next|neq, "$caesim_name_tags_distance_limit", 1),
                    (lt, ":distance", 40),
                    
                    (position_get_screen_projection, pos2, pos1),
                    (overlay_set_position, "$caesim_name_tag_$id", pos2),
                    
                    
                    (store_zoom_amount, ":zoom_amount"),
                    (try_begin),
                        (neg|gt, ":zoom_amount", 0),
                        (val_mul, ":distance", 10),
                    (else_try),
                        (assign, ":distance", 0),
                    (try_end),
                    (store_sub, ":size", 800, ":distance"),
                    (position_set_x, pos3, ":size"),
                    (position_set_y, pos3, ":size"),
                    (overlay_set_size, "$caesim_name_tag_$id", pos3),
                    
                    (str_store_player_username, s0, ":player_no"),
                    (assign, reg1, ":distance"),
                    (overlay_set_text, "$caesim_name_tag_$id", "@{s0}"),
                    
                    (player_get_team_no,  ":team", ":player_no"),
                    (try_begin),
                        (neq, ":my_team", 2),
                        (neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
                        (neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
                        (try_begin),
                            (eq, ":team", ":my_team"),
                            (overlay_set_color, "$caesim_name_tag_$id", 0x00ff00),
                        (else_try),
                            (overlay_set_color, "$caesim_name_tag_$id", 0xff0000),
                        (try_end),
                    (try_end),
                    
                    (overlay_set_display, "$caesim_name_tag_$id", 1),
                (else_try),
                    (overlay_set_display, "$caesim_name_tag_$id", 0),
                (try_end),
            ]) + [
        ]),
    ]),
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
