"""
component_params.py
@author: jgrewal
"""

## here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
                 'input_dir' : '__REQUIRED__', #This is a directory containing all bams to be merged
		}

## here goes the list of the output files.
output_files = {
		'output_file' : '__REQUIRED__',
                }

## here goes the list of the input parameters excluding input/output files.
input_params = {
		'java_mem' : '4G',
                'val_stringency' : 'SILENT', #'__REQUIRED__',
                'verbosity' : 'INFO',
                'quiet' : 'false',
		'sort_order': 'coordinate',
		'use_threading': 'true',
                'input_regex': '*.bam', #regex to identify the batch of input files with
		'delete_input' : 'true'
		}

## here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
