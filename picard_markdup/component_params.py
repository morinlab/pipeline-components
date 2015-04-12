"""
component_params.py
@author: jgrewal
"""

## here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
                 'input_file' : '__REQUIRED__', 
                }

## here goes the list of the output files.
output_files = {
                 'output_file' : '__REQUIRED__',
                }

## here goes the list of the input parameters excluding input/output files.
input_params = {
                'val_stringency' : 'SILENT', #'__REQUIRED__',
                'verbosity' : 'INFO',
                'quiet' : 'false',
                 'metrics_file' : '__REQUIRED__',
                }

## here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
