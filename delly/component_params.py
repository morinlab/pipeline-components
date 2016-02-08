"""
component_params.py

@author: bgrande
"""


input_files = {'tumour_bam': '__REQUIRED__',
               'normal_bam': '__REQUIRED__'}

output_files = {'vcf_file': '__REQUIRED__'}

input_params = {'sv_type': '__REQUIRED__',
                'reference_fasta': '__REQUIRED__',
                'excluded_regions': '__OPTIONAL__',
                'num_threads': '__OPTIONAL__',
                'map_qual': '__OPTIONAL__',
                'mad_cutoff': '__OPTIONAL__',
                'min_flank': '__OPTIONAL__',
                'vcfgeno': '__OPTIONAL__',
                'geno_qual': '__OPTIONAL__'}

return_value = []
