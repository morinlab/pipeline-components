"""
component_params.py

@author: ppararaj
"""


input_files = {"normal_pileup","tumour_pileup"}

output_files = {"output_basename"}

input_params = {"output_snp": "__OPTIONAL__",
		"output_indel": "__OPTIONAL__",
		"min_coverage": "__OPTIONAL__",
		"min_coverage_normal": "__OPTIONAL__",
		"min_coverage_tumor": "__OPTIONAL__",
		"min_var_freq": "__OPTIONAL__",
		"min_freq_for_hom": "__OPTIONAL__",
		"normal_purity": "__OPTIONAL__",
		"tumor_purity": "__OPTIONAL__",
		"p_value": "__OPTIONAL__",
		"somatic_p_value": "__OPTIONAL__",
		"strand_filter": "__OPTIONAL__",
		"validation": "__OPTIONAL__",
                "output_vcf": "__OPTIONAL__"
		}

return_value = []
