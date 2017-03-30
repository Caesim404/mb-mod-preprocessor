#
# Adds zoom. Works with name_tags.py
#
#   toggle person key - toggles zoom, but only on a specific person. (default: 1st person)
#   f - enable/disable zoom
#   h - change zoom person to current
#   mouse scroll up - zooms in
#   mouse scroll down - zooms out
#

from pp import *

triggers = [
    (0, 0, ti_once, [], [
        (assign, "$caesim_zoom_amount", 1500),
        (start_presentation, "prsnt_caesim_zoom_key_record_dummy"),
    ]),
    
    ### zoom enable/disable
    (0, 0, 0, [
        (key_clicked, key_f),
        
        (multiplayer_get_my_player, ":player_id"),
        (neg|player_is_busy_with_menus, ":player_id"),
        
        (player_get_agent_id, ":agent_id", ":player_id"),
        (agent_is_active, ":agent_id"),
        
        (neg|is_presentation_active, "prsnt_game_multiplayer_admin_panel"),
        (neg|is_presentation_active, "prsnt_multiplayer_admin_chat"),
    ], [
        (try_begin),
            (eq, "$caesim_zoom_enabled", 1),
            (assign, "$caesim_zoom_enabled", 0),
            (display_message, "@Zoom OFF"),
        (else_try),
            (assign, "$caesim_zoom_enabled", 1),
            (display_message, "@Zoom ON"),
        (try_end),
        (call_script, "script_caesim_apply_zoom"),
    ]),
    
    ### zoom toggle
    (0, 0, 0, [
        (game_key_clicked, gk_cam_toggle),
        
        (multiplayer_get_my_player, ":player_id"),
        (neg|player_is_busy_with_menus, ":player_id"),
        
        (player_get_agent_id, ":agent_id", ":player_id"),
        (agent_is_active, ":agent_id"),
        
        (neg|is_presentation_active, "prsnt_game_multiplayer_admin_panel"),
        (neg|is_presentation_active, "prsnt_multiplayer_admin_chat"),
    ], [
        (try_begin),
            (eq, "$caesim_zoom_on", 1),
            (assign, "$caesim_zoom_on", 0),
        (else_try),
            (assign, "$caesim_zoom_on", 1),
        (try_end),
        (call_script, "script_caesim_apply_zoom"),
    ]),
    
    ### zoom reset
    (0, 0, 0, [
        (key_clicked, key_h),
    ], [
        (assign, "$caesim_zoom_on", 1),
        (call_script, "script_caesim_apply_zoom"),
    ]),
]

scripts += [
    ("caesim_apply_zoom", [
        (try_begin),
            (try_begin),
                (eq, "$caesim_zoom_enabled", 1),
                (eq, "$caesim_zoom_on", 1),
                (set_zoom_amount, "$caesim_zoom_amount"),
            (else_try),
                (set_zoom_amount, 0),
            (try_end),
        (try_end),
    ]),
]

presentations += [
    ("caesim_zoom_key_record_dummy", prsntf_read_only|prsntf_manual_end_only, 0, [
        (ti_on_presentation_load, [
            (set_fixed_point_multiplier, 1000),
            
            (omit_key_once, key_mouse_scroll_up),
            (omit_key_once, key_mouse_scroll_down),
            
            (presentation_set_duration, 999999999),
        ]),
        (ti_on_presentation_run, [
            (try_begin),
                (eq, "$caesim_zoom_enabled", 1),
                (eq, "$caesim_zoom_on", 1),
                
                (multiplayer_get_my_player, ":player_id"),
                (neg|player_is_busy_with_menus, ":player_id"),
                
                (player_get_agent_id, ":agent_id", ":player_id"),
                (agent_is_active, ":agent_id"),
                
                (neg|is_presentation_active, "prsnt_game_multiplayer_admin_panel"),
                (neg|is_presentation_active, "prsnt_multiplayer_admin_chat"),
                
                (omit_key_once, key_mouse_scroll_up),
                (omit_key_once, key_mouse_scroll_down),
                
                (try_begin),
                    (key_clicked, key_mouse_scroll_up),
                    (val_add, "$caesim_zoom_amount", 300),
                    (call_script, "script_caesim_apply_zoom"),
                (else_try),
                    (key_clicked, key_mouse_scroll_down),
                    (val_sub, "$caesim_zoom_amount", 300),
                    (call_script, "script_caesim_apply_zoom"),
                (try_end),
            (else_try),
                (clear_omitted_keys),
            (try_end),
        ]),
    ]),
]

i = 0
for template in mission_templates:
    mission_templates[i] = template[:5] + (template[5] + triggers,)
    i += 1
