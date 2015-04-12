"""
component_params.py

"""

## here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
		'input_bam' : '__REQUIRED__'
                }

## here goes the list of the output files.
output_files = {
		'output_paired' : '__REQUIRED__',
		'output_unpaired' : '__REQUIRED__',
		'output_readnames' : '__REQUIRED__'
                }

## here goes the list of the input parameters excluding input/output files.
input_params = {
		'verbosity': 'INFO',
		'quiet': 'false',
		'val_stringency': 'STRICT',
		'sort_order' : 'coordinate',
		'delete_input' : 'false',
#                 'input_param2' : '__FLAG__',
#                 'input_param3' : None
                }

## here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
