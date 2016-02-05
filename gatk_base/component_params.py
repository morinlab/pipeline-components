"""
component_params.py

@author: bgrande
"""


input_files = {"input_file": "__OPTIONAL__",
               "intervals": "__OPTIONAL__",
               "excludeIntervals": "__OPTIONAL__",
               "reference_sequence": "__OPTIONAL__",
               "BQSR": "__OPTIONAL__",
               "read_group_black_list": "__OPTIONAL__"}

output_files = {"log_to_file": "__OPTIONAL__"}

input_params = {"analysis_type": "__REQUIRED__",
                "java_memory": "5G",
                "arg_file": "__OPTIONAL__",
                "showFullBamList": "__FLAG__",
                "read_buffer_size": "__OPTIONAL__",
                "phone_home": "__OPTIONAL__",
                "gatk_key": "__OPTIONAL__",
                "tag": "__OPTIONAL__",
                "read_filter": "__OPTIONAL__",
                "disable_read_filter": "__OPTIONAL__",
                "interval_set_rule": "__OPTIONAL__",
                "interval_merging": "__OPTIONAL__",
                "interval_padding": "__OPTIONAL__",
                "nonDeterministicRandomSeed": "__FLAG__",
                "maxRuntime": "__OPTIONAL__",
                "maxRuntimeUnits": "__OPTIONAL__",
                "downsampling_type": "__OPTIONAL__",
                "downsample_to_fraction": "__OPTIONAL__",
                "downsample_to_coverage": "__OPTIONAL__",
                "baq": "__OPTIONAL__",
                "baqGapOpenPenalty": "__OPTIONAL__",
                "refactor_NDN_cigar_string": "__FLAG__",
                "fix_misencoded_quality_scores": "__FLAG__",
                "allow_potentially_misencoded_quality_scores": "__FLAG__",
                "useOriginalQualities": "__FLAG__",
                "defaultBaseQualities": "__OPTIONAL__",
                "performanceLog": "__OPTIONAL__",
                "quantize_quals": "__OPTIONAL__",
                "disable_indel_quals": "__FLAG__",
                "emit_original_quals": "__FLAG__",
                "preserve_qscores_less_than": "__OPTIONAL__",
                "globalQScorePrior": "__OPTIONAL__",
                "validation_strictness": "__OPTIONAL__",
                "remove_program_records": "__FLAG__",
                "keep_program_records": "__FLAG__",
                "sample_rename_mapping_file": "__OPTIONAL__",
                "unsafe": "__OPTIONAL__",
                "sites_only": "__FLAG__",
                "never_trim_vcf_format_field": "__FLAG__",
                "bam_compression": "__OPTIONAL__",
                "simplifyBAM": "__FLAG__",
                "disable_bam_indexing": "__FLAG__",
                "generate_md5": "__FLAG__",
                "num_threads": "__OPTIONAL__",
                "num_cpu_threads_per_data_thread": "__OPTIONAL__",
                "monitorThreadEfficiency": "__FLAG__",
                "num_bam_file_handles": "__OPTIONAL__",
                "pedigree": "__OPTIONAL__",
                "pedigreeString": "__OPTIONAL__",
                "pedigreeValidationType": "__OPTIONAL__",
                "variant_index_type": "__OPTIONAL__",
                "variant_index_parameter": "__OPTIONAL__",
                "logging_level": "__OPTIONAL__"}

return_value = []
