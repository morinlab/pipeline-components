"""
component_params.py
@author: jgrewal
"""

## here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
                 'input_maf' : '__REQUIRED__', 
                 'input_tbam' : '__REQUIRED__',
		 'input_nbam' : '__REQUIRED__',
		 'reference' : '__REQUIRED__'
                }

## here goes the list of the output files.
output_files = {
                 'output_augmaf' : '__REQUIRED__',
                }

## here goes the list of the input parameters excluding input/output files.
input_params = {
#                 'input_param1' : '__REQUIRED__',
#                 'input_param2' : '__FLAG__',
#                 'input_param3' : None
                }

## TODO: here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
