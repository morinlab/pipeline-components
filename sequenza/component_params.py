"""
component_params.py

@author: bgrande
"""


input_files = {'seq_analyze': '__REQUIRED__',
               'input_normal_bam': '__REQUIRED__',
               'input_tumour_bam': '__REQUIRED__',
               'ref_fa': '__REQUIRED__',
               'seq_utils': '__REQUIRED__',
               'gc_ref': '__REQUIRED__'}

output_files = {'output_dir': '__REQUIRED__'}

input_params = {'gender': '__OPTIONAL__',
                'sample_id': '__OPTIONAL__'}

return_value = []
