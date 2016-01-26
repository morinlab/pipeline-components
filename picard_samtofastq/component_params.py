"""
component_params.py
@author: jgrewal
Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

## here goes the list of the input files. Use flags: 
## '__REQUIRED__' to make it required
## '__FLAG__' to make it a flag or switch.
input_files  = {
		'input_bam': '__REQUIRED__',
                }

## here goes the list of the output files.
output_files = {
		'output_dir': './',
                'outfile1' : '__OPTIONAL__',
                'outfile2' : '__OPTIONAL__' ,
		'log_file': 'samToFastq_run.log'
		}

## here goes the list of the input parameters excluding input/output files.
input_params = {
		'javamem' : '4G',
		'no_compression': False,
		'output_per_rg' : 'false',
		'rg_tag' : 'PU',
		'rereverse_bases' : 'false', #'__FLAG__',
		'interleave' : 'false',
         	'include_non_pf_reads' : 'false', #'__FLAG__',
		'clipping_attribute' : 'null', #'__OPTIONAL__',
         	'clipping_action' : 'null', #'__OPTIONAL__',
		'read1_trim' : '0',
		'read1_maxbases' : 'null',
		'read2_trim' : '0',
		'read2_maxbases' : 'null',
		'include_nonprimary' : 'false',
	        'val_stringency' : 'SILENT', #'__REQUIRED__',
		'verbosity' : 'INFO',
		'quiet' : 'false',
		'tmp_dir' : 'null'
		}

## here goes the return value of the component_seed. 
## DO NOT USE, Not implemented yet!
return_value = []

                    
                    
