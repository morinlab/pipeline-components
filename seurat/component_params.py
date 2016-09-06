"""
component_params.py

@author: ppararaj
"""


input_files = {
		"I:dna_normal": "__REQUIRED__",
		"I:dna_tumor": "__REQUIRED__",
              }

output_files = {
		"out": "__REQUIRED__",
		"go": "__REQUIRED__",
		"output_snv": "__REQUIRED__",
		"output_indel": "__REQUIRED__"
               }

input_params = {
		"I:rna_normal": "__OPTIONAL__",
                "I:rna_tumor": "__OPTIONAL__",
		"T": "Seurat",
		"reference_sequence": "__REQUIRED__",
		"java_memory": "__OPTIONAL__",
		"read_buffer_size": "__OPTIONAL__",
		"phone_home": "__OPTIONAL__",
		"gatk_key": "__OPTIONAL__",
		"read_filter": "__OPTIONAL__",
		"intervals": "__OPTIONAL__",
		"excludeIntervals": "__OPTIONAL__",
		"interval_set_rule": "__OPTIONAL__",
		"interval_merging": "__OPTIONAL__",
		"nonDeterministicRandomSeed": "__FLAG__",
		"downsampling_type": "__OPTIONAL__",
		"downsample_to_fraction": "__OPTIONAL__",
		"downsample_to_coverage": "__OPTIONAL__",
		"baq": "__OPTIONAL__",
		"baqGapOpenPenalty": "__OPTIONAL__",
		"performanceLog": "__OPTIONAL__",
		"useOriginalQualities": "__FLAG__",
		"BQSR": "__OPTIONAL__",
		"defaultBaseQualities": "__OPTIONAL__",
		"validation_strictness": "__OPTIONAL__",
		"unsafe": "__OPTIONAL__",
		"num_bam_file_handles": "__OPTIONAL__",
		"read_group_black_list": "__OPTIONAL__",
		"pedigree": "__OPTIONAL__",
		"pedigreeString": "__OPTIONAL__",
		"pedigreeValidationType": "__OPTIONAL__",
		"logging_level": "__OPTIONAL__",
		"log_to_file": "__OPTIONAL__",
		"filter_mismatching_base_and_quals": "__FLAG__",
		"prior_alpha": "__OPTIONAL__",
		"prior_beta": "__OPTIONAL__",
		"refnormal_only": "__FLAG__",
		"both_strands": "__FLAG__",
		"coding_only": "__FLAG__",
		"rna_snv": "__FLAG__",
		"pileup_info": "__FLAG__",
		"min_event_quality": "__OPTIONAL__",
		"expected_insert_size": "__OPTIONAL__",
		"maximum_mismatches": "__OPTIONAL__",
		"indels": "__FLAG__",
		"loh": "__FLAG__",
		"structvar": "__FLAG__",
		"metrics": "__FLAG__",
		"debug": "__FLAG__",
		"min_base_quality_score": "__OPTIONAL__",
		"min_coverage": "__OPTIONAL__",
		"output_all": "__FLAG__",
		"refseq": "__OPTIONAL__"
               }

return_value = []
