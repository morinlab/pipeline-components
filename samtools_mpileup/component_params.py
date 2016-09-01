"""
component_params.py

@author: ppararaj
"""


input_files = {"input_bam": "__REQUIRED__"}

output_files = {"output_pileup": "__REQUIRED__"}

input_params = {"fasta-ref": "__REQUIRED__",
		"illumina1.3+": "__FLAG__",
		"count-orphans": "__FLAG__",
		"bam-list": "__OPTIONAL__",
		"no-BAQ": "__FLAG__",
		"adjust-MQ": "__OPTIONAL__",
		"max-depth": "__OPTIONAL__",
		"redo-BAQ": "__FLAG__",
		"fasta-ref": "__OPTIONAL__",
		"exclude-RG": "__OPTIONAL__",
		"positions": "__OPTIONAL__",
		"min-MQ": "__OPTIONAL__",
		"min-BQ": "__OPTIONAL__",
		"region": "__OPTIONAL__",
		"ignore-RG": "__FLAG__",
		"incl-flags": "__OPTIONAL__",
		"excl-flags": "__OPTIONAL__",
		"ignore-overlaps": "__FLAG__",
		"output": "__OPTIONAL__",
		"BCF": "__FLAG__",
		"VCF": "__FLAG__",
		"output-BP": "__FLAG__",
		"output-MQ": "__FLAG__",
		"output-tags": "__OPTIONAL__",
		"uncompressed": "__OPTIONAL__",
		"ext-prob": "__OPTIONAL__",
		"gap-frac": "__OPTIONAL__",
		"tandem-qual": "__OPTIONAL__",
		"skip-indels": "__FLAG__",
		"max-idepth": "__OPTIONAL__",
		"min-ireads": "__OPTIONAL__",
		"open-prob": "__OPTIONAL__",
		"per-sample-mF": "__FLAG__",
		"platforms": "__OPTIONAL__"
		}

return_value = []
