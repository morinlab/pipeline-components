"""
component_params.py

@author: autogen_component.py
"""


input_files = {'fastq_files': '__REQUIRED__'}

output_files = {'interval_file': '__OPTIONAL__', 'output_dir': '__OPTIONAL__'}

input_params = {'no_compression': False, 'num_buffer': 5000000, 'num_reads': 75000000,
                'no_symlink': False}

return_value = []
