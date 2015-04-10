"""
component_params.py

"""

## here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
                 'input_filenames' : '__REQUIRED__', 
		 'out_files' : '__REQUIRED__',
                }

## TODO: here goes the list of the output files.
output_files = {
#                 'output_file1' : '__REQUIRED__',
#                 'output_file1' : None
                }

## TODO: here goes the list of the input parameters excluding input/output files.
input_params = {
		'out_dir': './',
		'in_dir' : './',
		'filetype_in' : '__REQUIRED__', #Can be bam or fastq
		'filetype_out' : '__REQUIRED__',
#                 'input_param1' : '__REQUIRED__',
#                 'input_param2' : '__FLAG__',
#                 'input_param3' : None
                }

## TODO: here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
