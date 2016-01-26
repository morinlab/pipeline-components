"""
component_params.py

@author: bgrande
"""


input_files = {"input_bam": "__REQUIRED__",
               "bam_list": "__OPTIONAL__",
               "fasta_ref": "__OPTIONAL__",
               "exclude_RG": "__OPTIONAL__",
               "positions": "__OPTIONAL__"}

output_files = {"output": "__REQUIRED__"}

input_params = {"illumina1.3+": "__FLAG__",
                "count_orphans": "__FLAG__",
                "no_BAQ": "__FLAG__",
                "redo_BAQ": "__FLAG__",
                "ignore_RG": "__FLAG__",
                "ignore_overlaps": "__FLAG__",
                "BCF": "__FLAG__",
                "VCF": "__FLAG__",
                "output_BP": "__FLAG__",
                "output_MQ": "__FLAG__",
                "uncompressed": "__FLAG__",
                "skip_indels": "__FLAG__",
                "per_sample_mF": "__FLAG__",
                "adjust_MQ": "__OPTIONAL__",
                "max_depth": "__OPTIONAL__",
                "min_MQ": "__OPTIONAL__",
                "min_BQ": "__OPTIONAL__",
                "region": "__OPTIONAL__",
                "incl_flags": "__OPTIONAL__",
                "excl_flags": "__OPTIONAL__",
                "output_tags": "__OPTIONAL__",
                "ext_prob": "__OPTIONAL__",
                "gap_frac": "__OPTIONAL__",
                "tandem_qual": "__OPTIONAL__",
                "max_idepth": "__OPTIONAL__",
                "min_ireads": "__OPTIONAL__",
                "open_prob": "__OPTIONAL__",
                "platforms": "__OPTIONAL__",
                "compress_pileup": "__FLAG__"}

return_value = []
