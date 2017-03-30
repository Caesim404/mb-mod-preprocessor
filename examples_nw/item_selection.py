#
# Allows selecting all items
#


from pp import *

item_select = [
    (multiplayer_get_my_player, ":my_player"),
    (player_is_active, ":my_player"),
    (player_get_troop_id, ":my_troop", ":my_player"),
    
    (call_script, "script_multiplayer_get_troop_class", ":my_troop"),
    (assign, ":my_troop_class", reg0),
    
    (assign,":cur_y2", 370),
] + template(dict(
    i = range(9),
), [
    (val_sub, ":cur_y", 35),
    (val_sub, ":cur_y2", 35),
    
    (create_combo_label_overlay, "$caesim_item_select_$i"),
    (position_set_y, pos8, ":cur_y2"),
    (overlay_set_position, "$caesim_item_select_$i", pos8),
    (position_set_x, pos7, 1000),
    (position_set_y, pos7, 950),
    (overlay_set_size, "$caesim_item_select_$i", pos7),
    (overlay_add_item, "$caesim_item_select_$i", "@Empty"),
    
    (store_add, ":slot", slot_player_selected_item_indices_begin, "~$i"),
    (player_get_slot, ":target_item", ":my_player", ":slot"),
    (assign, ":selected_item", 0),
    
    (troop_get_inventory_capacity, ":inventory_size", ":my_troop"),
    (val_sub, ":inventory_size", num_equipment_kinds),
    (assign, ":index", 1),
    (try_for_range, ":i", 0, ":inventory_size"),
        (troop_get_inventory_slot, ":item", ":my_troop", ":i"),
        
        (gt, ":item", -1),
        (item_get_type, ":item_type", ":item"),
        
        (str_store_item_name, s3, ":item"),
        (item_get_slot, ":item_class", ":item", slot_item_multiplayer_item_class),
        
        (assign, ":valid", 0),
        (try_begin),
            (eq, "~$i", ek_horse),
            (is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
            (eq, "$g_horses_are_avaliable", 1),
            (assign, ":valid", 1),
        (else_try),
            (eq, "~$i", ek_head),
            (is_between, ":item_class", multi_item_class_type_heads_begin, multi_item_class_type_heads_end),
            (assign, ":valid", 1),
        (else_try),
            (eq, "~$i", ek_body),
            (is_between, ":item_class", multi_item_class_type_bodies_begin, multi_item_class_type_bodies_end),
            (assign, ":valid", 1),
        (else_try),
            (eq, "~$i", ek_foot),
            (is_between, ":item_class", multi_item_class_type_feet_begin, multi_item_class_type_feet_end),
            (assign, ":valid", 1),
        (else_try),
            (eq, "~$i", ek_gloves),
            (is_between, ":item_class", multi_item_class_type_gloves_begin, multi_item_class_type_gloves_end),
            (assign, ":valid", 1),
        (else_try),
            (is_between, "~$i", 0, 4),
            # (display_message, "@i=$i"),
            # (neq, ":item_type", itp_type_horse),
            (try_begin),
                (this_or_next|eq,":my_troop_class", multi_troop_class_mm_sapper),
                (this_or_next|eq, ":my_troop_class", multi_troop_class_mm_artillery),
                (eq, ":my_troop_class", multi_troop_class_mm_rocket),
                (assign, ":valid", 1),
            (else_try),
                (try_begin),
                    (eq, "~$i", 0),
                    (this_or_next|eq, ":item_class", multi_item_class_type_flag),
                    (eq, ":item_class", multi_item_class_type_misc),
                    (assign, ":valid", 1),
                (else_try),
                    (eq, "~$i", 1),
                    (this_or_next|eq, ":item_class", multi_item_class_type_gun),
                    (this_or_next|eq, ":item_class", multi_item_class_type_lance),
                    (eq, ":item_class", multi_item_class_type_instrument),
                    (assign, ":valid", 1),
                (else_try),
                    (eq, "~$i", 2),
                    (eq, ":item_class", multi_item_class_type_sword),
                    (assign, ":valid", 1),
                (else_try),
                    (eq, "~$i", 3),
                    (eq, ":item_class", multi_item_class_type_bullet),
                    (assign, ":valid", 1),
                (try_end),
            (try_end),
        (try_end),
        
        (try_begin),
            (eq, ":valid", 1),
            
            (overlay_add_item, "$caesim_item_select_$i", s3),
            
            (try_begin),
                (gt, ":target_item", 0),
                (eq, ":target_item", ":item"),
                (assign, ":selected_item", ":index"),
            (try_end),
            
            (val_add, ":index", 1),
        (try_end),
        
        (overlay_set_val, "$caesim_item_select_$i", ":selected_item"),
    (try_end),
])

item_select_change = template(dict(
    i = range(4) + [4,8],
), [
    (else_try),
        (eq, ":object", "$caesim_item_select_$i"),
        (store_trigger_param_2, ":value"),
        
        (multiplayer_get_my_player, ":my_player"),
        (player_is_active, ":my_player"),
        (store_add, ":slot", slot_player_selected_item_indices_begin, "~$i"),
        
        (try_begin),
            (eq, ":value", 0),
            (assign, ":item", -1),
        (else_try),
            (player_get_troop_id, ":my_troop", ":my_player"),
            (troop_get_inventory_capacity, ":inventory_size", ":my_troop"),
            (val_sub, ":inventory_size", num_equipment_kinds),
            
            (call_script, "script_multiplayer_get_troop_class", ":my_troop"),
            (assign, ":my_troop_class", reg0),
            
            (assign, ":find_i", 1),
            (assign, ":stop", 0),
            (try_for_range, ":i", 0, ":inventory_size"),
                (eq, ":stop", 0),
                
                (troop_get_inventory_slot, ":slot_item", ":my_troop", ":i"),
                
                (gt, ":slot_item", -1),
                (item_get_type, ":item_type", ":slot_item"),
                
                (item_get_slot, ":item_class", ":slot_item", slot_item_multiplayer_item_class),
                
                (assign, ":valid", 0),
                (try_begin),
                    (eq, "~$i", ek_horse),
                    (is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
                    (eq, "$g_horses_are_avaliable", 1),
                    (assign, ":valid", 1),
                (else_try),
                    (eq, "~$i", ek_head),
                    (is_between, ":item_class", multi_item_class_type_heads_begin, multi_item_class_type_heads_end),
                    (assign, ":valid", 1),
                (else_try),
                    (eq, "~$i", ek_body),
                    (is_between, ":item_class", multi_item_class_type_bodies_begin, multi_item_class_type_bodies_end),
                    (assign, ":valid", 1),
                    (assign, ":body_item_example", ":slot_item"), 
                (else_try),
                    (eq, "~$i", ek_foot),
                    (is_between, ":item_class", multi_item_class_type_feet_begin, multi_item_class_type_feet_end),
                    (assign, ":valid", 1),
                (else_try),
                    (eq, "~$i", ek_gloves),
                    (is_between, ":item_class", multi_item_class_type_gloves_begin, multi_item_class_type_gloves_end),
                    (assign, ":valid", 1),
                (else_try),
                    (is_between, "~$i", 0, 4),
                    (try_begin),
                        (this_or_next|eq,":my_troop_class", multi_troop_class_mm_sapper),
                        (this_or_next|eq, ":my_troop_class", multi_troop_class_mm_artillery),
                        (eq, ":my_troop_class", multi_troop_class_mm_rocket),
                        (assign, ":valid", 1),
                    (else_try),
                        (try_begin),
                            (eq, "~$i", 0),
                            (this_or_next|eq, ":item_class", multi_item_class_type_flag),
                            (eq, ":item_class", multi_item_class_type_misc),
                            (assign, ":valid", 1),
                        (else_try),
                            (eq, "~$i", 1),
                            (this_or_next|eq, ":item_class", multi_item_class_type_gun),
                            (this_or_next|eq, ":item_class", multi_item_class_type_lance),
                            (eq, ":item_class", multi_item_class_type_instrument),
                            (assign, ":valid", 1),
                        (else_try),
                            (eq, "~$i", 2),
                            (eq, ":item_class", multi_item_class_type_sword),
                            (assign, ":valid", 1),
                        (else_try),
                            (eq, "~$i", 3),
                            (eq, ":item_class", multi_item_class_type_bullet),
                            (assign, ":valid", 1),
                        (try_end),
                    (try_end),
                (try_end),
                
                (try_begin),
                    (eq, ":valid", 1),
                    
                    (try_begin),
                        (eq, ":find_i", ":value"),
                        (assign, ":item", ":slot_item"),
                        (assign, ":stop", 1),
                    (else_try),
                        (val_add, ":find_i", 1),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
        
        (player_set_slot, ":my_player", ":slot", ":item"),
        (multiplayer_send_2_int_to_server, multiplayer_event_set_item_selection, ":slot", ":item"),
        (assign, reg0, ":slot"),
        (assign, reg1, ":item"),
        
        (str_clear, s4),
        (try_begin),
            (gt, ":item", -1),
            (str_store_item_name, s4, ":item"),
        (try_end),
        (display_message, "@{reg0}: {reg1} ({s4})"),
])

for prsnt in presentations:
    if prsnt[0] == "multiplayer_item_select":
        for trigger in prsnt[3]:
            if trigger[0] == ti_on_presentation_load:
				try:
					i = trigger[1].index((this_or_next|eq,":cur_troop","trp_russian_partizan"))
					trigger[1][i-1:i+128] = item_select
				except ValueError:
					pass
            elif trigger[0] == ti_on_presentation_event_state_change:
                i = trigger[1].index((eq,":object","$g_presentation_obj_item_select"))
                trigger[1][i-1:i+7] = item_select_change

for troop in troops:
    troop[7] = list(set(troop[7]))
 
for script in scripts:
    if script[0] == "multiplayer_client_on_agent_killed_or_wounded_common":
        j = script[1].index((player_get_troop_id,":my_troop_id",":my_player_no"))
        script[1][j-1:j+10] = []
