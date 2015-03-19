"""
component_params.py

@author: bgrande
"""


input_files = {"tumour_bam": "__REQUIRED__",
               "normal_bam": "__REQUIRED__",
               "reference": "__REQUIRED__"}

output_files = {"output_dir": "__REQUIRED__",
                "passed_snvs_vcf": "__REQUIRED__",
                "passed_indels_vcf": "__REQUIRED__"}

input_params = {"is_genome": True,
                "num_threads": 1}

return_value = []
