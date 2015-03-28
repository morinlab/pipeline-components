"""
component_params.py

@author: bgrande
"""


input_files = {"fastq_files": "__REQUIRED__"}

output_files = {"output_dir": "__REQUIRED__",
                "interval_file": "__OPTIONAL__"}

input_params = {"num_reads": 75000000,
                "num_buffer": 5000000,
                "no_compression": "__FLAG__"}

return_value = []
