"""
component_params.py

@author: bgrande
"""


input_files = {"input_vep": "__REQUIRED__"}

output_files = {"output_maf": "__REQUIRED__"}

input_params = {"tumour_id": "__OPTIONAL__",
                "normal_id": "__OPTIONAL__",
                "vcf_tumour_id": "TUMOR",
                "vcf_normal_id": "NORMAL"}

return_value = []
