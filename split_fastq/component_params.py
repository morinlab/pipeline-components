"""
component_params.py

@author: bgrande
"""


input_files = {"fastq_1": "__REQUIRED__",
               "fastq_2": "__OPTIONAL__"}

output_files = {"output_prefix": "__REQUIRED__",
                "interval_file": "__OPTIONAL__"}

input_params = {"num_reads": "__OPTIONAL__",
                "num_buffer": "__OPTIONAL__",
                "no_compression": "__FLAG__"}

return_value = []
