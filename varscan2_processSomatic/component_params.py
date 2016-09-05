"""
component_params.py

@author: ppararaj
"""


input_files = {"varscan2_somatic_output": "__REQUIRED__"}

output_files = {"somatic_output": "__REQUIRED__",
                "somatic_hc_output": "__REQUIRED__",
		"germline_output": "__REQUIRED__",
		"germline_hc_output": "__REQUIRED__",
		"loh_output": "__REQUIRED__",
		"loh_hc_output": "__REQUIRED__"}

input_params = {"varscan2_command": "processSomatic",
		"java_memory": "__OPTIONAL__",
		"min_tumor_freq": "__OPTIONAL__",
		"max_normal_freq": "__OPTIONAL__",
		"p_value": "__OPTIONAL__"
		}

return_value = []
