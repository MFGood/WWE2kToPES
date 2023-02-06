bl_info = {
	"name": "WWE2K to PES",
	"category": "Rigging",
	"author": "MFG",
	"version": "0.0.5"
}

import bpy, fnmatch

def doTheThing(context, booby_physics=0.0):
	obj = context.active_object

	remap = {
		"J_Hips": "dsk_hip",
		"J_Spine1": "sk_belly",
		"J_Chest": "sk_chest",
		"J_Elbow_L": "dsk_forearm_t_l",
		"J_Wrist_L": "sk_hand_l",
		"J_ThumbF1_L": "skh_thumb_mata_l",
		"H_Elbow_L_tw02": "dsk_forearm_l",
		"H_Delt_L_OS01": "dsk_upperarm_l",
		"J_Clavicle_L": "dsk_clavicle_l",
		"J_Neck": "sk_neck",
		"J_Head": "sk_head",
		"H_Leg_Vol_C_L": "dsk_hem_l",
		"J_Leg_L": "sk_thigh_l",
		"J_Knee_L": "sk_leg_l",
		"J_Foot_L": "sk_foot_l",
		"J_Toe_L": "dsk_toe_l",
		"H_Kn_L_OS02": "dsk_knee_l",
		"J_ThumbF2_L": "skh_thumb_mcp_l",
		"J_ThumbF3_L": "skh_thumb_pip_l",
		"J_IndexF0_L": "skh_index_mata_l",
		"J_IndexF1_L": "skh_index_mcp_l",
		"J_IndexF2_L": "skh_index_pip_l",
		"J_IndexF3_L": "skh_index_dip_l",
		"J_MiddleF0_L": "skh_middle_mata_l",
		"J_MiddleF1_L": "skh_middle_mcp_l",
		"J_MiddleF2_L": "skh_middle_pip_l",
		"J_MiddleF3_L": "skh_middle_dip_l",
		"J_RingF0_L": "skh_ring_mata_l",
		"J_RingF1_L": "skh_ring_mcp_l",
		"J_RingF2_L": "skh_ring_pip_l",
		"J_RingF3_L": "skh_ring_dip_l",
		"J_PinkyF0_L": "skh_pinky_mata_l",
		"J_PinkyF1_L": "skh_pinky_mcp_l",
		"J_PinkyF2_L": "skh_pinky_pip_l",
		"J_PinkyF3_L": "skh_pinky_dip_l",
		"J_Elbow_R": "dsk_forearm_t_r",
		"J_Wrist_R": "sk_hand_r",
		"J_ThumbF1_R": "skh_thumb_mata_r",
		"H_Elbow_R_tw02": "dsk_forearm_r",
		"H_Delt_R_OS01": "dsk_upperarm_r",
		"J_Clavicle_R": "dsk_clavicle_r",
		"H_Leg_Vol_C_R": "dsk_hem_r",
		"J_Leg_R": "sk_thigh_r",
		"J_Knee_R": "sk_leg_r",
		"J_Foot_R": "sk_foot_r",
		"J_Toe_R": "dsk_toe_r",
		"H_Kn_R_OS02": "dsk_knee_r",
		"J_ThumbF2_R": "skh_thumb_mcp_r",
		"J_ThumbF3_R": "skh_thumb_pip_r",
		"J_IndexF0_R": "skh_index_mata_r",
		"J_IndexF1_R": "skh_index_mcp_r",
		"J_IndexF2_R": "skh_index_pip_r",
		"J_IndexF3_R": "skh_index_dip_r",
		"J_MiddleF0_R": "skh_middle_mata_r",
		"J_MiddleF1_R": "skh_middle_mcp_r",
		"J_MiddleF2_R": "skh_middle_pip_r",
		"J_MiddleF3_R": "skh_middle_dip_r",
		"J_RingF0_R": "skh_ring_mata_r",
		"J_RingF1_R": "skh_ring_mcp_r",
		"J_RingF2_R": "skh_ring_pip_r",
		"J_RingF3_R": "skh_ring_dip_r",
		"J_PinkyF0_R": "skh_pinky_mata_r",
		"J_PinkyF1_R": "skh_pinky_mcp_r",
		"J_PinkyF2_R": "skh_pinky_pip_r",
		"J_PinkyF3_R": "skh_pinky_dip_r",
		"H_TrapBase_L": "dsk_deltoid_l",
		"H_TrapBase_R": "dsk_deltoid_r",
		"H_Ebw_In_L": "dsk_elbow_l",
		"H_Ebw_In_R": "dsk_elbow_r",
		"J_Shoulder_L": "sk_upperarm_l",
		"J_Shoulder_R": "sk_upperarm_r",
		"H_Leg_Vol_B_R": "dsk_hip",
		"H_Leg_Vol_S_R": "dsk_hip",
		"H_Leg_Vol_F_R": "dsk_hip",
		"H_Leg_Vol_B_L": "dsk_hip",
		"H_Leg_Vol_S_L": "dsk_hip",
		"H_Leg_Vol_F_L": "dsk_hip",
		"J_Spine2": "sk_belly",
		"H_S_blade_L": "sk_chest",
		"H_S_blade_R": "sk_chest",
		"H_Ebw_Out_L": "dsk_elbow_l",
		"H_Neck_tw": "sk_neck",
		"J_Eye_R": "sk_head",
		"J_Eye_L": "sk_head",
		"H_Hip_L_OS1": "sk_thigh_l",
		"H_Kn_L_OS01": "dsk_knee_l",
		"H_Ebw_Out_R": "dsk_elbow_r",
		"H_Hip_R_OS1": "sk_thigh_r",
		"H_Kn_R_OS01": "dsk_knee_r",
		"H_Elbow_L_tw01": "dsk_forearm_t_l",
		"H_Elbow_R_tw01": "dsk_forearm_t_r",
	}

	wildcard_mix = {
		
	}

	delete_list = [
		
	]

	mix_to = {}

	#populate mix_to with the first match for a VG remap or existing remapped VGs
	for vg in obj.vertex_groups:
		if vg.name in remap:
			new_name = remap[vg.name]
			if not new_name in mix_to:
				vg.name = new_name
				mix_to[new_name] = vg
		elif vg.name in remap.values():
			mix_to[vg.name] = vg

	def delete_and_normalize(vg):
		print('Removing '+vg.name)
		obj.vertex_groups.remove(vg)
		bpy.ops.object.vertex_group_normalize_all()

	def weight_mix(a, b, weight=1.0, delete=True):
		print('Mixing '+b.name+' to '+a.name)
		mod = obj.modifiers.new('Vertex Weight Mix', 'VERTEX_WEIGHT_MIX')
		mod.vertex_group_a = a.name
		mod.vertex_group_b = b.name
		mod.mix_mode = 'ADD'
		mod.mix_set = 'ALL'
		mod.mask_constant = weight
		bpy.ops.object.modifier_apply(modifier=mod.name)
		if delete: delete_and_normalize(b)

	def get_in_mix(vg):
		if vg.name in remap: return mix_to[remap[vg.name]]
		return None

	def wildcard_match(vg):
		for pattern, to in wildcard_mix.items():
			if fnmatch.fnmatch(vg.name, pattern):
				return mix_to[wildcard_mix[pattern]]
		return None

	#delete VGs
	for vg in obj.vertex_groups:
		if vg.name in delete_list:
				delete_and_normalize(vg)

	#remap VGs
	for vg in obj.vertex_groups:
		if not vg.name in remap.values():
			to = get_in_mix(vg)
			if to is None:
				to = wildcard_match(vg)
			if to is not None:
				weight_mix(to, vg)

	#create breast movement or mix it back to sk_chest
	if 'breast_l' in mix_to:
		if booby_physics:
			weight_mix(mix_to['sk_chest'], mix_to['breast_l'], weight=0.9, delete=False)
			weight_mix(mix_to['sk_thigh_l'], mix_to['breast_l'], weight=0.1)
			weight_mix(mix_to['sk_chest'], mix_to['breast_r'], weight=0.9, delete=False)
			weight_mix(mix_to['sk_thigh_r'], mix_to['breast_r'], weight=0.1)
		else:
			weight_mix(mix_to['sk_chest'], mix_to['breast_l'])
			weight_mix(mix_to['sk_chest'], mix_to['breast_r'])

	bpy.ops.object.vertex_group_remove_unused()

class WWE2kToPES(bpy.types.Operator):
	"""Convert vertex groups from WWE2K to PES"""
	bl_idname = "object.wwe2k_to_pes"
	bl_label = "PESify WWE2K vertex groups"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		doTheThing(context)

		return {'FINISHED'}

'''
class WWE2kToPESformaDeHorny(bpy.types.Operator):
	"""Convert vertex groups from WWE2K to PES"""
	bl_idname = "object.wwe2k_to_pes_boobies"
	bl_label = "PESify WWE2K vertex groups (w/ Booby Jiggles)"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		doTheThing(context, booby_physics=True)

		return {'FINISHED'}
'''

def register():
	bpy.utils.register_class(WWE2kToPES)
	#bpy.utils.register_class(WWE2kToPESformaDeHorny)

def unregister():
	bpy.utils.unregister_class(WWE2kToPES)
	#bpy.utils.unregister_class(WWE2kToPESformaDeHorny)

if __name__ == "__main__":
	register()

