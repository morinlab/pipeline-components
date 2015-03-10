"""
component_params.py

@author: bgrande
"""


input_files = {"fastq_1": "__REQUIRED__",
               "fastq_2": "__OPTIONAL__",
               "reference": "__REQUIRED__",
               "input_dir": "__OPTIONAL__"}

output_files = {"output_bam": "__REQUIRED__",
                "output_dir": "__OPTIONAL__"}

input_params = {"num_threads": "__OPTIONAL__"}

return_value = []
