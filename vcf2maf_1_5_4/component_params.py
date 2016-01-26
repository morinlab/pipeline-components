"""
component_params.py

@author: bgrande
"""


input_files = {"input_vcf": "__OPTIONAL__",
               "input_vep": "__OPTIONAL__",
               "input_snpeff": "__OPTIONAL__",
               "vep_path": "__OPTIONAL__",
               "vep_data": "__OPTIONAL__",
               "ref_fasta": "__OPTIONAL__",
               "snpeff_path": "__OPTIONAL__",
               "snpeff_data": "__OPTIONAL__",
               "custom_enst": "__OPTIONAL__"}

output_files = {"output_maf": "__OPTIONAL__"}

input_params = {"tumor_id": "__OPTIONAL__",
                "normal_id": "__OPTIONAL__",
                "vcf_tumor_id": "__OPTIONAL__",
                "vcf_normal_id": "__OPTIONAL__",
                "use_snpeff": "__OPTIONAL__",
                "vep_forks": "__OPTIONAL__",
                "snpeff_db": "__OPTIONAL__",
                "ncbi_build": "__OPTIONAL__",
                "maf_center": "__OPTIONAL__",
                "min_hom_vaf": "__OPTIONAL__"}

return_value = []
