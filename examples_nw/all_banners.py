#
# Adds all possible banners to selection
#

from pp import *

i = 0
for presentation in presentations:
	if presentation[0] == "game_profile_banner_selection":
		for trigger in presentation[3]:
			if trigger[0] == ti_on_presentation_load:
				try:
					while True:
						trigger[1].pop(trigger[1].index((lt, ":cur_banner_mesh", "mesh_banner_d11")))
				except ValueError:
					pass
				
				trigger[1][trigger[1].index((try_for_range, ":cur_banner_mesh", banner_meshes_begin, banner_meshes_end_minus_one))] = (try_for_range, ":cur_banner_mesh", banner_meshes_begin, "mesh_meshes_end")
			
				index = trigger[1].index((create_image_button_overlay, reg1, ":cur_banner_mesh", ":cur_banner_mesh"))
				trigger[1][index:index+1] = [
					(try_begin),
						(this_or_next|eq, ":cur_banner_mesh", "mesh_banner_kingdom_e"),
						(eq, ":cur_banner_mesh", "mesh_banner_f21"),
						(create_image_button_overlay, reg1, "mesh_white_plane", "mesh_white_plane"),
					(else_try),
						(create_image_button_overlay, reg1, ":cur_banner_mesh", ":cur_banner_mesh"),
					(try_end),
				]
			elif trigger[0] == ti_on_presentation_event_state_change:
				trigger[1][trigger[1].index((val_mod, "$g_presentation_page_no", 5))] = (val_mod, "$g_presentation_page_no", (mesh_meshes_end-mesh_banner_a01)//15)
				trigger[1][trigger[1].index((assign, ":end_cond", banner_meshes_end_minus_one))] = (assign, ":end_cond", "mesh_meshes_end")
				
	i += 1
